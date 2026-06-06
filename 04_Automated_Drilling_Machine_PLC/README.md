# 04 — Automated Two-Hole Drilling Machine

> Automatizēta iekārta divu urbumu izveidošanai sagatavē
> PLC control with GRAFCET sequence, FBD program and FluidSIM simulation

**Context** RTU studiju projekts · *Ražošanas Automatizācijas pamati* (Production Automation Basics) · 3. uzdevums (Task 3) · RMCE01 · 2nd year · 2024/2025
**Tools** FluidSIM (electropneumatic + GRAFCET simulation) · Siemens LOGO! SoftComfort (FBD)
**Target** Siemens LOGO! PLC

---

## The brief

The brief described the machine in plain language: *"In a parallelepiped workpiece two holes must be drilled. The operator places the workpiece in the clamp. After pressing the start button: pneumatic cylinder A clamps the workpiece. When clamping force reaches maximum, the drill rotation motor starts and pneumatic cylinder B advances/retracts the drill (slow forward / fast return). Then pneumatic cylinder C shuttles the carriage to the second position and the second hole is drilled the same way. Then the clamp releases, the carriage returns to start, the drill motor stops."*

This must be implemented with full automation. The deliverables are split into two sections:
- **Section A** — GRAFCET sequence diagram in FluidSIM
- **Section B** — implementation in FBD (Function Block Diagram) targeting a programmable Siemens LOGO!

Plus full safety and operating modes.

---

## The actuators

Three pneumatic cylinders + one electric motor:

| Element | Role | Direction control | End sensors |
|---|---|---|---|
| **Cylinder A** | Workpiece clamping | Y1 (extend), Y2 (retract) | A0 (home), A1 (clamped), **P1** (force sensor at max) |
| **Cylinder B** | Drill feed | Y3 (slow extend), Y4 (fast retract) | B0 (home), B1 (drill depth reached) |
| **Cylinder C** | Carriage shuttle | Y5 (extend), Y6 (retract) | C0 (position 1), C1 (position 2) |
| **Motor M1** | Drill rotation | K1 (start), K3 (emergency stop) | — |

Plus safety-system valves: Y7 (general air supply), Y8 (emergency dump).

---

## Section A — GRAFCET in FluidSIM

![GRAFCET diagram](images/04_plc_grafcet.png)

*Fig. 1 — GRAFCET cycle in FluidSIM: states built on cylinder end-states (A0/A1, B0/B1, C0/C1) with the P1 clamping-force sensor gating B+ advance*

The cycle is structured around the cylinder end-position sensors so transitions are clean and unambiguous. Two engineering catches required iteration:

1. **The P1 gating** — The brief specifies that B+ must wait until clamping reaches **max force**, not just until A is extended. A naive GRAFCET (B+ on A1) won't satisfy that. Solution: add a guard `A1 AND P1` on the transition from "clamping" to "drilling" — only proceed when the force sensor fires.
2. **Motor / drill synchronization** — The motor must run only during drilling, not during clamp/release or carriage shuttle. Solution: put the motor `K1` on the same step that initiates B+ (so the motor turns on for the drilling step and off when the step ends).

---

## Section B — FBD implementation on Siemens LOGO!

The starting point is a classical electrical schematic — relay logic + 6 solenoid valves — that serves as the conceptual backbone:

![Electrical schematic with relays](images/04_plc_electric_clean.png)

*Fig. 2 — Electrical relay schematic: Y1–Y6 solenoid valves, R-relays for sequencing, start/stop buttons. This was the "paper" form before porting to PLC FBD.*

Then the FBD program in LOGO! SoftComfort:

![Full FluidSIM system](images/04_plc_full.png)

*Fig. 3 — Final FluidSIM simulation: pneumatic system (cylinders A/B/C with end-position switches, valves Y1–Y6, P1 force sensor), PLC FBD program controlling them, cylinder-motion timing diagram on the right, plus the machine animation*

The FBD has the basic cycle wired around set/reset flip-flops for each cylinder, transition logic for the sequence, and a "system ready" gate that prevents START from working unless safe.

---

## Safety and operating modes

After the base cycle worked, three layers were added:

### Emergency stop (AV.STOP)

![E-stop](images/04_plc_estop.png)

*Fig. 4 — Emergency stop circuit: red AV STOP button → relay K3 → halts the cycle and dumps pneumatic supply via Y8. An indicator light shows the system is in emergency state.*

Pressing the red mushroom button activates **relay K3**, which:
- Immediately halts the cycle (cuts power to active valves)
- Activates **valve Y8** which dumps the main pneumatic supply (zero pressure on cylinders → no movement)
- Lights the emergency indicator

After emergency, a **RESET** button manually re-arms: clears all outputs, deactivates relays, returns to home state. Cycle can be restarted.

### Auto / Manual modes (SOLU_R)

![Auto/Manual modes](images/04_plc_modes.png)

*Fig. 5 — Mode switching: button SOLU_R activates manual (step-by-step) mode where each transition waits for STEP press. AUTO returns to free-running automatic. Two indicator lights show which mode is active.*

- **Auto mode** (default): full cycle runs continuously after START.
- **Manual mode** (after pressing `SOLU_R`): cycle pauses at each transition. Operator presses **STEP** to advance one stage at a time. Useful for training, troubleshooting and slow walk-throughs.

### Hands-off safety (HANDS_OFF)

![Hands-off sensor](images/04_plc_handsoff.png)

*Fig. 6 — HANDS_OFF gate: optical light-curtain sensor monitors the operator's hand zone. The cycle cannot start while the sensor is interrupted. Wired as a separate input; checked before START is enabled.*

An optical sensor watches the work envelope. The cycle **cannot start** while the sensor is interrupted — so the operator's hand inside the working area blocks unsafe start-up. The sensor input is wired through the START enable.

---

## Files in this folder

| File | Size | What's inside | How to view |
|---|---:|---|---|
| `MD_3.uzd_Razosanas_Automatizacijas_pamati.docx` | 4.4 MB | Full study work report (LV) — narrative description, all 8 figures (electrical, GRAFCET, FluidSIM with minimal functionality, full FBD on PLC, AV.STOP, SOLU_R modes, HANDS_OFF, integrated final), conclusions. The main reference document. | Word/LibreOffice |
| `fluidsim_sources/GRAFCET_FluidSIM.ct` | — | Original GRAFCET diagram from FluidSIM (Section A solution) | **FluidSIM** (Festo) |
| `fluidsim_sources/Elektriska_shema.ct` | — | Electrical relay schematic — backbone for the FBD port | FluidSIM |
| `fluidsim_sources/Hard_FBD.ct` | — | Full PLC FBD program with all safety + modes | FluidSIM |
| `fluidsim_sources/Grafcet.ct` | — | Intermediate GRAFCET iteration | FluidSIM |
| `fluidsim_sources/Automatizacija_final.ct` | — | Final integrated solution | FluidSIM |
| `images/` | — | Extracted figures used in this README | — |

---

## How to open the simulation files

The `.ct` files are **FluidSIM project files** (Festo Didactic's electropneumatic / GRAFCET / PLC simulator).

- **Software:** Festo FluidSIM (versions FluidSIM-P, FluidSIM-H, FluidSIM-E or the unified FluidSIM 6+). Demo versions are usually screen-shot only; the full version is needed to *run* the simulation but the file structure is readable for visual inspection.
- **Open:** *File → Open* → select the `.ct` file
- **Run:** *Simulation → Start* (or F9). The pneumatic cylinders animate, sensors trigger, the GRAFCET steps highlight, and the PLC outputs activate live.
- **Inspect the FBD program:** double-click the PLC block → opens the block diagram view → you can step through inputs/outputs as the simulation runs.

If you don't have FluidSIM available, the `.docx` report contains all 8 figures as embedded screenshots — sufficient to follow the design.

---

## Skills demonstrated

- **PLC programming** (Siemens LOGO! FBD)
- **GRAFCET sequence design** — proper transition formulation, parallel/sequential structures
- **FluidSIM electropneumatic + PLC co-simulation**
- **Electrical relay schematic design** — set/reset, sequencing
- **Industrial safety design**:
  - E-stop architecture (relay K3 + Y8 air dump)
  - Operating-mode switching (Auto / Manual STEP)
  - Light-curtain hand-presence interlock
- **Multi-mode operator interface** (AUTO, MANUAL STEP, RESET, AV STOP)

---

## Latvian summary (LV)

Šis projekts ir automātiska divu urbumu urbšanas iekārta — pilna automatizācijas sistēma trim pneimocilindriem (A iespīlēšana, B urbja padeve, C kamanu pārvietošana) un urbja rotācijas elektromotoram. Risinājums sastāv no divām daļām: **A sadaļa** — GRAFCET sekvences diagramma FluidSIM vidē; **B sadaļa** — programmēta vadība FBD (funkciju bloku diagramma) formā uz Siemens LOGO!

Galvenais GRAFCET izstrādes mācība: P1 spiediena sensors jāizmanto kā vārti starp iespīlēšanas un urbšanas soļiem (nevis tikai A1 gala stāvokli) — tas nodrošina pareizu iespīlēšanas spēka kontroli pirms urbšanas sākuma.

Pievienoti drošības un operatora režīmi: **AV.STOP** (avārijas apturēšana ar K3 + Y8 pneimatiskās padeves pārtraukšanu), **SOLU_R** (manuālais soļa pa solim režīms ar STEP pogu), **HANDS_OFF** (optiskais sensors bloķē cikla palaišanu, ja darba zonā ir roka).

Pilna dokumentācija failā `MD_3.uzd_Razosanas_Automatizacijas_pamati.docx`. Visi FluidSIM projektu faili (`*.ct`) — `fluidsim_sources/` apakšmapē.
