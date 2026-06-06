# 05 — Industrial Electronics Coursework Portfolio

> Praktiskie un laboratorijas darbi kursā *Rūpnieciskās elektroniskās iekārtas*
> Practical and laboratory works in *Industrial Electronic Equipment*

**Context:** RTU, Enerģētikas un elektrotehnikas fakultāte, RMCE01, 2. kurss, 2024/2025
**Group code:** 231RMC173

A bundled portfolio of 7 lab and practical works covering the foundations of industrial electronics — diodes, voltage regulation/stabilization, op-amp circuits, ADC/DAC converters, and sensor characterization. Each work combined hands-on lab measurements (oscilloscope, voltmeter, signal generator) with PSIM circuit simulation and analytical calculation cross-checks.

---

## EN — for GitHub README / EN CV

**Industrial Electronics Coursework — RTU FEEF, 2024/2025**

Practical and laboratory works covering analog/power electronics fundamentals; relevance directly maps to my current role as Electronics Adjuster at Latvijas Finieris.

**Diodes — rectification and unregulated supplies (Lab #1 + Practical)**
- Compared p-n vs Schottky diode characteristics in rectification
- Single-phase rectifiers (half-wave, full-wave bridge); ripple analysis with and without filter capacitor
- PSIM simulation + bench measurement cross-validation

**Diodes — voltage multiplication and stabilization (Lab)**
- Voltage-doubler circuit: measured u_in_amp = 20.25 V → u_out = 40.5 V (matches theoretical 2× peak)
- Zener-diode voltage stabilizer characterization

**Voltage regulators (Practical, with thyristor)**
- Single-phase half-wave controlled rectifier with thyristor, control angle α = 0…180°
- Captured u₁, u₂ and control-voltage u_vad waveforms in PSIM at α = 90°
- Resistive-load behavior across regulation range

**Linear compensation-type voltage stabilizers (Lab #3)**
- Built bench circuit, regulated U_out = 10 V from U_in = 15 V via potentiometer R2
- Stabilization coefficient and output-impedance characterization

**Amplifiers, ADC, DAC (Practical #3)**
- Inverting op-amp configurations (V_s = ±5 V, K_v = 100 000)
- Gain measurement at R2 = 10 kΩ and 100 kΩ, DC and 1 kHz sinusoidal inputs
- PSIM simulation vs classical formula cross-check; A = R2/R1
- ADC/DAC converter characterization

**Sensor characterization (Lab #5)**
- Resistive potentiometric sensors for linear displacement: static transfer curve U_out = f(X), loaded vs unloaded (R_sl = 4.7 kΩ)
- Sensor non-linearity quantified under loading

**Skills demonstrated:** analog electronics · power electronics (thyristors, controlled rectifiers) · op-amp circuit analysis · ADC/DAC fundamentals · sensor characterization · PSIM simulation · bench measurement (oscilloscope, multimeter) · simulation-vs-measurement validation

---

## LV — for LV CV

**Rūpnieciskās elektronikas studiju darbu portfolio (RTU EEF, 2024/2025)**

7 praktiskie un laboratorijas darbi, kas aptver rūpnieciskās elektronikas pamatus — diodes, sprieguma stabilizācija/regulēšana, operacionālie pastiprinātāji, ACP/CAP pārveidotāji un sensoru izpēte. Katrs darbs apvieno PSIM modelēšanu, analītiskos aprēķinus un stenda mērījumus.

**Tēmu pārskats**
- Diožu lietojumi taisngriešanai (p-n vs Šotki diodes; vienfāzes pusperiods/tilta taisngrieži)
- Diožu lietojumi sprieguma daudzkāršošanai un stabilizācijai (divkāršotājs; Zenera stabilizators)
- Vienfāzes vadāmais taisngriezis ar tiristoru (regulēšanas leņķis 0–180°)
- Lineārie kompensācijas tipa sprieguma stabilizatori
- Operacionālie pastiprinātāji, ACP/CAP pārveidotāji (invertējošais slēgums, sinusoidāls maiņspriegums)
- Rezistīvie potenciometriskie pārvietojuma sensori (statiskās raksturlīknes)

**Prasmes:** analogā un jaudas elektronika · tiristori un vadāmie taisngrieži · operacionālie pastiprinātāji · ACP/CAP pamati · sensoru raksturošana · PSIM modelēšana · stenda mērījumi (osciloskops, multimetrs) · modelēšanas un eksperimenta salīdzināšana

**Saistība ar darbu Latvijas Finierī:** šis kurss veido tiešu zināšanu bāzi pašreizējam darbam *Elektronikas regulētājs* — taisngriežu, stabilizatoru un sensoru izpratne ir tieši pielietojama rūpnieciskās elektronikas tehnikas regulēšanai.

---

## Files in this folder
- `Lab1_Diozu_lietojumi_taisngriesanai.pdf` — Lab #1: Diode rectification
- `Praktiskais_Diozu_taisngriesana.docx` — Practical on diode rectification
- `Lab2_Diozu_daudzkarsosana_stabilizacija.pdf` — Lab #2: Voltage multiplication & stabilization
- `Lab3_Linearie_kompensacijas_stabilizatori.pdf` — Lab #3: Linear compensation stabilizers
- `Praktiskais_Spriegumu_regulatori.pdf` — Practical: Voltage regulators (thyristor)
- `Praktiskais3_Pastiprinataji_ADC_DAC.pdf` — Practical #3: Op-amps, ADC, DAC
- `Lab5_Sensoru_izpete.pdf` — Lab #5: Sensors
- `psim_sources/*.psimsch` — PSIM source files for all simulations (editable circuits)

## CV bullet (short, EN)
> *Completed industrial electronics coursework (RTU FEEF) covering diode rectifiers, thyristor-controlled regulators, linear voltage stabilizers, op-amp circuits, ADC/DAC and resistive sensors — combining PSIM simulation with bench measurement validation.*

## CV bullet (short, LV)
> *Pabeigti rūpnieciskās elektronikas studiju darbi (RTU EEF): diožu taisngrieži, tiristoru regulatori, lineārie stabilizatori, operacionālie pastiprinātāji, ACP/CAP un rezistīvie sensori — apvienojot PSIM modelēšanu ar stenda mērījumiem.*
