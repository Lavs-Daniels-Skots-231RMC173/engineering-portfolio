# 01 — WPL_Station

> Trīs robotu metināšanas un paletizēšanas līnija ABB RobotStudio vidē
> Three-robot welding & palletizing line in ABB RobotStudio

**Context:** RTU studiju projekts, RMCE01, 3. kurss, 2026
**Supervisor:** Artjoms Supoņenkovs
**Tooling:** ABB RobotStudio 2023, RAPID

---

## EN — for GitHub README / EN CV

**WPL_Station — Three-robot welding & palletizing line (ABB RobotStudio 2026)**

Designed and simulated a fully automated production cell with three cooperating ABB robots — IRB 2600 (feeder), IRB 1660ID (welder), IRB 460 (palletizer) — running on three independent virtual controllers. The line processes 12 parts per cycle (4 tall → pallet A, 8 short → pallet B), with automatic part-type detection by height sensors and adaptive trajectory selection.

**Technical scope**
- 5 RAPID modules across 3 controllers, 20+ procedures, custom FUNCs (`fCalcWeldAngle`, `fIsWelderBusy`)
- 8 Smart Components (conveyor logic, vacuum/magnet grippers, weld visualization, pallet counters, light stack)
- 25+ I/O signals wired via Station Logic; 20+ Station Logic connections
- 30+ targets, 5+ paths, work objects for feeder, weld zone, conveyor end, pallets A/B
- Motion types: MoveJ, MoveL, MoveC (circular weld seams); pallet-B positions computed with `DIV`/`MOD`
- HMI module with FlexPendant menus (TPReadFK), diagnostics, emergency-stop routine

**Result:** Stable 12-part demo cycle (4 + 8) with automatic stop and green-light signal on completion.

**Skills demonstrated:** ABB RAPID programming · Smart Components · multi-controller signal synchronization · industrial robot path planning · sensor-driven adaptive logic

---

## LV — for LV CV

**WPL_Station — Trīs robotu metināšanas un paletizēšanas līnija (ABB RobotStudio, 2026)**

Izstrādāta un simulēta pilnībā automatizēta ražošanas šūna ar trim ABB robotiem — IRB 2600 (padevējs), IRB 1660ID (metinātājs), IRB 460 (paletizētājs) — kas darbojas uz trim neatkarīgiem virtuālajiem kontrolleriem. Līnija apstrādā 12 detaļas ciklā (4 augstās → palete A, 8 zemās → palete B) ar automātisku detaļas tipa noteikšanu pēc augstuma un adaptīvu trajektorijas izvēli.

**Tehniskais apjoms**
- 5 RAPID moduļi 3 kontrolleros, 20+ procedūras, lietotāja funkcijas
- 8 viedie komponenti (konveijera vadība, satvērēji, metināšanas vizualizācija, palešu skaitītāji)
- 25+ I/O signāli caur Station Logic
- 30+ mērķpunkti, kustību tipi MoveJ / MoveL / MoveC
- HMI ar FlexPendant izvēlni, diagnostika, avārijas apturēšana

**Rezultāts:** Stabils 12 detaļu demo cikls ar automātisku noslēgšanu.

**Prasmes:** ABB RAPID · Smart Components · daudzkontrolleru sinhronizācija · industriālo robotu kustības plānošana

---

## Files in this project folder
- `WPL_Station_Tehniskais_Apraksts.pdf` — full technical description (12 pages, LV)
- `WPL_Station.rspag` — packed RobotStudio station file (the actual working simulation)
- `Cycle_demo.mp4` — full demo cycle video (logic & motion)
- `wpl_flow_diagram.png` — process flow diagram

## CV bullet (short, EN)
> *Designed a 3-robot ABB RobotStudio welding & palletizing line (IRB 2600 / 1660ID / 460) with 5 RAPID modules across 3 virtual controllers, 8 Smart Components, and 25+ Station Logic signals; stable 12-part adaptive cycle with height-based trajectory selection.*

## CV bullet (short, LV)
> *Izstrādāta 3 robotu ABB RobotStudio metināšanas un paletizēšanas līnija (IRB 2600 / 1660ID / 460) ar 5 RAPID moduļiem 3 virtuālajos kontrolleros, 8 viedajiem komponentiem un 25+ Station Logic signāliem; stabils 12 detaļu adaptīvs cikls.*
