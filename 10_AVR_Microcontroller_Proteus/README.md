# 10 — AVR Microcontroller Programming + Proteus Simulation

> Mikrokontroleru programmēšana C valodā (AVR / Microchip Studio) ar Proteus simulāciju
> AVR microcontroller programming in C with Proteus circuit simulation

**Context:** RTU studiju projekti, RMCE01, 3. kurss, oktobris–decembris 2025
**IDEs:** Microchip Studio (AVR-GCC) + Proteus Design Suite
**Target:** Atmel AVR (8-bit)

---

## EN — for GitHub README / EN CV

**AVR Microcontroller Programming — 9 progressive C programs + Proteus simulations (Oct–Dec 2025)**

Progression from blinking LEDs to closed-loop motor control. All programs written in C against the AVR runtime (`avr/io.h`, `avr/interrupt.h`, `util/delay.h`), debugged in Proteus before flashing.

**Skills progression**
| # | Date | Topic | Techniques |
|---|---|---|---|
| 1 | 01.10.2025 | LED running light + START/STOP | GPIO, button polling, software debounce |
| 2 | 22.10.2025 | RESET / START / STOP control | 3-button state machine |
| 3 | 22.10.2025 | Timer-overflow interrupt | `ISR(TIMER0_OVF_vect)`, `sei()` |
| 5 | 29.10.2025 | Timer-compare interrupt | `ISR(TIMER0_COMP_vect)`, CTC mode, `F_CPU` 1 MHz |
| 9 | 19.11.2025 | **DC motor control with ADC + PWM + H-bridge** | full closed-loop system (see below) |

**Project highlight — GccApplication9: DC motor controller (Nov 2025)**

A complete embedded system on AVR (F_CPU = 8 MHz) combining four peripherals:

- **ADC** — 10-bit single-ended, AVCC reference, channel 3, prescaler /128, interrupt-driven continuous conversion (`ADC_vect` ISR re-triggers via `ADCSRA |= (1 << ADSC)`)
- **PWM** — Timer2 Fast PWM, non-inverting OC2 output on PB7, duty from `OCR2 = adc_10bit >> 2` (10→8-bit mapping)
- **LED bar graph** — 8 LEDs on PORTD, level computed as `lvl = (adc * 9) / 1024`, mask `0xFF << (8 - lvl)` — clean monotonic display
- **H-bridge direction control** — PC0–PC3 drive the four bridge transistors; direction state machine:
  - State A → `PC2 | PC1` set (forward)
  - State B → `PC3 | PC0` set (reverse)
  - Stop → `PORTC = 0`
- **Button debouncing** — 50 ms delay + re-read pattern on PB0/PB1

**Proteus simulations**
- `2_pr_darbs.pdsprj`, `3_pr_darbs.pdsprj`, `4_pr_darbs.pdsprj` — practical works wired to AVR + LEDs + buttons + display
- `laboratorijas_5.pdsprj` — lab 5 circuit (December 2025)

Daniel mentioned video recordings of these simulations exist — can be added to portfolio if relevant.

**Skills demonstrated:** AVR C programming · register-level GPIO/ADC/PWM/Timer configuration · interrupt service routines · CTC and Fast PWM modes · H-bridge motor control · PWM duty-cycle control from sensor input · button debouncing · Proteus circuit simulation · Microchip Studio toolchain

---

## LV — for LV CV

**AVR mikrokontroleru programmēšana — 9 progresīvas C programmas + Proteus simulācijas (10.–12. 2025)**

Programmēšanas progresija no LED mirgošanas līdz slēgtas cilpas līdzstrāvas motora vadībai. Visas programmas rakstītas C valodā ar AVR bibliotēkām, debugētas Proteus vidē.

**Galvenais kods — GccApplication9 (19.11.2025):** pilna ieguldītā sistēma uz AVR (8 MHz) ar:
- **ADC** — 10-bit, AVCC bāze, pārtraukuma vadīta nepārtraukta konversija
- **PWM** — Timer2 Fast PWM, OCR2 vadība no ADC
- **LED bar graph** — 8 LED uz PORTD, līmenis ar maskas pieeju
- **H-tilta vadība** — PC0–PC3, virziena valsts mašīna (Stāvoklis A / B / Stop)
- **Pogu debounce** — 50 ms aizture ar atkārtotu nolasīšanu

**Proteus simulācijas:** 4 praktiskie darbi + laboratorijas darbs Nr. 5 — visas shēmas pārbaudītas pirms koda ielādes.

**Prasmes:** AVR C programmēšana · reģistru līmeņa GPIO/ADC/PWM/Timer konfigurēšana · pārtraukumi (ISR) · CTC un Fast PWM režīmi · H-tilta motora vadība · PWM aizpildījuma vadība no sensora · pogu debounce · Proteus shēmu simulācija · Microchip Studio darba plūsma

---

## Files in this folder
**Source code (`code/`):**
- `01_pr_darbs_LED_running_light.c` — first practical work (01.10.2025)
- `02_LED_reset_start_stop.c` — 3-button state machine
- `03_timer_overflow_isr.c` — Timer0 overflow ISR
- `06_timer_compare_isr.c` — Timer0 CTC compare ISR
- `09_motor_control_ADC_PWM_Hbridge.c` — **motor control highlight**
- Additional files: `04_app3.c`, `05_app4.c`, `07_app6.c`, `08_app8.c`

**Proteus simulations (`proteus/`):**
- `2_pr_darbs.pdsprj`, `3_pr_darbs.pdsprj`, `4_pr_darbs.pdsprj` — practical-work schematics
- `laboratorijas_5.pdsprj` — lab 5

## CV bullet (short, EN)
> *9 AVR microcontroller C programs (Microchip Studio + Proteus), Oct–Dec 2025: from interrupt-driven timers to a complete DC-motor controller combining ADC, Timer2 Fast PWM, H-bridge state machine and LED bar graph.*

## CV bullet (short, LV)
> *9 AVR mikrokontrolera C programmas (Microchip Studio + Proteus), 10.–12. 2025: no pārtraukuma vadītiem taimeriem līdz pilnai DC motora vadībai, kas apvieno ADC, Timer2 Fast PWM, H-tilta stāvokļu mašīnu un LED bar graph.*
