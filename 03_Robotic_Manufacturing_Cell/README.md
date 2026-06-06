# 03 — Robotic Manufacturing Cell (RTK, Variant 4.7)

> Robotizētais Tehnoloģiskais Komplekss — pilna ražošanas ciklu projektēšana
> Robotic Technological Complex — full machining-cell design

**Context:** RTU studiju projekts, kurs *MAB373 — Detaļu orientēšanas un padeves iekārtas*, RMCE01, 3. kurss, 2026
**Variant:** 4.7 (Detal Nr. 4, Tērauds C45)
**Annual production volume:** N = 180 000 pcs/year (mass production)

---

## EN — for GitHub README / EN CV

**RTK — Robotic Manufacturing Cell, Variant 4.7 (2026)**

End-to-end design of a robotic machining cell to produce a stepped shaft component (steel C45) in mass production (180 000 pcs/year). The course work covers the full engineering chain — from part analysis to cell commissioning logic — across 16 documented sections plus 4 graphical sheets.

**Part designed for production**
- Stepped shaft, L = 100 mm; stages L1…L5 = 40/32/32/20/13 mm
- Outer Ø25, M30 external thread, Ø18 internal axial bore, Ø8×13 right-side axial bore, Ø5 transverse hole
- 2×45° and 3×45° chamfers, Ra 3.2, 0.01 mm tolerance against datum A

**Engineering scope (full course work, 16 sections)**
1. Initial data & constructive/technological analysis of the part
2. Production-type determination (mass production from N = 180 000 pcs/yr)
3. Workpiece (sagatave) selection
4. Technological route — turn-mill machining sequence
5. Basing and clamping strategy (datum A reference)
6. RTK equipment selection (robot + 2× turn-mill CNC, magazine, separator)
7. Workpiece feeding & orientation device — design and sizing calculation
8. Tools and machining operation selection (carbide for C45, with coolant)
9. **Cutting-regime calculation** — speeds, feeds, depths per pass
10. Auxiliary-time and RTK takt-time calculation
11. **RTK cyclogram** — time-synchronized chart of robot/CNC/auxiliary cycles
12. Equipment layout — 6500 × 9500 mm floor plan, 13 positions:
    - Safety fence (DN), parts magazine (SM), slide rail (SR-30), separator/feeder (AT)
    - Industrial robot (R) — Ø600 / Ø400 reach circles laid out
    - Two turn-mill CNC centers (CNC-V1, CNC-V2)
    - Chip conveyors (SK1/SK2), inspection station (AKS), marking machine (M)
    - Finished-parts pallet (GP), reject bin (BK), PLC/HMI control cabinet
13. **Automatic control, sensors and safety**
14. Chip removal and cooling system
15. RTK variant comparison and final selection
16. Conclusions

**Graphical deliverables**
- Part drawing (Detal Nr. 4.7, scale 1:1)
- Operation sketches with all `Pāreja` (pass) layouts
- RTK floor plan (scale 1:30, A2)
- Plan with cyclogram

**Skills demonstrated:** robotic cell design · CNC turn-mill technological-route planning · cutting-regime calculation · cycle-time and takt analysis for mass production · industrial floor-plan layout · sensor / safety integration · workpiece feeding system sizing · technical drawing per ISO conventions

---

## LV — for LV CV

**RTK — Robotizētais Tehnoloģiskais Komplekss, 4.7. variants (2026)**

Izstrādāts pilns robotizēts apstrādes komplekss Ø30 vārpstas detaļas ar M30 vītni ražošanai (Tērauds C45). Projekts aptver visu inženiertehnisko ķēdi: detaļas rasējums → operāciju secība → kompleksa plānojums → cikla sinhronizācija.

**Apjoms**
- **Detaļas rasējums** — Ø30/Ø25/Ø18, vītne M30, fāzes 2×45° / 3×45°, Ra 3,2, sišana 0,01 mm pret bāzi A, garums 100 mm.
- **Operāciju skices** — virpošanas pārejas katram diametra posmam, fāzēšana, vītnes griešana.
- **RTK plānojums (M 1:30)** — 6500 × 9500 mm grīdas plāns ar 13 numurētām pozīcijām: drošības nožogojums, sagatavju magazīna, slīdes rene, atdalītājs/padevējs, rūpnieciskais robots (ar Ø600/Ø400 darba zonām), divi turn-mill CNC centri, skaidu konveijeri, kontroles stacija, marķēšanas iekārta, gatavo detaļu palete, brāķa kaste, PLC/HMI vadības skapis.
- **Ciklogramma** — robota, CNC centru un palīgstaciju sinhronizācija.

**Prasmes:** robotizētu šūnu projektēšana · CNC turn-mill operāciju plānošana · ražošanas grīdas plānojums · cikla laika analīze · drošības zonu plānošana · tehniskie rasējumi

---

## Files in this project folder
**Course work report (16-section technical document, ~7 300 words):**
- `RTK_kursa_darbs_FULL.docx` — full course work
- `MAB373_pilna_versija.docx` — alternate version

**Graphical sheets:**
- `01_Detalas_rasejums.pdf` — part drawing (Detal Nr. 4.7, steel C45, scale 1:1)
- `02_Operaciju_skices.pdf` — operation sketches (turning, chamfering, threading passes)
- `03_RTK_planojums.pdf` — cell layout (scale 1:30, A2)
- `04_RTK_planojums_ar_ciklogrammu.pdf` — layout + cyclogram

## CV bullet (short, EN)
> *Designed a robotic machining cell (RTK, 6.5 × 9.5 m, 13-position layout) for mass production of an M30 stepped shaft in C45 steel — 180 000 pcs/year — including technological route, cutting-regime calculation, takt-time analysis, cyclogram and safety/sensor integration (RTU MAB373 course work).*

## CV bullet (short, LV)
> *Izstrādāts robotizētais apstrādes komplekss (RTK, 6,5 × 9,5 m, 13 pozīciju plānojums) M30 vārpstveida detaļas (C45 tērauds) sērijveida ražošanai — 180 000 gab./gadā — ar tehnoloģiskā maršruta, griešanas režīmu un takta laika aprēķiniem, ciklogrammu un sensoru/drošības integrāciju (RTU MAB373 kursa darbs).*
