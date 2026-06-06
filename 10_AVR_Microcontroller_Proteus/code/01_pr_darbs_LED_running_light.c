/*
 * 1-praktiskais darbs - Daniels Skots Lavs.c
 *
 * Created: 01.10.2025 15:09:56
 * Author : dino3
 */ 

#include <avr/io.h>
#include <util/delay.h>

#define START_BTN   (PINB & (1<<PB0))
#define STOP_BTN    (PINB & (1<<PB1))

int main(void)
{
	DDRD = 0xFF;
	PORTD = 0x00;

	DDRB &= ~((1<<PB0)|(1<<PB1));
	PORTB |= (1<<PB0)|(1<<PB1);

	uint8_t led = 0;
	int8_t dir = 1;
	uint8_t running = 0;

	while(1)
	{
		if(!(START_BTN)) {
			running = 1;
			_delay_ms(200);
		}
		if(!(STOP_BTN)) {
			running = 0;
			_delay_ms(200);
		}

		if(running)
		{
			PORTD = (1<<led);

			_delay_ms(300);

			led += dir;
			if(led >= 7) dir = -1;
			else if(led == 0) dir = 1;
		}
	}
}



