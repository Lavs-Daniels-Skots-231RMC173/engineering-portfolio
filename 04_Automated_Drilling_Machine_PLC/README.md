<div align="center">

[← back to portfolio](../README.md)

# 🔌 Project 04

[![Tech1](https://img.shields.io/badge/-Siemens_LOGO!-009999?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-GRAFCET-512BD4?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-FluidSIM-0091D5?style=for-the-badge)](#)

</div>

---

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

![Auto/Manual mod