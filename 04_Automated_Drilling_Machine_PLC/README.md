# 04 — Automated Two-Hole Drilling Machine (PLC + GRAFCET + FluidSIM)

> Automatizēta iekārta divu urbumu izveidošanai sagatavē
> Automated machine for drilling two holes in a workpiece

**Context:** RTU studiju projekts, *Ražošanas Automatizācijas pamati*, 3. uzdevums, RMCE01, 2. kurss, 2024/2025
**Group code:** 231RMC173

---

## EN — for GitHub README / EN CV

**Automated Drilling Machine — PLC control with GRAFCET, FBD and FluidSIM (2024/2025)**

End-to-end design of a discrete-event automation cell that drills two holes in a parallelepiped workpiece. The operator loads the part; START triggers a sequence of three pneumatic cylinders coordinated with a drill-rotation motor, with full safety and dual-mode control.

**Process sequence**
1. Cylinder **A** clamps the workpiece; clamping force sensor **P1** confirms max force reached.
2. Drill motor starts; cylinder **B** advances drill (slow feed) and retracts (fast return).
3. Cylinder **C** shuttles the carriage to the second drilling position.
4. Second hole drilled by repeating B cycle.
5. Clamp releases, carriage returns home, motor stops.

**Engineering deliverables (Section A — GRAFCET in FluidSIM)**
- GRAFCET cycle built on cylinder end-states (A0/A1, B0/B1, C0/C1), with **P1 sensor gating** ensuring B advances only after clamping force is reached.
- Motor synchronization: motor energized in the same step that initiates B+, so rotation runs only during drilling.

**Engineering deliverables (Section B — PLC FBD on Siemens LOGO!)**
- Classical electrical schematic with relays and 6 solenoid valves (Y1–Y6) as the logic backbone.
- Base FBD cycle ported from the electrical schematic, verified for state-machine integrity.
- **Emergency stop (AV.STOP)** — relay K3 immediately halts cycle and triggers Y8 to dump pneumatic pressure; alarm indicator.
- **Reset** — manual return-to-home with output and relay clear-down.
- **Auto / Manual (SOLU_R) modes** — STEP button advances one transition at a time in manual; AUTO returns to free-running cycle; mode indicators on the panel.
- **HANDS_OFF safety** — optical sensor blocks cycle start while the operator's hand is in the work envelope.

**Skills demonstrated:** PLC programming (Siemens LOGO!, FBD) · GRAFCET sequence design · FluidSIM pneumatic/electric simulation · electrical relay schematics · industrial safety design (E-stop, light-curtain logic, mode switching)

---

## LV — for LV CV

**Automatizēta urbšanas iekārta — PLC vadība ar GRAFCET, FBD un FluidSIM (2024/2025)**

Pilna diskrētas darbības automatizācijas sistēma divu urbumu izveidošanai paralēlskaldņa sagatavē. Pēc START pogas trīs pneimocilindri (A iespīlēšana, B urbja padeve, C kamanu pārbīde) tiek sinhronizēti ar urbja rotācijas elektrodzinēju.

**Izstrādes apjoms**
- **Sadaļa A — GRAFCET FluidSIM vidē:** cikls balstīts uz cilindru gala stāvokļiem; P1 spiediena sensors nodrošina, ka B+ izvirzīšanās sākas tikai pēc maksimālā iespīlēšanas spēka sasniegšanas.
- **Sadaļa B — Siemens LOGO! FBD risinājums:** elektriskā shēma ar relejiem un 6 vārstiem (Y1–Y6); pamatcikls PLC programmā.
- **Avārijas stops (AV.STOP)** — relejs K3 + Y8 pneimatiskās padeves pārtraukšana.
- **Reset** — manuāla atgriešanās sākuma stāvoklī.
- **Auto / Manual (SOLU_R) režīmi** — STEP poga soļa pa solim kontrolei.
- **HANDS_OFF** — optiskais sensors bloķē cikla palaišanu, ja darba zonā ir roka.

**Prasmes:** PLC programmēšana (Siemens LOGO!, FBD) · GRAFCET algoritma izstrāde · FluidSIM pneimatiskā/elektriskā modelēšana · releju vadības shēmas · industriālā drošības projektēšana

---

## Files in this project folder
- `MD_3.uzd_Razosanas_Automatizacijas_pamati.docx` — full report (LV) with schematic figures
- `fluidsim_sources/GRAFCET_FluidSIM.ct` — original GRAFCET FluidSIM file (Section A)
- `fluidsim_sources/Elektriska_shema.ct` — electrical schematic with relays
- `fluidsim_sources/Hard_FBD.ct` — full PLC FBD program
- `fluidsim_sources/Grafcet.ct` + `Automatizacija_final.ct` — iteration versions

## CV bullet (short, EN)
> *Designed a PLC-controlled two-hole drilling cell in Siemens LOGO! (FBD) with GRAFCET sequence in FluidSIM — 3 pneumatic cylinders, 6 solenoid valves, P1 pressure gating, plus E-stop, Auto/Manual STEP modes and HANDS_OFF optical safety.*

## CV bullet (short, LV)
> *Izstrādāta PLC vadīta divu urbumu automatizēta iekārta Siemens LOGO! vidē (FBD) ar GRAFCET ciklu FluidSIM — 3 pneimocilindri, 6 elektromagnētiskie vārsti, spiediena sensora bloķēšana, avārijas stops, Auto/Manual STEP režīmi un HANDS_OFF optiskā drošība.*
