/*
 * 3.L.D._Deniss.K.c
 *
 * Created: 29.10.2025 17:28:27
 * Author : DenPC
 */ 

#define F_CPU 1000000UL
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint16_t adc_val = 0;

ISR(ADC_vect)
{
	adc_val = ADC;
}

int main(void)
{

	DDRD = 0xFF;
	PORTD = 0x00;

	ADMUX = (1 << REFS0) | 5;

	SFIOR &= ~((1 << ADTS2) | (1 << ADTS1) | (1 << ADTS0));

	ADCSRA = (1 << ADEN) | (1 << ADATE) | (1 << ADIE) | (1 << ADPS2) | (1 << ADPS1);

	ADCSRA |= (1 << ADSC);

	sei();

	while (1)
	{

		uint8_t lvl = (uint16_t)(adc_val * 9) / 1024;   // 0..8

		uint8_t mask = (lvl == 0) ? 0x00 : (uint8_t)(0xFF << (8 - lvl));

		PORTD = mask;
	}
}
