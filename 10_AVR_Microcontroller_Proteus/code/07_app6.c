/*
 * GccApplication6.c
 *
 * Created: 12.11.2025 17:31:55
 * Author : dino3
 */ 

#define F_CPU 1000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>

volatile uint8_t led   = 0;
volatile int8_t  dir   = 1;
volatile uint8_t run   = 0;
volatile uint8_t count = 0;


ISR(TIMER0_COMP_vect)
{
	if (++count >= 80) {
		count = 0;
		if (run) {
			PORTD = (1 << led);
			if (dir == 1 && led == 7) dir = -1;
			else if (dir == -1 && led == 0) dir = 1;
			led += dir;
		}
	}
}

int main(void)
{
	
	DDRD = 0xFF;
	PORTD = 0x00;

	
	DDRB  &= ~((1<<PB0) | (1<<PB1));
	PORTB |=  (1<<PB0) | (1<<PB1);

	
	TCCR0 = (1<<WGM01)
	| (1<<CS01) | (1<<CS00);
	OCR0  = 155;
	TIMSK = (1<<OCIE0);

	sei();

	while (1)
	{
		
		if (!(PINB & (1<<PB0))) run = 1;
		if (!(PINB & (1<<PB1))) run = 0;
		
	}
}


