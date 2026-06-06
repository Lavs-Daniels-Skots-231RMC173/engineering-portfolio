# 02 — Metrology Study: Shaft Detail (M16×1.5)

> Mērīšana, formas un novietojuma noviržu noteikšana un darba rasējuma izstrāde
> Precision measurement, GD&T analysis and engineering drawing of a shaft part

**Context:** RTU studiju projekts, kurs *Vispārīgā metroloģija, papildnodaļas*, RMCE01, 2026
**Group code:** 231RMC173

---

## EN — for GitHub README / EN CV

**Metrology Study — Shaft detail with M16×1.5 thread (2026)**

Full metrological characterization and production drawing of a shaft-type component (Detail #10): a camlock-style head with ring groove, two conical transitions, cylindrical seat, M16×1.5 metric thread and Ø3.5 mm transverse hole. Designed to accept a gear (A=17, B=17 mm), key and retaining ring per RTU catalog spec.

**Instruments & methods**
- **Digital micrometer** (±0.001 mm) — 3 critical seat diameters, 10 measurements each for statistical reliability: Ø17 (gear seat), Ø19 (head profile), Ø23 (axial support)
- **Digital caliper** (±0.01 mm) — secondary linear dimensions
- **Mitutoyo Contracer CV-2100** — thread profile capture, confirmed M16×1.5-6g
- **Mitutoyo Surftest SJ-210** — surface roughness, measured Ra ≈ 1.2 µm
- **Mitutoyo Roundtest RA-120P** — form & runout: roundness 122.6 µm, radial runout 144.5 µm (after datum correction from an initial mis-referenced 454 µm)

**Engineering decisions documented**
- ISO 286-2 transition fit H7/k6 for the gear seat (es = +0.012, ei = +0.001)
- Per-standard form tolerances assigned to drawing: ○ 0.005 / ↗ 0.01 │ A — explicitly *not* copied from the worn real-part measurements
- Seat shortening of thread (30 → 28 mm) to make room for the retaining-ring groove without losing thread length
- Key per DIN 6885 (5×5×16, t1 = 3.0 mm); retaining ring per DIN 471 (d2 = 16.2, m = 1.1, s = 1.0)
- General tolerance fallback: H14/h14/±IT14/2

**Deliverables:** technical report (LV, ~10 pages) + production drawing (1:1, steel C35 LVS EN 10027-1:2005).

**Skills demonstrated:** precision metrology · GD&T (form, position, runout) · ISO/DIN standard selection · tolerance-fit selection · technical drawing per ISO conventions · root-cause correction of measurement error (datum mis-reference)

---

## LV — for LV CV

**Metroloģijas studiju darbs — vārpstveida detaļa ar M16×1,5 vītni (2026)**

Pilna detaļas Nr. 10 metroloģiskā raksturošana un darba rasējuma izstrāde: ātrās savienošanas profila galva ar gredzenveida rievu, divi konusveida pārejas elementi, cilindrisks sēžas posms, metriskā vītne M16×1,5 un šķērsurbums Ø3,5 mm. Detaļa paredzēta zobrata (A=17, B=17 mm), ierievja un sprostgredzena uzstādīšanai pēc RTU kataloga.

**Mērinstrumenti un metodes**
- Digitālais mikrometrs (±0,001 mm) — Ø17, Ø19, Ø23, katrs 10 mērījumi
- Digitālais bīdmērs (±0,01 mm)
- Mitutoyo Contracer CV-2100 — vītnes profils, apstiprināta M16×1,5-6g
- Mitutoyo Surftest SJ-210 — virsmas raupjums Ra ≈ 1,2 µm
- Mitutoyo Roundtest RA-120P — apaļums 122,6 µm, radiālā sišana 144,5 µm (pēc bāzes korekcijas no sākotnējiem 454 µm)

**Inženiertehniskie risinājumi**
- Salāgojums H7/k6 zobrata sēžai (ISO 286-2): Ø17 k6 (+0,012/+0,001)
- Standarta pielaides rasējumā (○ 0,005 / ↗ 0,01 │ A), nevis nolietotās detaļas faktiskās novirzes
- Sēžas pakāpes pagarinājums uz vītnes posma rēķina (30 → 28 mm) sprostgredzena rievai
- Ierievis DIN 6885 (5×5×16), sprostgredzens DIN 471, vītne ISO 965 (6g)

**Prasmes:** precīzā metroloģija · formas un novietojuma novirzes · ISO/DIN standartu izvēle · salāgojumu izvēle · darba rasējuma izstrāde

---

## Files in this project folder
- `Studiju_darbs_detala.docx` — full technical report (LV)
- `Detalas_rasejums.pdf` — production drawing (1:1, steel C35)

## CV bullet (short, EN)
> *Metrological characterization of an M16×1.5 shaft with Mitutoyo Contracer CV-2100, Surftest SJ-210, Roundtest RA-120P, micrometer and caliper; produced ISO-compliant drawing with H7/k6 gear fit and DIN 6885 / DIN 471 standard-element selection.*

## CV bullet (short, LV)
> *Vārpstveida detaļas ar M16×1,5 vītni metroloģiskā raksturošana, izmantojot Mitutoyo Contracer CV-2100, Surftest SJ-210, Roundtest RA-120P, mikrometru un bīdmēru; izstrādāts ISO atbilstošs darba rasējums ar H7/k6 zobrata salāgojumu un DIN 6885 / DIN 471 standarta elementiem.*
