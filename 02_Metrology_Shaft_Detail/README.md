<div align="center">

[← back to portfolio](../README.md)

# 📐 Project 02

[![Tech1](https://img.shields.io/badge/-Mitutoyo-1E40AF?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-GD&T-374151?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-ISO/DIN-1E40AF?style=for-the-badge)](#)

</div>

---

# 02 — Precision Metrology of an M16×1.5 Shaft

> Mērīšana, formas un novietojuma noviržu noteikšana un darba rasējuma izstrāde
> Precision measurement, GD&T characterization and ISO-compliant production drawing

**Context** RTU studiju projekts · course *Vispārīgā metroloģija, papildnodaļas* (General Metrology, advanced topics) · RMCE01 · 2026
**Group ID** 231RMC173
**Reviewers** N. Bulaha

---

## The task

The course brief required:
1. Choose appropriate instruments to capture every dimension of a real worn part (Detail #10)
2. Measure 3 critical seat diameters with **±0.001 mm precision** (10 readings each for statistical confidence)
3. Determine **surface roughness** on at least one critical face
4. Determine **form & position deviations** on at least two surfaces using a roundness tester
5. Produce an **ISO-compliant production drawing** of the *idealized* part — not the worn original — including:
   - Material designation per LVS EN 10027-1:2005
   - Surface roughness symbols (Ra)
   - Form & position tolerances (GD&T)
   - General tolerances fallback (H14/h14/±IT14/2)
6. Specify a manufacturing-grade fit for a standard mating element (gear + key + retaining ring) per the RTU catalog

---

## The part — Detail #10

![Measured part](images/02_met_skice.png)

*Fig. 1 — The actual measured shaft (Detail #10): camlock head, ring groove, M16×1.5 thread, Ø23/Ø19/Ø17 stages. Fitted with a gear (A=17 mm bore, B=17 mm width), Woodruff key and retaining ring per RTU catalog spec.*

The shaft has:
- **Camlock-style profile head** (Ø19) with ring groove for the camlock latch
- **Two conical transitions** between cylindrical stages
- **Cylindrical seat** Ø17 — the **critical** dimension (gear sits here)
- **Cylindrical support flange** Ø23
- **M16×1.5 metric thread** at the right end (24 mm long)
- **Ø3.5 mm transverse cross-hole** through the thread section

Total length: 87 mm.

---

## Instruments and measurement strategy

| Instrument | Used for | Precision | Notes |
|---|---|---|---|
| Digital micrometer (0–25 mm) | Critical Ø17, Ø19, Ø23 — **10 readings each** | ±0.001 mm | Statistical mean to reduce random error |
| Digital caliper (0–150 mm) | All linear / non-critical Ø | ±0.01 mm | Length stages, chamfers, hole position |
| **Mitutoyo Contracer CV-2100** | Thread profile capture | Z = (2.5 + \|0.1H\|) µm | Confirmed pitch p = 1.5 mm → M16×1.5-6g |
| **Mitutoyo Surftest SJ-210** | Surface roughness Ra | 0.001 µm resolution | Measured Ø17 seat: Ra ≈ 1.2 µm |
| **Mitutoyo Roundtest RA-120P** | Roundness + radial runout | 0.001 mm resolution | See "datum-correction lesson" below |

Lab conditions: T = 20 °C throughout.

---

## Critical measurements — 3 seat diameters

Each measured 10 times with the digital micrometer:

| Stage | Mean value (mm) | Function |
|---|---|---|
| Ø17 (gear seat) | 17.005 | Directly mates with gear — H7/k6 fit will be assigned in drawing |
| Ø19 (camlock head) | 18.992 | Mates with retaining mechanism |
| Ø23 (support flange) | 23.012 | Axial gear support; reference surface (datum A) |

The Ø17 readings ranged from 17.000 to 17.009 mm — a spread of 9 µm — illustrating why 10 readings rather than 1 matter at this precision level.

---

## The datum-correction lesson

![Roundness polar diagram](images/02_met_apaluma.png)

*Fig. 2 — Roundness measurement of Ø17 seat (Mitutoyo Roundtest RA-120P): polar diagram — 122.6 µm out-of-round*

The first radial-runout reading came out as **454 µm** — implausibly large. The cause: I had placed the **datum** on a section with significant form deviation itself, so the "runout" measured everything against a wobbly reference.

The correction: re-set the datum to the support flange + camlock head (form deviation 4.1 / 9.9 µm respectively — clean cylindrical references). Runout recomputed to **144.5 µm** — the real value.

![Runout diagram](images/02_met_runout.png)

*Fig. 3 — Radial runout diagram after datum correction: 144.5 µm — the real value of the worn part*

**Takeaway for the drawing:** the worn part's actual numbers (○ 0.123 / ↗ 0.144 │ A) tell us about *this* aging shaft. The new-production drawing will specify tolerances appropriate for the *function* (gear fit), not these measured values.

---

## The production drawing — idealizing for manufacture

![Production drawing](images/met_dra