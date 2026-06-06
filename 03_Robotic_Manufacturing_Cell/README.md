<div align="center">

[← back to portfolio](../README.md)

# 🏭 Project 03

[![Tech1](https://img.shields.io/badge/-MAB373-FF0000?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-Industrial_Layout-374151?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-Mass_Production-15803D?style=for-the-badge)](#)

</div>

---

# 03 — RTK 4.7: Robotic Manufacturing Cell Design

> Robotizēta tehnoloģiskā kompleksa izstrāde detaļas Nr. 4 automātiskai apstrādei
> End-to-end design of a robotic machining cell for mass production (180 000 pcs/year)

**Context** RTU course work · *MAB373 — Detaļu orientēšanas un padeves iekārtas* · RMCE01 · 3rd year · 2026
**Variant** 4.7 (Detail Nr. 4, steel C45)
**Production volume** 180 000 pcs/year (mass production)

---

## The brief

Design a complete robotic technological cell (RTK = *Robotizētais Tehnoloģiskais Komplekss*) to manufacture a shaft component automatically. Must cover:
- Full technological route
- Robot + CNC layout with reach circles and safety zones
- Workpiece feeding & orientation device sizing
- Cutting regimes per tool/operation
- Cycle and takt-time calculation
- Cyclogram syncing robot, both CNCs, magazine, separator, aux stations
- Safety, sensors, chip removal integration
- Variant comparison + selection

16 sections + 4 graphical sheets (A2, A3).

---

## The part — stepped shaft, steel C45

- Total length L = 100 mm
- Stage lengths L1=40, L2=32, L3=32, L4=20, L5=13 mm
- External Ø25 / M30 thread
- Internal axial bore Ø18 (left, 0.6·M30)
- Axial bore right Ø8×13 mm
- Cross-bore Ø5
- Chamfers 2×45° + 3×45°
- Ra 3.2 / runout 0.01 │ A

Steel C45 → carbide tooling + coolant. Geometry fits **CNC turn-mill centre** (turning + cross-bore via C-axis driven tool).

![Part drawing](images/rtk_part_hi-1.png)

*Fig. 1 — Detail Nr. 4.7 drawing*

---

## Technological route — turn-mill in 2 setups

![Operation sketches](images/rtk_ops_hi-1.png)

*Fig. 2 — Operation sketches: multi-pass turning + chamfering + threading*

**Setup A** (grip right): face left, drill Ø18, rough-turn Ø25 stages, finish to Ra 3.2, chamfer 2×45°
**Setup B** (grip left, reversed): face right, drill Ø8, drive cross-bore Ø5 (C-axis), cut M30 thread, chamfer 3×45°

Two **identical turn-mill centres (CNC-V1, CNC-V2)** run in parallel — one does Setup A while the other does Setup B on the previous part.

---

## Cell layout — 6.5 × 9.5 m, 13 positions

![RTK layout](images/rtk_layout_hi-1.png)

*Fig. 3 — Floor plan (1:30, A2): 13 positions, 6.5 × 9.5 m, robot Ø600 outer / Ø400 inner reach*

| # | Code | Element |
|---|---|---|
| 1 | DN | Safety fence |
| 2 | SM | Workpiece magazine |
| 3 | SR | Feeding slide |
| 4 | AT | Separator/singulator |
| 5 | R | Industrial robot |
| 6-7 | CNC-V1/V2 | Turn-mill centres |
| 8 | SK1/SK2 | Chip conveyors |
| 9 | AKS | Inspection station |
| 10 | M | Marking machine |
| 11 | GP | Finished-parts pallet |
| 12 | BK | Reject bin |
| 13 | PLC/HMI | Control cabinet |

Robot outer reach Ø600 covers both CNCs + inspection + magazine outlet — keeps cycle short. Inner Ø400 covers pallet + reject.

---

## Cyclogram — sync robot, CNCs, aux stations

![Cyclogram](images/rtk_cycle_hi-1.png)

*Fig. 4 — Layout with cyclogram overlay*

The cyclogram shows:
- CNCs run continuously (one machining, the other loaded)
- Robot waits for CNCs — cell is **CNC-bound**, not robot-bound
- Marking/inspection run in parallel with CNC machining — off critical path

Cycle time + takt computed for 180 000 pcs/yr.

---

## 16 sections of the course work

1. Initial data + part analysis
2. Production-type determination (180 000 pcs/yr → mass)
3. Workpiece selection (solid bar vs forging trade-off)
4. Technological route — operation sequence + setup choice
5. Basing + clamping with datum A reference
6. RTK equipment selection (robot + 2× turn-mill CNC + magazine + separator)
7. Workpiece feeding & orientation device — design + sizing
8. Tool selection (carbide for C45 + coolant)
9. **Cutting-regime calculation** — speeds, feeds, depths per pass
10. Auxiliary-time + takt-time
11. **RTK cyclogram**
12. Equipment layout (floor plan)
13. Automatic control, sensors, safety
14. Chip removal + cooling
15. RTK variant comparison + final selection
16. Conclusions

---

## Files in this folder

| File | Size | What |
|---|---:|---|
| `RTK_kursa_darbs_FULL.docx` | 36 KB | **Full course work** — 16 sections, ~7 300 words LV |
| `MAB373_pilna_versija.docx` | 49 KB | Alternative full version |
| `01_Detalas_rasejums.pdf` | 225 KB | Part drawing (A4, 1:1) |
| `02_Operaciju_skices.pdf` | 316 KB | Operation sketches |
| `03_RTK_planojums.pdf` | 379 KB | Cell layout (A2, 1:30) |
| `04_RTK_planojums_ar_ciklogrammu.pdf` | 380 KB | Layout + cyclogram |
| `images/` | — | Figures used in this README |

---

## How to read

1. Start with `01_Detalas_rasejums.pdf` — what part is being made
2. Read sections 1–6 of `RTK_kursa_darbs_FULL.docx` — engineering reasoning
3. Open `02_Operaciju_skices.pdf` — machining route
4. Open `03_RTK_planojums.pdf` — floor plan
5. `04_RTK_planojums_ar_ciklogrammu.pdf` — cyclogram proves throughput target

Deeper: section 9 (cutting regimes), section 11 (cyclogram sync), section 13 (safety/sensor approach).

---

## Skills demonstrated

- **Robotic cell design** — equipment selection, layout, reach analysis
- **CNC turn-mill route planning** — multi-setup, parallel-machine flow
- **Cutting-regime calculation** — speeds, feeds, depths for C45 + carbide
- **Cycle-time + takt analysis** for mass production
- **Industrial floor-plan layout** — scaled drawings, safety zones
- **Sensor/safety integration**
- **Workpiece feeding system sizing**
- **Technical drawing per ISO** — A2/A3/A4 sheets, title blocks, 1:30 / 1:1

---

## Latvian summary (LV)

Kursa darbs *MAB373 — Detaļu orientēšanas un padeves iekārtas* (variants 4.7) — pilns robotizētais tehnoloģiskais komplekss Detaļas Nr. 4 (Ø25/M30 vārpsta, C45) sērijveida ražošanai 180 000 gab./gadā.

6,5 × 9,5 m, 13 pozīcijas: robots, divi turn-mill CNC centri, magazīna, atdalītājs, skaidu konveijieri, kontroles stacija, marķēšanas iekārta, gatavo detaļu palete, brāķa kaste, PLC vadības skapis. Galvenais inženiertehniskais izaicinājums — sinhronizēt robotu, abus CNC un palīgstacijas vienā nepārtrauktā ciklā, ko apliecina ciklogramma uz A2 lapas.

Pilna 16 sadaļu dokumentācija failā `RTK_kursa_darbs_FULL.docx`. Grafiskās lapas — detaļas rasējums, operāciju skices, kompleksa plānojums, plānojums ar ciklogrammu.
