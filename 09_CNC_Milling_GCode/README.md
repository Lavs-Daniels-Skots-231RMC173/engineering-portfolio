# 09 — CNC Milling Programming (G-code, CNC Simulator Pro)

> Laboratorijas darbs: CNC frēzes programmēšana G-kodos
> Lab: CNC milling programming in G-code

**Context:** RTU studiju projekts, RMCE01, 3. kurss, 16.11.2025
**Tooling:** CNCSimulator Pro
**Machine simulated:** HobbyMill — vertical CNC milling machine
**Workpiece:** 150 × 100 × 20 mm

---

## EN — for GitHub README / EN CV

**CNC Milling — Hand-written G-code program (CNC Simulator Pro, 2025)**

Wrote a complete G-code program from scratch to machine a "rocket with stars" pattern on a 150 × 100 × 20 mm workpiece using two tools, then verified the toolpath in CNC Simulator Pro.

**Tools used**
- **T6** — Ø5 mm cylindrical flat end mill (body & rocket contour)
- **T7** — Ø5 mm conical / pointed end mill (stars)

**Program structure**
- CNC Simulator Pro setup: `$Mill`, `$Millimeters`, `$AddMillPart 170 120 20 …` (workpiece definition), `$DefineMillTool` for each cutter, `$ReadTasDefinedTool`
- Header: `G21` (metric) · `G90` (absolute) · `G92` work-offset zero
- Tool change cycles: `T6 M6` → spindle on `M03 S2500` → feed `F400 / F350 / F300`
- Rocket body — closed linear contour via `G01` with five-point silhouette
- Window — `G02` circular interpolation
- Wings (left + right) — symmetric linear contours
- Flame — triangular profile
- Stars — cross-hair patterns at five positions with the conical tool

**Skills demonstrated:** manual G-code programming (G00/G01/G02, G21/G90/G92) · M-code (M03 spindle, M06 tool change) · CNC Simulator Pro setup commands · tool/feed/speed selection per material and operation · multi-tool job sequencing · workpiece-coordinate system setup

---

## LV — for LV CV

**CNC frēzēšana — manuāli rakstīts G-koda programmēšanas darbs (CNC Simulator Pro, 2025)**

Izstrādāta pilna G-koda programma no nulles raķetes ar zvaigznēm frēzēšanai uz 150 × 100 × 20 mm sagataves ar diviem instrumentiem; trajektorija pārbaudīta CNC Simulator Pro vidē.

**Instrumenti:** T6 (Ø5 mm cilindriskā gala frēze) korpusam un kontūrai; T7 (Ø5 mm koniskā gala frēze) zvaigznēm.

**Programmas struktūra**
- CNC Simulator Pro definīcijas: `$Mill`, `$AddMillPart`, `$DefineMillTool`
- Galvene: `G21` (mm), `G90` (absolūtais), `G92` darba koordinātu nulle
- Instrumentu maiņa `T6 M6` / `T7 M6`, vārpsta `M03 S2500`
- Raķetes korpuss — slēgta lineārā kontūra ar `G01`
- Logs — `G02` apļveida interpolācija
- Spārni (kreisais + labais) — simetriskas lineārās kontūras
- Liesma un piecas zvaigznes

**Prasmes:** manuāla G-koda rakstīšana (G00/G01/G02, G21/G90/G92) · M-kodu lietošana · CNC Simulator Pro definīciju komandas · instrumentu, padevju un griešanas ātrumu izvēle · daudzpārejas darba secība · darba koordinātu sistēmas iestatīšana

---

## Files in this folder
- `CNC_Lab_Daniels_Skots_Lavs.doc` — full lab report with screenshots and full G-code
- `CNC_Lab_text.txt` — text-only extract of the lab report
- `1001.nc` / `1002.nc` — Fusion 360 CAM-generated G-code (ball end mill T23, 2D contour) — to confirm with Daniel whether his work or reference

## CV bullet (short, EN)
> *Wrote a complete CNC milling program in G-code from scratch (CNC Simulator Pro, HobbyMill) — two-tool rocket-and-stars contour on 150×100×20 mm stock with G02 arcs, multi-tool job sequencing and CAM-style work-offset setup.*

## CV bullet (short, LV)
> *Izstrādāta pilna CNC frēzēšanas G-koda programma no nulles (CNC Simulator Pro, HobbyMill) — divu instrumentu raķetes-ar-zvaigznēm kontūra uz 150×100×20 mm sagataves ar G02 lokiem un daudzpārējiem darba soļiem.*
