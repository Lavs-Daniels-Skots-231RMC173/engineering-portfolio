<div align="center">

[← back to portfolio](../README.md)

# 💡 Project 05

[![Tech1](https://img.shields.io/badge/-PSIM-512BD4?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-Analog_Electronics-374151?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-Bench_Measurement-15803D?style=for-the-badge)](#)

</div>

---

# 05 — Industrial Electronics Coursework — 7 Lab & Practical Works

> Praktiskie un laboratorijas darbi kursā *Rūpnieciskās elektroniskās iekārtas*
> Lab and practical works covering analog & power electronics foundations

**Context** RTU · Enerģētikas un elektrotehnikas fakultāte (Faculty of Power & Electrical Engineering) · RMCE01 · 2nd year · 2024/2025
**Course** Rūpnieciskās elektroniskās iekārtas (Industrial Electronic Equipment)
**Tools** PSIM (circuit simulation) + bench measurement (oscilloscope, multimeter, signal generator)

---

## Why this matters for the portfolio

This coursework forms the **direct intellectual basis** for my current job role of *Electronics Adjuster (Elektronikas regulētājs)* at Latvijas Finieris. The course taught me to read, simulate, measure and tune rectifiers, voltage stabilizers, voltage regulators with thyristors, op-amp circuits, ADC/DAC converters and sensors — all of which are the building blocks of the industrial electronic equipment I now adjust on the factory floor.

Each lab combined three steps:
1. **Analytical calculation** of the expected behavior from theory
2. **PSIM circuit simulation** to verify the analytical prediction
3. **Bench measurement** on a physical circuit (oscilloscope + voltmeter)

The cross-check between these three is what makes the engineering value — not any single one in isolation.

---

## The 7 works in this folder

### Topic 1 — Diode rectification (Lab #1 + Practical)
- Comparison of **p-n junction diodes vs Schottky diodes** in rectification
- **Single-phase half-wave** and **full-wave bridge** rectifier behavior
- Ripple analysis with and without filter capacitor
- PSIM model vs bench measurement cross-validation

### Topic 2 — Diode voltage multiplication & stabilization (Lab #2)
- **Voltage doubler** circuit: applied AC with u_in_amp = 20.25 V, measured DC output u_out = 40.5 V — matches the theoretical 2× peak doubler equation
- **Zener-diode voltage stabilizer** characterization (load line, regulation factor)

### Topic 3 — Thyristor-controlled voltage regulator (Practical: Spriegumu regulatori)
![Thyristor regulator](images/elec_thyristor-02.png)
*Fig. 1 — Single-phase half-wave controlled rectifier (PSIM): u₁ input voltage, u₂ load voltage, u_vad gate-control voltage at firing angle α = 90°. Behavior shown across the full α = 0…180° range.*

Single-phase **half-wave controlled rectifier** with resistive load Rsl = 10 Ω, firing angle α swept 0…180°. PSIM oscillograms of input/output/control + load behavior across the regulation range.

### Topic 4 — Linear compensation voltage stabilizer (Lab #3)
Built the bench circuit, applied input U_in = 15 V, regulated output U_out = 10 V via potentiometer R2. Characterized:
- Stabilization coefficient
- Output impedance
- Load regulation

### Topic 5 — Op-amps, ADC, DAC (Practical #3)
![Op-amp](images/elec_opamp-03.png)
*Fig. 2 — Inverting op-amp configuration in PSIM: V_s = ±5 V, differential gain K_v = 100000. Verified gain calculation A = R2/R1 for R2 = 10 kΩ and 100 kΩ, both with DC input 0.01 V and 1 kHz sinusoidal input — analytical, PSIM and bench all agree.*

- Classical **inverting op-amp** with V_s = ±5 V, K_v = 100000
- Verified gain A = R2/R1 for R2 = 10 kΩ → A = -10 and R2 = 100 kΩ → A = -100
- Both DC behavior and 1 kHz sinusoidal (Uin_amp = 0.01 V → Uout_amp = 100 mV / 1 V)
- ADC and DAC converter characterization

### Topic 6 — Voltage doubler (Lab #2 second part)
![Voltage doubler](images/elec_doubler-2.png)
*Fig. 3 — Voltage-doubler bench measurement: u_in_amp = 20.25 V (yellow trace), u_out_DC = 40.5 V (cyan trace) on the load. The 2× ratio confirms the doubler topology is working as designed.*

### Topic 7 — Resistive potentiometric sensors (Lab #5)
![Sensor characterization](images/elec_sensor-02.png)
*Fig. 4 — Static transfer curve U_out = f(X) of a linear-displacement potentiometric sensor. Top curve = voltmeter-only loading; bottom curve = with R_sl = 4.7 kΩ shunt. The loading effect linearizes the curve at low X but adds a substantial error at full deflection — quantified for the design.*

Resistive potentiometric sensor for linear-displacement measurement. Captured **static transfer curve** U_out = f(X) in two conditions:
- Unloaded (high-impedance voltmeter only)
- Loaded (with R_sl = 4.7 kΩ shunt)

Quantified the sensor non-linearity under loading — a real-world issue when interfacing potentiometric sensors to ADCs with finite input impedance.

---

## Files in this folder

### Reports / labs
| File | Topic | Format |
|---|---|---|
| `Lab1_Diozu_lietojumi_taisngriesanai.pdf` | Lab #1: Diodes — rectification, p-n vs Schottky | PDF, 2.5 MB |
| `Praktiskais_Diozu_taisngriesana.docx` | Practical: Diode rectification | Word, 1.2 MB |
| `Lab2_Diozu_daudzkarsosana_stabilizacija.pdf` | Lab #2: Voltage multiplication & stabilization | PDF, 812 KB |
| `Lab3_Linearie_kompensacijas_stabilizatori.pdf` | Lab #3: Linear compensation stabilizers | PDF, 688 KB |
| `Praktiskais_Spriegumu_regulatori.pdf` | Practical: Voltage regulators (thyristor) | PDF, 1.0 MB |
| `Praktiskais3_Pastiprinataji_ADC_DAC.pdf` | Practical #3: Op-amps, ADC, DAC | PDF, 453 KB |
| `Lab5_Sensoru_izpete.pdf` | Lab #5: Sensors | PDF, 1.9 MB |

### Source files
| Folder | What's inside |
|---|---|
| `psim_sources/` | **Editable PSIM circuit files** (`.psimsch`) for all simulations — open and modify in PSIM 2025 or newer |