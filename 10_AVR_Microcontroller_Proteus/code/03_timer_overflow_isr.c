/*
 * GccApplication2.c
 *
 * Created: 22.10.2025 15:11:35
 * Author : dino3
 */
#include <avr/io.h>
#include <avr/interrupt.h>

int led = 0;
int dir = 1;
int run = 0;
int count = 0;

ISR(TIMER0_OVF_vect)
{
	count++;
	if (count > 50)
	{
		count = 0;
		if (run)
		{
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

	DDRB &= ~((1<<PB0) | (1<<PB1));
	PORTB |=  (1<<PB0) | (1<<PB1);  

	TCCR0 = (1<<CS01) | (1<<CS00);
	TCNT0 = 100;                    
	TIMSK = (1<<TOIE0);              

	sei();

	while(1)
	{
		if (!(PINB & (1<<PB0))) run = 1;
		if (!(PINB & (1<<PB1))) run = 0;   

	}
}