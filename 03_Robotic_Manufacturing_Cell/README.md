# 03 — RTK 4.7: Robotic Manufacturing Cell Design

> Robotizēta tehnoloģiskā kompleksa izstrāde detaļas Nr. 4 automātiskai apstrādei
> End-to-end design of a robotic machining cell for mass production (180 000 pcs/year)

**Context** RTU course work · *MAB373 — Detaļu orientēšanas un padeves iekārtas* (Part Orientation & Feeding Devices) · RMCE01 · 3rd year · 2026
**Variant** 4.7 (Detail Nr. 4, steel C45)
**Production volume** N = 180 000 pcs/year (mass production)

---

## The brief

Design a complete robotic technological cell (RTK = *Robotizētais Tehnoloģiskais Komplekss*) to manufacture a specified shaft component automatically. The design must cover:

- The full **technological route** from blank stock to finished part
- **Robot + CNC layout** with reach circles and safety zones
- **Workpiece feeding & orientation device** sized to keep the cell fed
- **Cutting regimes** computed per tool/operation
- **Cycle and takt-time** calculation
- **Cyclogram** synchronizing robot, both CNCs, magazine, separator and aux stations
- **Safety, sensors and chip removal** integration
- Comparison of design variants and selection

The work is documented across 16 sections + 4 graphical sheets (A2, A3 formats).

---

## The part — stepped shaft, steel C45

A stepped rotational-symmetry shaft with the following features:
- **Total length** L = 100 mm
- **Stage lengths** L1 = 40, L2 = 32, L3 = 32, L4 = 20, L5 = 13 mm
- **External diameter** Ø25 (cylindrical base/seat)
- **External thread** M30
- **Internal axial bore** Ø18 (left side, 0.6·M30)
- **Axial bore right** Ø8 × 13 mm
- **Cross-bore** Ø5
- **Chamfers** 2×45° and 3×45°
- **Surface roughness** Ra 3.2
- **Tolerance** 0.01 mm to datum A
- **Material** Steel C45 — carbide tooling required, with coolant supply

The geometry is well-suited to a **CNC turn-mill centre** (turning + cross-bore via C-axis driven tool) — no separate milling station needed.

![Part drawing](images/rtk_part_hi-1.png)

*Fig. 1 — Detail Nr. 4.7 part drawing: Ø25 / M30 stepped shaft, steel C45, Ra 3.2, runout 0.01 │ A, total length 100 mm*

---

## Technological route — turn-mill machining sequence

The part is machined on a **CNC turn-mill centre** in two setups:

![Operation sketches](images/rtk_ops_hi-1.png)

*Fig. 2 — Operation sketches: each multi-pass turning + chamfering + thread cutting operation*

Operations:
1. **Setup A** (gripping right end)
   - Face the left end + drill Ø18 axial bore
   - Rough-turn the Ø25 cylindrical stages
   - Finish-turn to Ra 3.2
   - Chamfer 2×45° (left transitions)
2. **Setup B** (gripping left, reversed)
   - Face the right end + drill Ø8 axial bore
   - Drive cross-bore Ø5 (C-axis + driven tool)
   - Cut M30 thread
   - Chamfer 3×45° (right transitions)

Two **identical turn-mill centres (CNC-V1, CNC-V2)** are used in parallel — one does Setup A while the other does Setup B on the previous part, giving a continuous flow.

---

## Cell layout — 6.5 × 9.5 m, 13 positions

![RTK layout](images/rtk_layout_hi-1.png)

*Fig. 3 — RTK cell floor plan (scale 1:30, A2 sheet): 13 numbered positions, 6.5 × 9.5 m footprint, robot Ø600 inner / Ø400 outer reach circles*

| # | Code | Element | Role |
|---|---|---|---|
| 1 | DN | Drošības nožogojums | Safety fence (perimeter) |
| 2 | SM | Sagatavju magazīna | Workpiece magazine |
| 3 | SR | Slīdes rene 30 | Feeding slide |
| 4 | AT | Atdalītājs / padevējs | Singulator/separator |
| 5 | R | Robots | Industrial robot |
| 6 | CNC-V1 | Turn-mill centre | First CNC |
| 7 | CNC-V2 | Turn-mill centre | Second CNC |
| 8 | SK1/SK2 | Skaidu konveijieri | Chip conveyors |
| 9 | AKS | Kontroles stacija | Inspection station |
| 10 | M | Marķēšanas iekārta | Marking machine |
| 11 | GP | Gatavo detaļu palete | Finished-parts pallet |
| 12 | BK | Brāķa kaste | Reject bin |
| 13 | PLC/HMI | Vadības skapis | Control cabinet |

The robot reach is laid out so its **outer reach circle (Ø600)** covers both CNCs, the inspection station and the magazine outlet — keeping cycle time short. Inner reach circle (Ø400) covers the pallet and reject zone.

---

## Cyclogram — keeping robot, CNCs and aux stations in sync

![RTK layout with cyclogram](images/rtk_cycle_hi-1.png)

*Fig. 4 — Same layout with the cyclogram overlay: a time-synchronised chart showing what robot, CNC-V1, CNC-V2, magazine, separator, inspection and marking are doing across one full production cycle*

The cyclogram is the design's heart: it shows that:
- CNCs run continuously (one machining while the other is being loaded)
- The robot's cycle is dominated by *waiting* for the CNCs (machining time > robot transfer time) — confirming the cell is **CNC-bound**, not robot-bound
- The marking and inspection stations operate in parallel with CNC machining, off the critical path

Cycle time and takt are computed from the cyclogram for the target 180 000 pcs/year throughput.

---

## Engineering scope — 16 sections of the course work

The full course work (~7 300 words, in `RTK_kursa_darbs_FULL.docx`) covers:

1. Initial data & constructive/technological analysis of the part
2. Production-type determination (180 000 pcs/yr → mass production)
3. Workpiece (sagatave) selection — solid bar vs forging trade-off
4. Technological route — operation sequence + setup choice
5. Basing and clamping strategy with datum A as reference
6. RTK equipment selection (robot model, 2× turn-mill CNC, magazine, separator)
7. **Workpiece feeding & orientation device design and sizing calculation**
8. Tool selection (carbide inserts for C45, coolant supply)
9. **Cutting-regime calculation** — speeds, feeds, depths per pass per operation
10. Auxiliary-time and RTK takt-time calculation
11. **RTK cyclogram** — full time-sync chart (see Fig. 4)
12. Equipment layout — the floor plan (see Fig. 3)
13. Automatic control, sensors and safety system
14. Chip removal system + cooling supply
15. RTK variant comparison (this 2-CNC vs single-CNC alternatives) and final selection
16. Final conclusions

---

## Files in this folder

| File | Size | What's inside | How to view |
|---|---:|---|---|
| `RTK_kursa_darbs_FULL.docx` | 36 KB | **Full course work** — 16 sections, ~7 300 words, LV. All tables (part stages, cutting regimes, equipment list, sensor list), calculations and conclusions. The primary reference document. | Microsoft Word, LibreOffice, Google Docs |
| `MAB373_pilna_versija.docx` | 49 KB | Alternative full version with additional formatting | Word/LibreOffice |
| `01_Detalas_rasejums.pdf` | 225 KB | **Part drawing** — A4, scale 1:1, Detail Nr. 4.7 with all dimensions, tolerances, chamfers, surface finish | PDF viewer |
| `02_Operaciju_skices.pdf` | 316 KB | **Operation sketches** — A4, multi-pass turning, chamfering, threading operations | PDF viewer |
| `03_RTK_planojums.pdf` | 379 KB | **Cell layout** — A2 sheet at scale 1:30, all 13 numbered positions, dimensions, robot reach circles, safety perimeter | PDF viewer |
| `04_RTK_planojums_ar_ciklogrammu.pdf` | 380 KB | **Layout with cyclogram** — same layout sheet with the time-synchronisation chart overlay | PDF viewer |
| `images/` | — | Extracted figures used in this README | — |

---

## How to read the package

For a recruiter or technical reviewer:

1. Start with `01_Detalas_rasejums.pdf` — understand what part is being made
2. Read sections 1–6 of `RTK_kursa_darbs_FULL.docx` — the engineering reasoning
3. Look at `02_Operaciju_skices.pdf` to follow the machining route
4. Open `03_RTK_planojums.pdf` to see the floor plan
5. The cyclogram in `04_RTK_planojums_ar_ciklogrammu.pdf` is where the design pays off — it visually proves the cell hits its throughput target

For a deeper read: section 9 (cutting regimes) shows the per-operation calculations; section 11 (cyclogram) shows the synchronization logic; section 13 covers the safety/sensor approach.

---

## Skills demonstrated

- **Robotic cell design** — equipment selection, layout planning, reach analysis
- **CNC turn-mill technological-route planning** — multi-setup routing, parallel-machine flow
- **Cutting-regime calculation** — speeds, feeds, depths per material (C45 carbide)
- **Cycle-time and takt analysis** for mass production
- **Industrial floor-plan layout** — scaled drawings, dimensioning, safety zones
- **Sensor / safety integration**
- **Workpiece feeding system sizing**
- **Technical drawing per ISO conventions** — A2/A3/A4 sheets, title blocks, scale 1:30 / 1:1

---

## Latvian summary (LV)

Šis ir kursa darbs *MAB373 — Detaļu orientēšanas un padeves iekārtas* (variants 4.7), kurā izstrādāts pilns robotizētais tehnoloģiskais komplekss (RTK) Detaļas Nr. 4 (Ø25/M30 vārpsta no tērauda C45) sērijveida ražošanai — 180 000 gab./gadā.

Komplekss aptver 6,5 × 9,5 m un satur 13 pozīcijas: robotu, divus turn-mill CNC centrus, magazīnu, atdalītāju, skaidu konveijierus, kontroles staciju, marķēšanas iekārtu, gatavo detaļu paleti, brāķa kasti un PLC vadības skapi. Galvenais inženiertehniskais izaicinājums — sinhronizēt robotu, abus CNC un palīgstacijas vienā nepārtrauktā ciklā, ko apliecina ciklogramma uz lapas A2.

Pilna 16 sadaļu kursa dokumentācija failā `RTK_kursa_darbs_FULL.docx`, grafiskās daļas — detaļas rasējums, operāciju skices, kompleksa plānojums un plānojums ar ciklogrammu — atsevišķās PDF lapās.
