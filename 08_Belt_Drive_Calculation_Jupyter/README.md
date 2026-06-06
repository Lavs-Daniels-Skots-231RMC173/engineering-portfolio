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

Mechanical-element design problems are classically done on paper or in Excel. Implementing this as a **Jupyter notebook** gives three advantages:

1. **Reproducibility** — change one input (motor speed), re-run, all downstream values update consistently. No copy-paste errors.
2. **Documented derivations** — every formula written out in LaTeX in a markdown cell *before* the code cell that computes it.
3. **Reusability** — the notebook becomes a template for future flat-belt drive sizing exercises.

---

## The task

Design a flat-belt power transmission for two horizontally and parallel-mounted shafts. Given motor speed + power, driven shaft target speed, axis distance and belt material → compute:
- Required belt width, type, thickness
- Pre-tension, centrifugal, tight/slack-side forces
- Resultant force on the shafts (for bearing sizing)
- Effective belt length and required take-up

---

## The drive — geometric scheme

![Belt drive scheme](images/08_belt_scheme.png)

*Fig. 1 — Driver pulley d, driven pulley D, axis distance C, wrap angle β. Two horizontally-mounted parallel shafts.*

Notation:
- `d`, `D` — pulley diameters (m)
- `C` — center distance (m)
- `β` — wrap angle (rad)
- `n_m`, `n_s` — motor / driven speed (rpm)
- `ω_d` — driver angular velocity (rad/s)
- `v` — belt linear velocity (m/s)
- `F_u`, `F_i`, `F_c`, `F_1`, `F_2`, `F_ω` — tangential, pre-tension, centrifugal, tight, slack, resultant (N)
- `L_eff` — effective belt length (m)
- `e_0`, `X_e` — elongation factor + take-up (m)

---

## Inputs

![Belt formulas](images/08_belt_formulas.png)

*Fig. 2 — Input parameters (left) + chain of NumPy formulas (right)*

```python
n_m = 3000               # motor speed, rpm
P   = 500                # motor power, W
n_s = 1000               # driven speed, rpm
C   = 1.5                # axis distance, m
Ks  = 1.15               # service factor
F_un = 36 * 1000         # nominal traction, N/m belt width
t = 3.4 / 1000           # belt thickness, m
m_i = 3.5                # belt mass per meter, kg/m
```

**Belt choice:** Habasit A3 — μ = 0.495, t = 3.4 mm, m_i = 3.5 kg/m, F_un = 36 kN/m. Drive ratio u = n_m / n_s = 3.0.

---

## The calculation chain — 21 code cells

### Driver angular velocity
```python
omega_d = (2 * np.pi * n_m) / 60     # rad/s
```

### Pulley diameters + wrap angle
Computed from u + C, verified against belt-material limits.

### Belt linear velocity
```math
v = ω_d · (d/2)
```

### Forces
```math
F_u = P / v                        (tangential, transmitted)
F_c = m_i · v²                     (centrifugal)
F_i = pre-tension (Euler with μ, β)
F_1 = F_i + F_c + F_u/2            (tight side)
F_2 = F_1 - F_u                    (slack side)
F_ω = F_1 + F_2 · sin(β/2) + 2·F_c (resultant — sizes the bearings)
```

### Effective belt length + take-up
```math
L_eff = 2C · sin(β/2) + π/2 · (d+D+4·t/2 + ((D-d)·(180-β)/180))
e_0   = (F_i + F_c) / (b · K_1)
X_e   = (L_eff · e_0) / (2 · 100)
```

X_e is the linear adjustment range the tensioning mechanism must provide.

---

## Files in this folder

| File | Size | What |
|---|---:|---|
| `Plakansiksnas_parvada_aprekins.ipynb` | 324 KB | **Main notebook** — 45 cells, full design + LaTeX derivations + NumPy code + scheme + Habasit catalog page |
| `Plakansiksnas_v31.ipynb` | 324 KB | Secondary version |
| `images/` | — | Figures used in this README |

---

## How to open & run

```bash
pip install jupyter numpy
cd 08_Belt_Drive_Calculation_Jupyter
jupyter notebook Plakansiksnas_parvada_aprekins.ipynb
```

Run cells in order with **Shift+Enter**. Each markdown shows the derivation; each code cell computes the next quantity and prints it.

**Parameter change:** edit cell 5 (inputs) — change `n_m = 3000` to `n_m = 2800`, then **Kernel → Restart & Run All** — all downstream values update consistently.

---

## Skills demonstrated

- **Mechanical-element design** — flat belt power transmission
- **Belt-drive theory** — pre-tension, centrifugal, tight/slack forces, wrap-angle correction
- **Bearing-load calculation** — resultant force on shafts
- **LaTeX-documented engineering math** — every formula shown before its code
- **NumPy numerical computation**
- **Jupyter as engineering notebook** — reproducible, parameter-driven
- **Manufacturer-catalog reading** — Habasit A3 spec integration

---

## Latvian summary (LV)

Plakansiksnas pārvada pilns aprēķins divām horizontāli un paralēli novietotām vārpstām, realizēts kā Jupyter Notebook ar NumPy. 45 šūnas — 21 koda + 23 markdown ar LaTeX formulām (katra formula parādīta *pirms* tās aprēķina).

**Ieejas dati:** n_m = 3000 rpm, P = 500 W, n_s = 1000 rpm, C = 1,5 m. Siksna Habasit A3 (μ = 0,495, t = 3,4 mm, m_i = 3,5 kg/m, F_un = 36 kN/m).

**Aprēķinātie izejas dati:** dzenošā skriemeļa leņķiskais ātrums ω_d, siksnas tips/platums/biezums, spriegošanas spēks F_i, centrbēdzes spēks F_c, spēki abām pusēm F_1, F_2, rezultējošais spēks uz vārpstām F_ω (gultņu izvēlei), efektīvais garums L_eff, nepieciešamā siksnas savilkšana X_e.

Notebook ir parametrizēta — mainot vienu ievades vērtību (motora apgriezienus) un izpildot atkārtoti, visi atvasinātie lielumi tiek pārrēķināti automātiski.
