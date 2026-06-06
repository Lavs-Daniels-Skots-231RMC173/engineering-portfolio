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

**Context** RTU · *Vispārīgā metroloģija, papildnodaļas* · RMCE01 · 2026
**Group ID** 231RMC173

---

## The task

1. Choose appropriate instruments for every dimension of a real worn part (Detail #10)
2. Measure 3 critical seat Ø with **±0.001 mm precision** (10 readings each for statistical confidence)
3. Determine **surface roughness** on at least one critical face
4. Determine **form & position deviations** on at least two surfaces with a roundness tester
5. Produce an **ISO-compliant production drawing** of the *idealized* part — material per LVS EN 10027-1:2005, Ra symbols, GD&T tolerances, H14/h14/±IT14/2 general tolerance fallback
6. Specify a manufacturing-grade fit (gear + key + retaining ring) per RTU catalog

---

## The part — Detail #10

![Measured part](images/02_met_skice.png)

*Fig. 1 — The actual shaft: camlock head, ring groove, M16×1.5 thread, Ø23/Ø19/Ø17 stages. Total length 87 mm.*

- Camlock head Ø19 with ring groove
- Two conical transitions
- Cylindrical seat Ø17 — critical (gear sits here)
- Support flange Ø23
- M16×1.5 thread (24 mm long)
- Ø3.5 mm transverse cross-hole

---

## Instruments

| Instrument | Used for | Precision |
|---|---|---|
| Digital micrometer | 3 critical seat Ø × 10 readings each | ±0.001 mm |
| Digital caliper | Linear / non-critical Ø | ±0.01 mm |
| **Mitutoyo Contracer CV-2100** | Thread profile (M16×1.5-6g confirmed) | Z = (2.5 + \|0.1H\|) µm |
| **Mitutoyo Surftest SJ-210** | Surface roughness (Ra ≈ 1.2 µm) | 0.001 µm |
| **Mitutoyo Roundtest RA-120P** | Roundness 122.6 µm; runout 144.5 µm after datum correction (initially 454 µm) | 0.001 mm |

Lab T = 20 °C.

---

## Critical measurements — 3 seat diameters

| Stage | Mean (mm) | Function |
|---|---|---|
| Ø17 (gear seat) | 17.005 | Mates with gear — H7/k6 fit |
| Ø19 (camlock head) | 18.992 | Retaining mechanism mate |
| Ø23 (support flange) | 23.012 | Axial gear support; datum A reference |

Ø17 readings: 17.000 to 17.009 — spread 9 µm. Why 10 readings rather than 1 matters at this precision.

---

## The datum-correction lesson

![Roundness polar diagram](images/02_met_apaluma.png)

*Fig. 2 — Roundness of Ø17 (Mitutoyo Roundtest RA-120P): 122.6 µm out-of-round*

First radial-runout came out as **454 µm** — implausibly large. Cause: datum placed on a section with significant form deviation, so "runout" measured against a wobbly reference.

Correction: re-set datum to the support flange + camlock head (form deviation 4.1 / 9.9 µm — clean cylindrical references). Recomputed runout → **144.5 µm** — the real value.

![Runout diagram](images/02_met_runout.png)

*Fig. 3 — Runout after datum correction: 144.5 µm*

The worn part's actual numbers (○ 0.123 / ↗ 0.144 │ A) describe *this* aging shaft. The new-production drawing specifies tolerances for the *function* (H7/k6 fit), not these measured values.

---

## The production drawing

![Production drawing](images/met_drawing_hi-1.png)

*Fig. 4 — Production drawing (1:1, steel C35 LVS EN 10027-1:2005): H7/k6 gear seat (es = +0.012, ei = +0.001), DIN 6885 key groove (5×5×16, t1 = 3.0), DIN 471 retaining-ring groove (d2 = 16.2, m = 1.1, s = 1.0), Ra 1.6 / 3.2, ○ 0.005 / ↗ 0.01 │ A*

Key engineering decisions:
- **H7/k6 transition fit** on Ø17 (ISO 286-2) — light press without arbor press
- **Form tolerances per standard**: IT6/2 ≈ 0.005 roundness, IT6 ≈ 0.010 runout — match what H7/k6 requires
- **Seat extended to 19.5 mm** — trimmed thread 2 mm to fit retaining-ring groove behind gear
- **Ra 1.6** on functional surfaces (H7/k6 seat + Ø23 support); Ra 3.2 elsewhere
- **Standard elements**: gear (Ø17 H7/k6 seat, B=17 mm); key DIN 6885 (5×5×16, t1=3.0, L=16); retaining ring DIN 471 (d2=16.2, m=1.1, s=1.0); thread ISO 965 (M16×1.5-6g)
- **General tolerance fallback** H14 / h14 / ±IT14/2

Plus manufacturing notes: blunt sharp edges, center holes per DIN 332, thread runout groove for tool exit.

---

## Files in this folder

| File | Size | What |
|---|---:|---|
| `Detalas_rasejums.pdf` | 230 KB | Production drawing PDF (A4, 1:1, full GD&T) |
| `Studiju_darbs_detala.docx` | 1.6 MB | Full study work report (LV) — task, instruments, all 30 raw readings, polar diagrams, datum analysis, fit justification, standard-element specs |
| `images/` | — | Figures used in this README |

---

## How to view the report

Open the `.docx` in Word / LibreOffice / Google Docs. Sections:
1. Task definition + RTU catalog mapping of standard elements
2. Instruments table with precision specs
3. Sketch with numbered measurement points (1–21)
4. Three measurement tables (10 readings × 3 Ø with means)
5. Contracer thread profile capture
6. Roundness + runout — both readings (wrong-datum 454 µm + corrected 144.5 µm)
7. Drawing justification: standard tolerances vs worn actuals
8. Standard-element fit calculations (H7/k6 ISO 286-2)

The drawing prints at 1:1 on A4 — physical reference or CAD source.

---

## Skills demonstrated

- **Precision metrology** — Mitutoyo CV-2100 / SJ-210 / RA-120P + micrometer + caliper
- **GD&T** — roundness, runout, datum selection
- **Statistical measurement** — 10-reading sampling
- **ISO/DIN standard selection** — ISO 286-2 fits, DIN 6885 keys, DIN 471 rings, ISO 965 threads
- **Tolerance-fit selection** — H7/k6 transition fit reasoning
- **Technical drawing per ISO** — title block, views, sections, general-tolerance fallback
- **Root-cause analysis of measurement error** — datum mis-reference catch (454 → 144.5 µm)

---

## Latvian summary (LV)

Vārpstas Detaļa Nr. 10 pilna metroloģiskā raksturošana un darba rasējuma izstrāde. Mērīšanai izmantoti pieci instrumenti — digitālais mikrometrs un bīdmērs, Mitutoyo Contracer CV-2100, Surftest SJ-210, Roundtest RA-120P.

Trīs galvenās sēžas diametrs (Ø17, Ø19, Ø23) izmērīts ar mikrometru ±0,001 mm precizitāti, katrs 10 reizes. Atklāts būtisks moments: pirmā radiālās sišanas mērījuma rezultāts 454 µm bija nereāls, jo bāze tika izvēlēta uz posma ar lielu formas novirzi — pēc korektas bāzes izvēles 144,5 µm.

Darba rasējumā detaļai piešķirtas H7/k6 salāgojuma tolerances (Ø17 k6 +0,012/+0,001 ISO 286-2), formas novirzes pēc standarta (○ 0,005 / ↗ 0,01 │ A), raupjums Ra 1,6 / 3,2, standarta elementi pēc DIN 6885 (ierievis) un DIN 471 (sprostgredzens).
