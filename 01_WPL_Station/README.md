# 01 — WPL_Station: Three-Robot Welding & Palletizing Line

> Trīs robotu metināšanas un paletizēšanas līnija ABB RobotStudio vidē
> Three-cooperating-robot automated production cell simulated in ABB RobotStudio 2023

**Context** RTU studiju projekts (course project) · RMCE01 · 3rd year · 2026
**Supervisor** Artjoms Supoņenkovs
**Tools** ABB RobotStudio 2023 · RAPID · Smart Components · Station Logic

---

## Overview

WPL_Station is a fully automated production cell designed and simulated in ABB RobotStudio that models a realistic scenario in which three ABB robots cooperate to feed, weld and sort parts onto pallets. The cell handles **two part types** (tall yellow PART_Tall and short blue PART_Short, distinguished by height sensors) and runs a full demo cycle of **12 parts** — 4 onto pallet A and 8 onto pallet B — autonomously.

The project demonstrates:
- Multi-robot orchestration across three independent virtual controllers
- Smart Components for sensor and actuator logic outside RAPID
- Adaptive trajectory selection driven by sensor input (HIGH/LOW welding paths chosen by detected part height)
- Mass-production cycle synchronization with full HMI, alarms and safety stops

![WPL Station overview](images/01_wpl_full_view.png)

*Fig. 1 — Overall WPL_Station layout in ABB RobotStudio 2023: three ABB robots, conveyor, parts magazine, two pallet zones, light stack and safety fence*

---

## The three robots and their roles

![Three robots with tools](images/01_wpl_robots.png)

| Robot | Model | Tool | Function |
|---|---|---|---|
| R1_Feeder | IRB 2600 12/1.85 | Tool_MagnetGrip (custom) | Feed cycle simulation and part-generation signaling |
| R2_Welder | IRB 1660ID 4/1.55 | Tool_WeldingGun (Binzel WH455D) | Welding with HIGH/LOW trajectory selection by height |
| R3_Palletizer | IRB 460 110/2.4 | Tool_PalletGrip (Equipment Builder) | Sorting and placement to pallet A or pallet B |

Each robot runs on its own virtual controller (`Sys_R1_Feeder`, `Controller_Welder`, `Sys_R3_Palletizer`).

---

## Station Logic — how the three controllers talk

![Station Logic signals](images/01_wpl_station_logic.png)

*Fig. 2 — Station Logic signal wiring: 8 Smart Components connected via 20+ I/O signals between 3 virtual controllers*

The cell uses **25+ discrete I/O signals** wired through Station Logic across 8 Smart Components:

- **SC_Conveyor** — the most complex one. Generates parts (Source_Tall / Source_Short), moves them with LinearMover @ 200 mm/s, detects them with LineSensor_BeltLength, and provides Inf/Sup sensor pairs at the weld zone and at the conveyor end
- **SC_MagnetGrip** — magnet gripper logic for R1 (visual imitation)
- **SC_VentosaTool** — vacuum gripper logic for R3 (Attacher, Detacher, TipSensor, LogicGate_NOT)
- **SC_WeldingGun** — Highlighter-based weld-visualization effect triggered by DI_WeldActive
- **SC_PalletLogic_A / SC_PalletLogic_B** — Counter + Comparer pallet counters that raise doPalletAFull / doPalletBFull at 4 / 8 parts respectively
- **SC_PalletMover** — auxiliary pallet B mover (kept as optional functionality)
- **SC_LightStack** — Highlighter-based signal-tower control (green, yellow, red)

---

## Inf/Sup sensor pairs — the trick that drives adaptive logic

![Sensors layout](images/01_wpl_sensors.png)

Two sensor pairs are placed along the conveyor — one at the weld zone (R2) and one at the conveyor end (R3). In each pair:

- **Inferior (Inf)** sensor sits low and triggers on ANY part (presence detection)
- **Superior (Sup)** sensor sits higher and triggers ONLY on tall parts (height detection)

When a part arrives at R2:
- `LineSensor_Welder_Inf` activates → conveyor stops, R2 starts welding cycle
- `LineSensor_Welder_Sup` activates only for tall parts → R2 chooses **HIGH trajectory** (raised 150 mm in Z); otherwise **LOW trajectory**

The same Inf/Sup pattern at R3 decides whether the part goes to pallet A (tall) or pallet B (short).

---

## RAPID programs across 3 controllers

Five RAPID modules, 20+ procedures, custom `FUNC`s. Highlights:

![RAPID code](images/01_wpl_rapid_code.png)

**R2_Welder Module1** — main welding cycle:

```rapid
WHILE TRUE DO
    rWaitForPart;
    IF DInput(DO_Sensor_Welder_Sup) = 1 THEN
        rWeldFullContour_High;
    ELSE
        rWeldFullContour_Low;
    ENDIF
    Incr weldCycleCount;
ENDWHILE
```

**R3_Palletizer** — pallet B 4×2 grid via DIV/MOD on counter:

```rapid
PROC rPlaceOnB()
    VAR num row;
    VAR num col;
    row := palletBIdx DIV 4;
    col := palletBIdx MOD 4;
    MoveJ Offs(tPalB_P_1, col*270, row*400, 250), v500, fine,
          tcp_palletgrip\WObj:=wobj_PalletB;
    MoveL Offs(tPalB_P_1, col*270, row*400, -130), v150, fine,
          tcp_palletgrip\WObj:=wobj_PalletB;
    Set DI_Attach_R3;
    PulseDO\PLength:=0.3, diBoxPlacedB;
    MoveL Offs(tPalB_P_1, col*270, row*400, 250), v300, fine,
          tcp_palletgrip\WObj:=wobj_PalletB;
    Reset DI_Attach_R3;
    Incr palletBIdx;
ENDPROC
```

**R2_HelperMod** — separate module with operator menu (`TPReadFK`), diagnostics, emergency-stop routine and helper `FUNC fIsWelderBusy`.

Motion types used: **MoveJ** (joint interpolation), **MoveL** (linear), **MoveC** (circular for weld seams), with `Offs()` parametric offsets.

---

## Full cycle flow — 12 parts in (4 tall + 8 short), 0 errors out

![Process flowchart](images/01_wpl_flowchart.png)

*Fig. 3 — Full process flow: feeder pulse → conveyor transport → R2 weld zone (Inf/Sup sensors decide LOW or HIGH path) → conveyor restart → R3 sort by Tall/Short to pallet A (2×2) or pallet B (4×2)*

The demo cycle:

1. **R1 feeds** — `Crear_Caja_gr` (tall) or `Crear_Caja_pq` (short) pulse, alternating per a `partType := feedCount MOD 2` rule; `SC_Conveyor.Source` clones the matching template at (100, 0, 450)
2. **Conveyor transports** — `LineSensor_BeltLength` picks up the new part as a `BoxPart` and pipes it to `LinearMover` via Property Binding
3. **R2 welds** — `LineSensor_Welder_Inf` halts the conveyor (`Reset DI_Run_After_Weld`); height sensor `DO_Sensor_Welder_Sup` decides HIGH vs LOW trajectory; on completion, conveyor restarts
4. **R3 sorts** — `LineSensor_Inferior` at end activates; R3 checks height sensor `DO_Sensor_Sup` and places on pallet A (2×2 grid, tall) or pallet B (4×2 grid, short)
5. **Cycle ends** when `palletAIdx ≥ 4 AND palletBIdx ≥ 8` — R3 calls `Stop`, signal tower switches to green

---

## Files in this folder

| File | Size | What's inside | How to view |
|---|---:|---|---|
| `WPL_Station_Tehniskais_Apraksts.pdf` | 933 KB | 12-page technical description (LV) with all tables, signal lists, RAPID excerpts and process flow diagrams | Any PDF viewer |
| `WPL_Station.rspag` | 66 MB | Packed RobotStudio station — full simulation environment with all controllers, robots, Smart Components and RAPID modules | Open in **ABB RobotStudio 2023 or later** via *File → Open → Unpack & Work Wizard* |
| `Cycle_demo.mp4` | 26 MB | Screen recording of one full demo cycle (12 parts, ~3 minutes) — robots, conveyor, weld effect, pallets filling | Any video player |
| `wpl_flow_diagram.png` | 208 KB | Process flow diagram with decision branches for HIGH/LOW path and pallet A/B | Any image viewer |
| `images/` | — | High-resolution figures extracted from the report (used in this README) | — |

---

## How to open the simulation (`.rspag`)

The `.rspag` file is a **Pack & Go** archive that includes:
- 3 virtual controllers and their RAPID modules
- All Smart Components and their I/O bindings
- The 3D station geometry
- Backup snapshots

To open and run:

1. Install **ABB RobotStudio 2023 or newer** (free Basic license is enough; download from new.abb.com/products/robotics/robotstudio)
2. Launch RobotStudio
3. **File → Open** → select `WPL_Station.rspag`
4. The Unpack & Work Wizard opens — keep defaults, click **Next** through, **Finish**
5. The station opens. Wait for all three virtual controllers to start (~30 sec)
6. Right panel → **Simulation tab** → click **Play** to start the cycle
7. Watch the parts feed in, weld, palletize. Process completes when both pallets are full and the light tower goes green

To inspect the code:
- **Controller browser** (left panel) → expand each controller → RAPID → T_ROB1 → modules
- Or attach to a running controller: **Controller** tab → **FlexPendant** for HMI menus

---

## Skills demonstrated

- **ABB RAPID programming** — `Move*` instructions, work-object math (`Offs`, `DIV`/`MOD`), `WaitDI` synchronization, FlexPendant HMI (`TPReadFK`, `TPWrite`)
- **Smart Components** — Source, LinearMover, LineSensor, Highlighter, Attacher/Detacher, Counter/Comparer wired via Property Binding
- **Multi-controller signal synchronization** — Station Logic with 25+ I/O signals across 3 virtual controllers
- **Industrial robot path planning** — MoveJ for transitions, MoveL for precise approaches, MoveC for circular weld seams
- **Sensor-driven adaptive logic** — Inf/Sup pair detection drives both branch selection (HIGH/LOW welding) and routing (pallet A/B)
- **Safety integration** — emergency-stop routine, status indication via light tower

---

## Latvian summary (LV)

Šis projekts ir trīs robotu metināšanas un paletizēšanas līnijas pilna RobotStudio simulācija — trīs ABB roboti (IRB 2600 padevējs, IRB 1660ID metinātājs, IRB 460 paletizētājs) sadarbojas, lai apstrādātu 12 detaļas (4 augstās → palete A 2×2, 8 zemās → palete B 4×2). Galvenais tehniskais izaicinājums — adaptīva metināšanas trajektoriju izvēle pēc augstuma sensora (HIGH/LOW) un palešu paralēla pildīšana ar DIV/MOD koordinātu aprēķinu.

Pilna tehniskā dokumentācija ir failā `WPL_Station_Tehniskais_Apraksts.pdf`. Pati simulācija ir `WPL_Station.rspag` Pack & Go arhīvā, ko var atvērt ar ABB RobotStudio 2023.
