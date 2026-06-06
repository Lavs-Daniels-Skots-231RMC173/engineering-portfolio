# 11 — FESTO MPS Station — Repair, Documentation & EPLAN Schematics

> Reālas Festo MPS izglītības stacijas remonts, diagnostika un pilnas tehniskās dokumentācijas izveide
> Repair, diagnostics and complete technical documentation of an RTU FESTO MPS education station

**Context:** RTU education FESTO MPS station — needed repair and was undocumented
**Role:** Co-authored repair, built up a clean ID/tagging system, drafted schematics in EPLAN, wrote full documentation
**Why it matters:** This is the closest project to real industrial equipment service — directly mirrors the *Elektronikas regulētājs* role at Latvijas Finieris.

---

## EN — for GitHub README / EN CV

**FESTO MPS Station — Repair, EPLAN Schematics & Full Maintenance Documentation (RTU)**

Hands-on maintenance project on the institute's FESTO Modular Production System: brought a non-working education station back into service, drew up the missing schematics in EPLAN, and authored a complete technical documentation handbook with tagging convention, alarm list, sequence logic and component database.

**System covered — 4 zones**

**Zone 1 — Loading**
- Inductive sensor "PART IN" (SIE-M12S-RS-S-L, PNP, 10–30 VDC)
- Festo DSR-25-180-P semi-rotary pneumatic drive (≤8 bar) for orientation
- End-position sensors (SIE-M8x1-PS-K, SIE-M12x1-PS-K-LED)
- 24 VDC conveyor motor M1
- Optical sensor for parts-on-line limit

**Zone 2 — Processing**
- F-module (tool feed) — pneumatic cylinder with SMT-8-K-LED reed switches on extend/retract
- H-module (cross transmission) — cylinder with reed switches on extend/retract and left/right cross-stroke
- 2V01/2V02 directional valves, 2G01 GRLA flow regulators

**Zone 3 — Pickup head (lift + vacuum gripper)**
- Festo 151270 VAL-1/8-10 vacuum block (6–8 bar)
- Festo DSNU/DNC pneumatic cylinder, magnetic stroke sensors
- Festo VUVG-L10-P53C-T-M5-1P3 solenoid valve (24 VDC)
- Festo DSR-25-180-P intermediate rotary drive
- Burgess U33 limit switches on rotary end-of-travel

**Zone 4 — Unloading** (documented similarly)

**Engineering deliverables**
- **EPLAN electrical schematics** — power, sensor and actuator wiring drawn from scratch (matching the rebuilt station)
- **Pneumatic schematics** (4 sheets) — valve manifold → actuator routing per zone
- **PLC wiring diagrams** — main + subsystem-specific (incl. one I co-prepared with a colleague, Denis Kashin)
- **Technical documentation handbook** (~2 600 words, LV) covering:
  - Zone & class legend, ID convention `[Zone][Class][Number]` (e.g. `2P3.1` = Zone 2, magnetic Position sensor, set 3 channel 1)
  - Per-zone component tables: ID, name, model/series, type, supply, function/location
  - PLC I/O map (sensor → input, valve → output)
  - Pneumatic map (valve → actuator)
  - **Alarm/diagnostic list** ("Nelaimes gadījumi un diagnostika") — failure modes and recovery
  - Cycle sequence and loop logic between zones

**Skills demonstrated:**
industrial equipment service · pneumatic system analysis · electrical/PLC wiring documentation in **EPLAN** · Festo component selection and identification (DSR, DSNU/DNC, VUVG, VAL series) · sensor types (inductive PNP, optical, magnetic reed, limit switches) · structured tagging conventions for plant equipment · failure-mode analysis and alarm-table authoring · cross-discipline collaboration (worked alongside Denis Kashin on PLC subsystems) · technical writing in Latvian

---

## LV — for LV CV

**FESTO MPS stacijas remonts, EPLAN shēmu izstrāde un pilnā tehniskā dokumentācija (RTU)**

Praktisks aprīkojuma apkalpošanas projekts uz institūta FESTO MPS stacijas: bojāta izglītības stacija atjaunota darbībā, no jauna izveidotas elektriskās un PLC shēmas EPLAN vidē, un sagatavota pilnīga tehniskā rokasgrāmata ar marķēšanas sistēmu, trauksmes sarakstu un cilpas loģiku.

**Aptvertās 4 zonas**
- **1. zona — Iekraušana:** induktīvie sensori, Festo DSR-25-180-P rotācijas piedziņa, konveijera motors M1, optiskais sensors
- **2. zona — Apstrāde:** F modulis (instrumenta vads) un H modulis (šķērspārvietošana) ar SMT-8-K-LED niedru slēdžiem; 2V01/2V02 vārsti un 2G01 GRLA droseļvārsti
- **3. zona — Pacelšanas/satvēriena galva:** Festo VAL-1/8-10 vakuuma bloks (151270), DSNU/DNC cilindrs, VUVG-L10 solenoīda vārsts, Burgess U33 robežslēdži
- **4. zona — Izkraušana**

**Inženiertehniskie nodevumi**
- **EPLAN elektriskās shēmas** — barošana, sensori, izpildmehānismi
- **Pneimatiskās shēmas (4 lapas)** — vārstu blokiem un izpildmehānismiem
- **PLC vadu shēmas** — galvenā + apakšsistēma (sadarbībā ar kolēģi Denisu Kašinu)
- **Tehniskās dokumentācijas rokasgrāmata (~2 600 vārdu)** ar ID konvenciju `[Zona][Klase][Nē]`, PLC I/O karti, pneimatikas karti, trauksmes sarakstu un cikla loģiku

**Prasmes:** rūpnieciskā aprīkojuma apkalpošana · pneimatisko sistēmu analīze · elektrisko/PLC shēmu dokumentēšana EPLAN vidē · Festo komponentu identificēšana (DSR, DSNU/DNC, VUVG, VAL sērijas) · strukturēta marķēšanas sistēma · trauksmes tabulu sastādīšana · sadarbība starpdisciplīnos · tehniskā rakstīšana latviešu valodā

---

## Files in this folder
- `FESTO_MPS_full_documentation.docx` — main handbook (~2 600 words, LV)
- `pneumatic_schemes/Pnevmo_1.pdf` … `Pnevmo_4.pdf` — pneumatic schematics, 4 sheets
- `electrical_PLC/Festo_electrical_wiring.pdf` — main electrical wiring
- `electrical_PLC/PLC_main.pdf` — main PLC schematic
- `electrical_PLC/PLC_for_Denis_Kashin.pdf` — collaborated subsystem
- `electrical_PLC/1OP1_4OP1_for_Denis_Kashin.pdf` — sensor sub-document

## CV bullet (short, EN)
> *Returned RTU's FESTO MPS education station to service: drew complete EPLAN electrical and PLC schematics, four pneumatic-system sheets and a full technical handbook with a custom `[Zone][Class][Number]` tagging convention, PLC I/O map and alarm list — the closest hands-on analogue to industrial maintenance work.*

## CV bullet (short, LV)
> *Atjaunota RTU FESTO MPS izglītības stacija darbībā: izstrādātas pilnas EPLAN elektrisko un PLC shēmu, četras pneimatiskās shēmas un pilna tehniskā rokasgrāmata ar pielāgotu `[Zona][Klase][Nē]` marķēšanas sistēmu, PLC I/O karti un trauksmes sarakstu — tuvākais praktiskais analogs rūpnieciskās apkalpes darbam.*
