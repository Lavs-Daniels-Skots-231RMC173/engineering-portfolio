# 06 — Engineering Drawing Coursework

> Inženiergrafikas studiju darbi — tehniskie rasējumi formātos A4 un A3
> Foundational technical-drawing coursework per ISO/LVS conventions

**Context** RTU studiju projekti · RMCE01 · 2nd year · 2024
**Supervisor** N. Mozga
**Tools** AutoCAD 2024

---

## Why this matters

Engineering drawings are the universal language of mechanical and mechatronic engineering — any part that gets manufactured, inspected, or serviced lives or dies by its drawing. Before doing the more advanced metrology study (project 02) or the RTK manufacturing cell design (project 03), I worked through this foundational coursework to be fluent in:

- **Multi-view orthogonal projection** — first-angle ISO convention
- **Section views** — when to use them, how to indicate cutting planes, hatch patterns
- **Dimensioning** — placement, chain vs base-line, datum reference
- **Title-block discipline** — what goes where on the official LVS frame
- **Material specification** — naming per LVS EN 10027-1:2005
- **Sheet layout** — A4 portrait, A3 landscape, scale selection

The four drawings in this folder cover progressively complex parts so the same techniques are practiced on different geometries.

---

## The four drawings

### 01 — Balsts (Support / Bracket)

![Balsts drawing](images/draw_01_balsts-1.png)

*Fig. 1 — Balsts (Support), A4 portrait, scale 1:1*

A bracket/mounting support component. The first drawing in the sequence — practices the fundamentals:
- Three orthogonal views
- A single section view
- Linear dimensioning chain
- Standard title block (LVS rakstrāmis)

### 02 — Statne (Frame / Stand)

![Statne drawing](images/draw_02_statne-1.png)

*Fig. 2 — Statne (Frame), A3 landscape, scale 1:1*

A more complex frame/stand component. Practices:
- A3 sheet management
- Multiple section views (full + partial)
- Hidden-line conventions
- Hole pattern dimensioning

### 03 — Detail Drawing (A3)

![Detail A3 drawing](images/draw_03_detala-1.png)

*Fig. 3 — Detail (A3), scale 1:1*

Third detail drawing. Practices:
- Advanced section views (offset / aligned)
- Threaded hole notation
- Chamfer and fillet specification
- General tolerance fallback in the title block

### 04 — Task 5 Detail (A4)

![Detail A4 drawing](images/draw_04_uzd5-1.png)

*Fig. 4 — Detail (A4, Task 5), scale 1:1*

The final exercise in the sequence — a small/precise part on A4 portrait. Practices everything previous + tighter dimension placement, surface roughness symbols, and material spec for steel.

---

## Files in this folder

| File | Sheet | What's inside | How to view |
|---|---|---|---|
| `01_Balsts_A4.pdf` | A4 portrait, 1:1 | Bracket/support drawing | PDF viewer |
| `02_Statne_A3.pdf` | A3 landscape, 1:1 | Frame/stand drawing | PDF viewer |
| `03_Detala_A3.pdf` | A3 landscape, 1:1 | Detail drawing | PDF viewer |
| `04_Uzd5_Detala_A4.pdf` | A4 portrait, 1:1 | Task 5 detail drawing | PDF viewer |
| `images/` | — | High-resolution figures used in this README | — |

---

## How to view & print

The PDFs are **production-ready** — they print directly to A4 / A3 at the correct scale on any home or office printer. For physical reference:

- A4 sheets: standard letter-size printer at 100% scale → 1:1 manufacturing reference
- A3 sheets: A3-capable printer at 100% scale; or split-print onto two A4 sheets with overlap

The title blocks contain all standard fields:
- Drawing number
- Part name (Balsts / Statne / Nosaukums)
- Material
- Scale (Mērogs)
- Author (D.S. Lavs)
- Supervisor signatures (N. Mozga + V. Uzvards)
- Date
- Sheet count

---

## Foundation for later work

The conventions practiced here are directly applied in:
- **Project 02 (Metrology Shaft Detail)** — same title block, same dimensioning conventions, same Ra symbols, advanced GD&T
- **Project 03 (RTK 4.7)** — part drawing, operation sketches, layout drawing all use the same ISO/LVS conventions but scaled up to A2

So this folder is the engineering-drawing foundation; projects 02 and 03 are where the technique gets applied to substantive work.

---

## Skills demonstrated

- **ISO / LVS technical drawing conventions**
- **Multi-view orthogonal projection** (first-angle)
- **Section views** — full, partial, offset, aligned
- **Dimensioning and tolerancing** — chain, baseline, general-tolerance fallback
- **Surface roughness symbols** (Ra)
- **Hidden-line and centerline conventions**
- **Title-block discipline** — proper field population for LVS standard frame
- **A4 / A3 sheet layout management**
- **AutoCAD 2024 production workflow** — model space + layout sheets, viewports, printable PDF export

---

## Latvian summary (LV)

Šis ir inženiergrafikas pamatkursa darbu komplekts (RTU, RMCE01, 2024) — četri tehniskie rasējumi formātos A4 un A3, kas praktizē ISO/LVS standartus:

- **Balsts** (A4, 1:1) — atbalsta detaļa
- **Statne** (A3, 1:1) — rāmis/karkasa elements
- **Detaļa** (A3, 1:1) — sarežģītāka komponente ar griezumiem
- **Detaļa 5. uzdevumam** (A4, 1:1) — noslēdzošais vingrinājums

Visi rasējumi seko LVS rakstrāmim, daudzskatu projicēšanai, griezumu un izmēru norādīšanai pēc standartiem. Šis darbu komplekts ir tehniskais pamats vēlākiem projektiem — Detaļas Nr. 10 metroloģijai (projekts 02) un RTK 4.7 kursa darbam (projekts 03).
