<div align="center">

[← back to portfolio](../README.md)

# ⚙️ Project 10

[![Tech1](https://img.shields.io/badge/-Atmel_AVR-009DDA?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-Microchip_Studio-EE3124?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-Proteus-3F51B5?style=for-the-badge)](#)

</div>

---

# 10 — AVR Microcontroller: 9 C Programs + Proteus Simulation

> Mikrokontroleru programmēšana C valodā (AVR / Microchip Studio) ar Proteus simulāciju
> Nine progressive C programs from blinking LEDs to open-loop DC motor speed control (ADC → PWM → H-bridge)

**Context** RTU studiju projekti · RMCE01 · 3rd year · October–December 2025
**Toolchain** Microchip Studio (AVR-GCC) · Proteus Design Suite
**Target** Atmel AVR (8-bit), F_CPU = 1 MHz or 8 MHz depending on program

---

## The progression

Nine C programs over 3 months — from GPIO + button reading to open-loop DC motor speed control with ADC + PWM + H-bridge + LED bar graph. All use AVR runtime headers (`avr/io.h`, `avr/interrupt.h`, `util/delay.h`), register-level config (not Arduino abstractions), simulated in Proteus before any hardware flashing.

> **Open-loop, not closed-loop:** the potentiometer reading maps directly to PWM duty — there is no speed or current feedback. A true closed-loop controller would require an encoder (or current sense) and a PI regulator. Calling out the distinction explicitly because the terminology matters.

| # | Date | Topic | Techniques |
|---|---|---|---|
| 1 | 01.10.2025 | LED running light + START/STOP | GPIO, button polling, debounce |
| 2 | 22.10.2025 | RESET / START / STOP | 3-button state machine |
| 3 | 22.10.2025 | Timer-overflow ISR | `ISR(TIMER0_OVF_vect)`, `sei()` |
| 5 | 29.10.2025 | Timer-compare ISR | `ISR(TIMER0_COMP_vect)`, CTC mode |
| **9** | **19.11.2025** | **DC motor controller** | **ADC + Fast PWM + H-bridge (flagship)** |

---

## Flagship — GccApplication9: open-loop DC motor controller

![GccApplication9 code](images/10_avr_motor_code.png)

*Fig. 1 — `GccApplication9.c` excerpts: ADC + Timer2 Fast PWM register-level init; `ADC_vect` ISR maps 10-bit ADC reading to 8-bit PWM duty + LED bar mask, re-triggers next conversion; H-bridge drives PC0–PC3.*

### Hardware
- **AVR** @ 8 MHz
- **Potentiometer** on ADC ch 3 (PF3) — sets speed
- **DC motor** via external **H-bridge** wired to PC0–PC3
- **PWM** on OC2 (PB7) — duty controls speed
- **8 LEDs** on PORTD — bar graph
- **2 buttons** on PB0/PB1 — direction (fwd / rev / stop)

### Peripheral init

```c
// ADC: 10-bit, AVCC, channel 3, interrupt-driven, /128 prescaler
void init_adc(void) {
    ADMUX  = (1 << REFS0) | (0x03 & 0x1F);
    ADCSRA = (1 << ADEN)  | (1 << ADIE)
           | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

// Timer2: Fast PWM, non-inverting on OC2 (PB7), prescaler /64
void init_pwm_timer2(void) {
    TCCR2 = (1 << WGM20) | (1 << WGM21) | (1 << COM21) | (1 << CS22);
    OCR2  = 0;
}
```

### ADC ISR — the heart

```c
ISR(ADC_vect) {
    uint16_t adc_10bit = ADC;
    uint8_t  pwm_speed = (uint8_t)(adc_10bit >> 2);    // 10→8 bit
    OCR2 = pwm_speed;
    uint8_t  lvl = (uint16_t)(adc_10bit * 9) / 1024;
    uint8_t  led_mask = (lvl == 0) ? 0x00 : (uint8_t)(0xFF << (8 - lvl));
    PORTD = led_mask;
    ADCSRA |= (1 << ADSC);                              // re-trigger
}
```

The trick: **ISR re-triggers ADC at the end** — continuous sampling without polling. Main loop stays free for button input.

### H-bridge state machine

```c
void motor_state_A(void) {  PORTC = (1 << PC2) | (1 << PC1); }  // forward
void motor_state_B(void) {  PORTC = (1 << PC3) | (1 << PC0); }  // reverse
void motor_stop(void)    {  PORTC = 0x00; }
```

### Button debounce + direction

```c
void handle_motor_control(void) {
    uint8_t current_pinb = PINB;
    if (!(current_pinb & (1 << PB0))) {
        _delay_ms(50);
        if (!(PINB & (1 << PB0))) motor_direction_state = 1;    // forward
    }
    else if (!(current_pinb & (1 << PB1))) {
        _delay_ms(50);
        if (!(PINB & (1 << PB1))) motor_direction_state = 2;    // reverse
    }
    if      (motor_direction_state == 1) motor_state_A();
    else if (motor_direction_state == 2) motor_state_B();
    else                                  motor_stop();
}
```

Classic "delay + re-read" debounce — eliminates bouncing without hardware. Reading the pin twice 50 ms apart and only acting if both agree guarantees a true press.

---

## What the system does

1. Operator turns the **potentiometer**
2. ADC samples continuously (interrupt-driven, ~7800 samples/sec at /128 prescaler)
3. Sample sets **OCR2** → PWM duty → motor speed proportionally
4. Sample also sets **LED bar mask** → 0–8 LEDs lit
5. Operator presses fwd/rev → H-bridge switches → motor flips direction
6. No press → motor stops (debounced state ignores noise)

Complete embedded system on 8-bit MCU — sensor input → real-time conversion → PWM actuator → state machine → debouncing → visual feedback.

---

## Files in this folder

### Source (`code/`)
- `01_pr_darbs_LED_running_light.c` — first practical work
- `02_LED_reset_start_stop.c` — 3-button state machine
- `03_timer_overflow_isr.c` — Timer0 overflow ISR
- `06_timer_compare_isr.c` — Timer0 CTC compare ISR
- `09_motor_control_ADC_PWM_Hbridge.c` — **flagship motor controller**
- `04_app3.c`, `05_app4.c`, `07_app6.c`, `08_app8.c` — intermediate

### Proteus simulations (`proteus/`)
- `2_pr_darbs.pdsprj`, `3_pr_darbs.pdsprj`, `4_pr_darbs.pdsprj` — practical-work schematics
- `laboratorijas_5.pdsprj` — lab 5 (December 2025)

---

## How to open & run

**Software:** Microchip Studio (free from Microchip) + Proteus Design Suite (Labcenter Electronics)

1. Microchip Studio: **File → New → Project → GCC C Executable Project**, target `ATmega16`
2. Replace generated `main.c` with chosen `.c` from `code/`
3. **Build → Build Solution** (F7) → `.hex` file
4. Open `.pdsprj` in Proteus
5. Right-click AVR → **Edit Properties** → Program File = `.hex` from step 3
6. Click **Play** — simulation runs, AVR executes code, LEDs blink, buttons respond, ADC reads simulated pot

---

## Skills demonstrated

- **AVR C programming** — datasheet-level, not Arduino
- **Register-level GPIO** — DDRx, PORTx, PINx direct config
- **ADC** — interrupt-driven continuous sampling, AVCC ref, prescaler choice, channel selection
- **Timer/PWM** — Timer2 Fast PWM, OC2 output, OCR2 duty
- **Timer interrupts** — overflow + compare-match ISRs
- **CTC mode** for Timer0
- **ISRs** — `sei()`, vector names, ISR-safe code
- **Bitwise register manipulation** — `(1 << BIT_NAME)` patterns
- **H-bridge motor direction control** with state machine
- **Button debouncing** — software delay + re-read
- **PWM duty from sensor input** — direct ADC → OCR2 mapping (open-loop, no feedback)
- **LED bar graph display** — mask `0xFF << (8 - lvl)`
- **Proteus simulation**
- **Microchip Studio toolchain**

---

## Latvian summary (LV)

AVR mikrokontroleru programmēšanas kursa darbu komplekts (RTU, 3. kurss, oktobris–decembris 2025) — deviņas C valodas programmas, kas progresē no LED mirgošanas līdz **atvērta cikla** (open-loop) līdzstrāvas motora ātruma vadībai. Visas rakstītas reģistru līmenī (nevis Arduino abstrakcijas), debugētas Proteus pirms ielādes.

*Atvērts cikls, nevis slēgts: potenciometrs iestata PWM aizpildījumu tieši; nav ātruma vai strāvas atgriezeniskās saites. Patiess slēgts cikls prasītu enkoderi (vai strāvas mērīšanu) un PI regulatoru.*

**Flagship — GccApplication9 (19.11.2025):** pilna ieguldītā sistēma uz AVR @ 8 MHz:
- **ADC** — 10-bit, AVCC, kanāls 3, pārtraukuma vadīta nepārtraukta konversija (ISR pati pārstartē)
- **Timer2 Fast PWM** — OC2 izeja uz PB7, OCR2 aizpildījums no ADC (10→8 bit ar `>> 2`)
- **LED bar graph** — 8 LED uz PORTD, līmenis ar maskas pieeju `0xFF << (8 - lvl)`
- **H-tilta vadība** — PC0–PC3, virziena valstu mašīna (A / B / Stop)
- **Pogu debounce** — 50 ms aizture + atkārtota nolasīšana

Pirmkods `code/`. Proteus `.pdsprj` faili `proteus/`. Atveramas attiecīgi ar Microchip Studio un Proteus Design Suite.
