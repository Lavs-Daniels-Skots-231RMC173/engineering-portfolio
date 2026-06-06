/*
 * GccApplication1.c
 *
 * Created: 22.10.2025 15:04:43
 * Author : dino3
 */ 

#include <avr/io.h>
#include <util/delay.h>

#define RESET_BTN   (PINB & (1<<PB0))
#define START_BTN   (PINB & (1<<PB1))
#define STOP_BTN    (PINB & (1<<PB2))

int main(void)
{
	DDRD = 0xFF;
	PORTD = 0x00;

	DDRB &= ~((1<<PB0)|(1<<PB1)|(1<<PB2));
	PORTB |= (1<<PB0)|(1<<PB1)|(1<<PB2);

	uint8_t led = 0;
	int8_t dir = 1;
	uint8_t running = 0;

	while(1)
	{
		if(!(RESET_BTN)) {
			led = 0;
			dir = 1;
			running = 0;
			PORTD = (1<<led);
			_delay_ms(200);
		}
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

			for(uint16_t i=0; i<300; i+=10) {
				_delay_ms(10);
				if(!(STOP_BTN)) {
					running = 0;
					_delay_ms(400);
					break;
				}
				if(!(RESET_BTN)) {
					led = 0;
					dir = 1;
					running = 0;
					PORTD = (1<<led);
					_delay_ms(400);
					break;
				}
			}

			if(running) {
				led += dir;
				if(led >= 7) dir = -1;
				else if(led == 0) dir = 1;
			}
		}
	}
}

