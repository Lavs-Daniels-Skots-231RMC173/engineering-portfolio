/*
 * labd4.c
 *
 * Created: 16.11.2025 17:48:39
 * Author : GccApplication8
 */ 

#define F_CPU 8000000UL

#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>
#include <util/delay.h>

volatile uint8_t motor_direction_state = 0;

void init_adc(void);
void init_pwm_timer2(void);
void init_ports(void);
void handle_motor_control(void);
void motor_stop(void);
void motor_state_A(void);
void motor_state_B(void);

int main(void)
{
	init_ports();
	init_adc();
	init_pwm_timer2();
	
	sei();
	
	ADCSRA |= (1 << ADSC);

	while (1)
	{
		handle_motor_control();
	}
}

void init_ports(void)
{
	DDRC = (1 << PC3) | (1 << PC2) | (1 << PC1) | (1 << PC0);
	DDRD = 0xFF;
	DDRB |= (1 << PB7);
	DDRB &= ~((1 << PB0) | (1 << PB1));
	PORTB |= (1 << PB0) | (1 << PB1);
	DDRF &= ~(1 << PF3);
}

void init_adc(void)
{
	ADMUX = (1 << REFS0) | (0x03 & 0x1F);
	ADCSRA = (1 << ADEN) | (1 << ADIE) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

void init_pwm_timer2(void)
{
	
	TCCR2 = (1 << WGM20) | (1 << WGM21) | (1 << COM21) | (1 << CS22);
	
	OCR2 = 0;
}

ISR(ADC_vect)
{
	uint16_t adc_10bit = ADC;
	
	uint8_t pwm_speed = (uint8_t)(adc_10bit >> 2);
	
	OCR2 = pwm_speed;
	
	uint8_t lvl = (uint16_t)(adc_10bit * 9) / 1024;
	
	uint8_t led_mask = (lvl == 0) ? 0x00 : (uint8_t)(0xFF << (8 - lvl));
	
	PORTD = led_mask;
	
	ADCSRA |= (1 << ADSC);
}

void handle_motor_control(void)
{
	uint8_t current_pinb = PINB;

	if (!(current_pinb & (1 << PB0)))
	{
		_delay_ms(50); 
		if (!(PINB & (1 << PB0)))
		{
			motor_direction_state = 1;
		}
	}
	else if (!(current_pinb & (1 << PB1)))
	{
		_delay_ms(50); 
		if (!(PINB & (1 << PB1)))
		{
			motor_direction_state = 2;
		}
	}
	
	if (motor_direction_state == 1)
	{
		motor_state_A();
	}
	else if (motor_direction_state == 2)
	{
		motor_state_B();
	}
	else
	{
		motor_stop();
	}
}

void motor_stop(void)
{
	PORTC = 0x00;
}

void motor_state_A(void)
{
	PORTC = (1 << PC2) | (1 << PC1); 
}

void motor_state_B(void)
{
	PORTC = (1 << PC3) | (1 << PC0); 
}

