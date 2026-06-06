# 08 — Flat Belt Drive Calculation (Jupyter / Python)

> Plakansiksnas pārvada aprēķins — mašīnu elementu aprēķins Python vidē
> Flat belt drive design calculation in Python (Jupyter, NumPy)

**Context:** RTU, mašīnu elementu kurss, RMCE01

---

## EN — for GitHub README / EN CV

**Flat Belt Drive Calculation — Mechanical engineering design in Python (Jupyter)**

Designed a flat-belt power transmission connecting two horizontally-mounted parallel shafts. The full design calculation (45 cells: 21 code + 23 markdown derivations) is implemented as a Jupyter notebook with NumPy — every formula written out in LaTeX, then computed.

**Inputs**
- Motor speed n_m = 3000 rpm; power P = 500 W
- Driven pulley speed n_s = 1000 rpm
- Shaft-axis distance C = 1.5 m
- Belt: Habasit A3 general-purpose flat belt (μ = 0.495, t = 3.4 mm, m_i = 3.5 kg/m, F_un = 36 kN/m nominal traction)

**Calculated outputs**
- Driving-pulley angular velocity ω_d = 2πn_m/60
- Belt parameters: type, width, thickness
- Required pre-tension force F_i and centrifugal force F_c
- Tight / slack-side tensions F_1, F_2
- Resultant force F_ω on shafts
- Effective belt length L_eff with wrap-angle correction
- Belt elongation e_0 and required take-up X_e

**Skills demonstrated:** mechanical-element design · belt-drive theory · LaTeX-documented engineering math · NumPy numerical computation · Jupyter as engineering notebook · reproducible calculation workflow (every step parameter-driven, can be re-run with different inputs)

---

## LV — for LV CV

**Plakansiksnas pārvada aprēķins — mašīnu elementu projektēšana Python vidē**

Izstrādāts plakansiksnu pārvada aprēķins divām horizontāli un paralēli novietotām vārpstām. Pilns aprēķins (45 šūnas: 21 kods + 23 markdown ar LaTeX formulām) realizēts Jupyter Notebook ar NumPy.

**Ieejas dati:** motora apgriezieni 3000 rpm, jauda 500 W, dzenamā skriemeļa 1000 rpm, asu attālums 1,5 m. Siksna Habasit A3 (μ = 0,495).

**Aprēķinātie parametri:** siksnas tips, platums un biezums; nepieciešamais spriegošanas spēks F_i; centrbēdzes spēks F_c; siksnas darbojošies spēki F_1, F_2; rezultējošā slodze uz vārpstām F_ω; siksnas efektīvais garums; nepieciešamā siksnas savilkšana X_e.

**Prasmes:** mašīnu elementu projektēšana · siksnu pārvada teorija · inženiermatemātika ar LaTeX dokumentāciju · NumPy aprēķini · Jupyter kā inženierdokuments · atkārtojami parametrizēti aprēķini

---

## Files in this folder
- `Plakansiksnas_parvada_aprekins.ipynb` — main notebook (v3)
- `Plakansiksnas_v31.ipynb` — secondary version

## CV bullet (short, EN)
> *Designed a Habasit A3 flat-belt power transmission (500 W, 3000→1000 rpm, 1.5 m axis distance) as a Jupyter notebook with NumPy — full chain from pre-tension and centrifugal force through wrap-angle correction to required belt take-up.*

## CV bullet (short, LV)
> *Aprēķināts Habasit A3 plakansiksnas pārvads (500 W, 3000→1000 rpm, 1,5 m asu attālums) Jupyter Notebook vidē ar NumPy — no spriegošanas un centrbēdzes spēkiem līdz efektīvajam siksnas garumam un nepieciešamajai savilkšanai.*
