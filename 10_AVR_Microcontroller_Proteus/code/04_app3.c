/*
 * GccApplication3.c
 *
 * Created: 29.10.2025 18:54:47
 * Author : dino3
 */ 

#define F_CPU 1000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>

static uint8_t rev8(uint8_t x){ uint8_t r=0; for(uint8_t i=0;i<8;i++) if(x&(1<<i)) r|=(1<<(7-i)); return r; }
ISR(ADC_vect)
{
	uint16_t v = ADCL; v |= ((uint16_t)ADCH)<<8;       
	uint8_t n = (uint8_t)((v + 1) >> 7);               
	uint8_t m = (n>=8)?0xFF : (n?((1u<<n)-1u):0u);
	PORTD = rev8(m);
}

int main(void)
{
	
	DDRD = 0xFF; PORTD = 0x00;

	DDRB &= ~((1<<PB0)|(1<<PB1)|(1<<PB2));
	PORTB |=  (1<<PB0)|(1<<PB1)|(1<<PB2);

	ADCSRA = 0;

	sei();

	uint8_t prev = PINB;
	while (1)
	{
		uint8_t now = PINB;

		if ( (prev&(1<<PB0)) && !(now&(1<<PB0)) ) {
			ADMUX  = (1<<REFS0) | (0<<ADLAR) | (1<<MUX2) | (0<<MUX1) | (1<<MUX0);
			ADCSRA = (1<<ADEN) | (1<<ADSC) | (1<<ADATE) | (1<<ADIE)             
			| (1<<ADPS2) | (1<<ADPS1);                                    
		}
		
		if ( (prev&(1<<PB1)) && !(now&(1<<PB1)) ) {
			ADCSRA &= ~((1<<ADEN)|(1<<ADIE)); 
		}
		
		if ( (prev&(1<<PB2)) && !(now&(1<<PB2)) ) {
			ADCSRA &= ~((1<<ADEN)|(1<<ADIE));  
			PORTD = 0x00;                      
		}

		prev = now;
	}
}
