<div align="center">

[← back to portfolio](../README.md)

# 🏁 Project 11

[![Tech1](https://img.shields.io/badge/-EPLAN-005CA9?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-Festo-0091D5?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-Pneumatics-374151?style=for-the-badge)](#)

</div>

---

# 11 — FESTO MPS Station: Repair, EPLAN Schematics & Documentation 🏁

> Reālas Festo MPS izglītības stacijas remonts, diagnostika un pilnas tehniskās dokumentācijas izveide
> Real-equipment maintenance project — restoring a non-working FESTO MPS station and producing full schematics

**Context** RTU's FESTO MPS station — needed repair and was undocumented
**Role** Co-authored the repair and the technical documentation handbook; drafted electrical schematics in EPLAN
**Team** Daniel + Denis Kashin (PLC subsystem co-prepared)
**Tools** EPLAN Education 2026 · Festo Automation Suite · CODESYS · SIMATIC Manager · pneumatic/electrical analysis

---

## Why this is the flagship project

This is the project that maps **closest to real industrial work** — and most closely mirrors my role as Industrial Electronics Technician (*Elektronikas regulētājs*) at Latvijas Finieris. Unlike the simulation-based projects (RobotStudio, FluidSIM, Proteus), this one involved:

- A **real broken physical machine** in the RTU lab
- A **real diagnosis** — finding what was wrong without existing schematics to reference
- **Real EPLAN schematic drafting** — drawing what was there from scratch
- **Real handoff documentation** — writing the maintenance handbook the next student/technician will use
- **Real team collaboration** with another student on the PLC subsystem

Every other project in this portfolio is something I designed and simulated. This is the one where I **restored a real machine to service** and **produced the documentation that didn't exist**.

---

## The system — FESTO MPS Modular Production System

![FESTO MPS station overview](images/11_festo_station_real.png)

*Fig. 1 — The actual rebuilt FESTO MPS station (cover photo from the handbook). Four-zone training cell: loading → processing → pickup head with vacuum gripper → unloading.*

The MPS station has **four working zones**, each with its own actuators, sensors and pneumatic supply.

### Zone 1 — Loading

| ID | Component | Model | Function |
|---|---|---|---|
| 1I01 | Inductive sensor "PART IN" | SIE-M12S-RS-S-L (PNP, 10–30 VDC) | Detects part arrival |
| 1R01 | Pneumatic rotary drive | Festo DSR-25-180-P (Series 0788) | Workpiece orientation/transfer |
| 1I02 | Position sensors (×2) on rotary | SIE-M8x1-PS-K / SIE-M12x1-PS-K-LED | End-of-travel detection |
| 1M01 | Conveyor motor | M1 (24 VDC) | Transports parts to processing |
| 1OP01 | Optical sensor — parts-on-line | — | Boundary / fullness monitor |

### Zone 2 — Processing

The processing zone has the **F module** (tool feed) and the **H module** (cross-transmission). Both use pneumatic cylinders with magnetic reed switches (Festo SMT-8-K-LED) sensing end positions on both extend and retract, plus cross-stroke for H. Controlled via `2V01` / `2V02` directional valves and `2G01` GRLA flow regulators.

### Zone 3 — Pickup head with vacuum gripper

| ID | Component | Model | Function |
|---|---|---|---|
| 3Q01 | Vacuum block | Festo 151270, VAL-1/8-10 | Vacuum gripping |
| 3C01 | Lift-axis cylinder | Festo DSNU/DNC series | Gripper head lift |
| 3S01 | Magnetic stroke sensors | SMT-8-K-LED | End-of-travel detection |
| 3V01 | Lift solenoid valve | Festo VUVG-L10-P53C-T-M5-1P3 | Cylinder direction control |
| 3R01 | Intermediate rotary drive | Festo DSR-25-180-P | Part reorientation |
| 3S02 | Rotary limit switches | BURGESS U33 | Hard-stop detection |

### Zone 4 — Unloading
Documented in same format as Zones 1–3.

---

## The tagging convention — methodology contribution

I designed a structured tagging convention applied throughout:

**Format:** `[Zone][Class][Number]`

- **Zone** — 1, 2, 3, or 4
- **Class** — letter encoding component type:
  - `I` — inductive sensor · `OP` — optical · `S` — magnetic/limit switches
  - `C` — cylinder · `R` — rotary drive · `V` — valve · `G` — flow regulator
  - `M` — motor · `Q` — vacuum block · `T` — MiniTool actuator
- **Number** — running serial within zone+class

**Example:** `2P3.1` = Zone 2, magnetic Position sensor, set 3 channel 1 — unambiguous and instantly traceable.

---

## The deliverables

### 1. EPLAN electrical wiring

![Festo electrical wiring](images/festo_wiring_main-01.png)

*Fig. 2 — Main electrical wiring (EPLAN Education 2026): 24 V power + sensor / actuator I/O for all four zones, drawn from scratch.*

### 2. Four pneumatic schematics — one per zone

![Pneumatic 1](images/festo_pneu1-1.png)
*Fig. 3 — Sheet 1: zone 1 (loading)*

![Pneumatic 2](images/festo_pneu2-1.png)
*Fig. 4 — Sheet 2: zone 2 (processing) — F and H modules*

![Pneumatic 3](images/festo_pneu3-1.png)
*Fig. 5 — Sheet 3: zone 3 (pickup head)*

![Pneumatic 4](images/festo_pneu4-1.png)
*Fig. 6 — Sheet 4: zone 4 (unloading)*

### 3. PLC wiring diagrams

![PLC main](images/festo_plc_main-1.png)
*Fig. 7 — Main PLC wiring diagram*

![PLC subsystem](images/festo_plc_denis-1.png)
*Fig. 8 — PLC subsystem co-prepared with Denis Kashin*

### 4. Technical documentation handbook (~2 600 words, LV)

The `FESTO_MPS_full_documentation.docx` is the **handbook** future technicians use. Structure:
1. Zone legend + class legend + tagging convention
2. Per-zone component tables (ID, name, model, type, supply, function)
3. PLC I/O map (sensor → input pin / valve → output pin)
4. Pneumatic map (valve → actuator routing)
5. **Alarm / diagnostic list** ("Nelaimes gadījumi un diagnostika") — failure modes + recovery
6. Cycle sequence logic between zones

---

## Files in this folder

| File / folder | What's inside |
|---|---|
| `FESTO_MPS_full_documentation.docx` | The handbook — ~2 600 words LV |
| `pneumatic_schemes/Pnevmo_1.pdf` … `Pnevmo_4.pdf` | Four pneumatic sheets |
| `electrical_PLC/Festo_electrical_wiring.pdf` | Main electrical (EPLAN) |
| `electrical_PLC/PLC_main.pdf` | Main PLC schematic |
| `electrical_PLC/PLC_for_Denis_Kashin.pdf` | PLC subsystem (Denis) |
| `electrical_PLC/1OP1_4OP1_for_Denis_Kashin.pdf` | Sensor sub-doc |
| `images/` | Figures used in this README |

---

## Skills demonstrated

- **Industrial equipment service** — diagnosis and repair of a real production-style training station
- **Pneumatic system analysis** — valves, manifolds, actuators across 4 zones
- **EPLAN documentation** — electrical / PLC wiring drawn from scratch
- **Festo component identification** — DSR, DSNU/DNC, VUVG, VAL, GRLA series
- **Sensor types** — inductive PNP, optical, magnetic reed, limit switches
- **Structured tagging convention** for plant equipment
- **Failure-mode analysis and alarm-table authoring**
- **Cross-discipline team collaboration** with Denis Kashin
- **Technical writing in Latvian**

---

## Latvian summary (LV)

Šis ir flagship projekts — reālas Festo MPS izglītības stacijas remonts un pilna tehniskās dokumentācijas izveide RTU. Stacija aptver 4 zonas ar pilnu Festo standarta komponentu sortimentu — DSR rotācijas piedziņas, DSNU/DNC cilindri, VUVG solenoīda vārsti, VAL vakuuma bloki, GRLA droseļvārsti.

Galvenais metodoloģiskais ieguldījums — pielāgota marķēšanas sistēma `[Zona][Klase][Nē]` (piem. `2P3.1` = Zona 2, magnētiskais pozīcijas sensors, komplekts 3 kanāls 1). Pilna EPLAN dokumentācija, četras pneimatiskās shēmas, PLC vadu shēmas un ~2 600 vārdu rokasgrāmata ar zonu/klases leģendām, PLC I/O karti, pneimatikas karti, trauksmes sarakstu un cikla loģiku.

Šis projekts ir tuvākais analogs reālajai industriālā aprīkojuma apkalpošanai — un tieši atbilst manai pašreizējai *Elektronikas regulētāja* darba lomai Latvijas Finierī.
