<div align="center">

[← back to portfolio](../README.md)

# 📊 Project 08

[![Tech1](https://img.shields.io/badge/-Jupyter-F37626?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-NumPy-013243?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-LaTeX-008080?style=for-the-badge)](#)

</div>

---

# 08 — Flat Belt Drive Design in Jupyter

> Plakansiksnas pārvada aprēķins — mašīnu elementu aprēķins Python vidē
> Mechanical-element design implemented as a reproducible Jupyter notebook

**Context** RTU · Mašīnu elementu (Machine Elements) course · RMCE01
**Tools** Jupyter Notebook · NumPy · LaTeX (markdown math)
**Format** 45 cells — 21 code + 23 markdown derivations

---

## Why a notebook instead of a spreadsheet

Mechanical-element design problems are classically done on paper or in Excel. I implemented this one as a **Jupyter notebook** for three reasons:

1. **Reproducibility** — change one input (say motor speed) and re-run; all downstream values update consistently. No copy-paste errors.
2. **Documented derivations** — every formula is written out in LaTeX in a markdown cell *before* the code cell that computes it. The notebook reads like a textbook chapter where every step is shown.
3. **Reusability** — the notebook becomes a template for any future flat-belt drive sizing exercise. Change the inputs, get a different design.

This approach scales — for more complex mechanical systems, the same pattern (LaTeX derivation → NumPy computation) makes the engineering reviewable and verifiable.

---

## The task

Design a flat-belt power transmission connecting two horizontally and parallel-mounted shafts. Given the motor speed and power, the driven shaft speed target, the axis distance and the belt material — compute:

- Required belt width, type and thickness
- Pre-tension, centrifugal and tight/slack-side forces
- Resultant force on the shafts (for bearing sizing)
- Effective belt length and required take-up

---

## The drive — geometric scheme

![Belt drive scheme](images/08_belt_scheme.png)

*Fig. 1 — Geometric scheme of the flat belt drive: driver pulley d, driven pulley D, axis distance C, wrap angle β. Two horizontally-mounted parallel shafts (1. att. in the notebook).*

Notation used throughout the notebook:
- `d`, `D` — driver and driven pulley diameters (m)
- `C` — center distance between shafts (m)
- `β` — wrap angle on the small pulley (radians)
- `n_m`, `n_s` — motor and driven shaft rotation speeds (rpm)
- `ω_d` — angular velocity of driver pulley (rad/s)
- `v` — belt linear velocity (m/s)
- `F_u`, `F_i`, `F_c`, `F_1`, `F_2`, `F_ω` — tangential, pre-tension, centrifugal, tight-side, slack-side, resultant forces (N)
- `L_eff` — effective belt length (m)
- `e_0`, `X_e` — belt elongation factor and required take-up (m)

---

## Inputs (with full justification in notebook)

![Belt formulas](images/08_belt_formulas.png)

*Fig. 2 — Input parameters (left) and the chain of NumPy-computed formulas (right) — from angular velocity through tensions to required take-up. Each formula has its derivation in a markdown cell above it.*

```python
n_m = 3000                # motora apgriezieni (motor speed, rpm)
P   = 500                 # motora jauda (motor power, W)
n_s = 1000                # dzenošā skriemeļa apgriezieni (driven pulley, rpm)
C   = 1.5                 # asu attālums (axis distance, m)
Ks  = 1.15                # darba režīma koeficients (se