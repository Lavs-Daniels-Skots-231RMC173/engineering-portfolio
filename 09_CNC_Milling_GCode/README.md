<div align="center">

[← back to portfolio](../README.md)

# 🛠️ Project 09

[![Tech1](https://img.shields.io/badge/-G_Code-374151?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-CNC_Simulator_Pro-374151?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-HobbyMill-991B1B?style=for-the-badge)](#)

</div>

---

# 09 — CNC Milling: Hand-Written G-code

> Laboratorijas darbs: CNC frēzes programmēšana G-kodos
> Hand-written G-code program for CNC milling — rocket-with-stars pattern

**Context** RTU studiju projekts · RMCE01 · 3rd year · 16.11.2025
**Software** CNCSimulator Pro
**Machine simulated** HobbyMill (vertical CNC mill)
**Workpiece** 150 × 100 × 20 mm

---

## The exercise

Hand-write a complete G-code program from scratch — "rocket with stars" pattern on 150 × 100 × 20 mm stock — using two cutting tools:
- **T6** — Ø5 mm cylindrical flat end mill (rocket body, contours)
- **T7** — Ø5 mm conical / pointed end mill (stars)

Verified in CNC Simulator Pro — renders toolpath, workpiece, cut surface in 3D.

Foundational CNC programming — no CAM software. Just G-code typed manually, including all bookkeeping commands.

---

## The result

![CNC rocket result](images/09_cnc_rocket.png)

*Fig. 1 — Final result in CNC Simulator Pro: rocket body + window + wings (T6), five stars (T7) on 150 × 100 × 20 mm workpiece*

---

## G-code structure — 4 sections

### 1. CNC Simulator Pro setup

```
(Daniels Skots Lavs RMCE01 3. kurss, 16.11.2025)
$Message "Raķete" 1 0           (detail name)
$Millimeters                    (mm scale)
$Mill                           (milling station)
$AddMillPart 170 120 20 0 0 0 0 0 190 218 218 0 1   (workpiece)
$DefineMillTool "N:Drill mm" 6 0 5 50 5 15 0        (T6: Ø5 flat)
$DefineMillTool "N:Drill mm" 7 30 5 50 5 15 2       (T7: Ø5 conical)
$ReadTasDefinedTool             (allow T command to use defined tools)
```

### 2. Initialization

```gcode
G92 Z20            (clearance height)
T6 M6              (select T6)
M03 S2500 F50      (spindle @ 2500 rpm, feed 50 mm/min)

G21                (mm)
G90                (absolute)
G92 X0 Y0 Z40
G92 Z20            (zero on workpiece surface)
```

### 3. T6 — body + window + wings + flame

Body — closed contour with 5 corner points, linear G01 at F400:

```gcode
T6 M6
M03 S2500

(Body contour)
G00 X75 Y80 Z2
G01 Z-2 F400
G01 X65 Y60
G01 X65 Y30
G01 X70 Y25
G01 X75 Y20
G01 X80 Y25
G01 X85 Y30
G01 X85 Y60
G01 X75 Y80
G01 Z2
```

Window — circular arc with G02:

```gcode
G00 X80 Y60 Z2
G01 Z-2 F300
G02 X75 Y60 I-5 J0     (G02 with I/J center offset)
G01 Z2
```

Wings (L/R symmetric linear contours), flame (triangular profile).

### 4. T7 — five stars

```gcode
T7 M6
M03 S2500

(Star 1)
G00 X40 Y77 Z2
G01 Z-2 F300
G01 X40 Y83          (vertical)
G01 Z2
G00 X37 Y80 Z2
G01 Z-2 F300
G01 X43 Y80          (horizontal — cross)
G01 Z2
```

Each star is a 2-line cross (horizontal + vertical) with the conical tool.

![G-code snippet](images/09_cnc_gcode_snippet.png)

*Fig. 2 — Syntax-highlighted G-code excerpt*

---

## Cutting parameters

| Parameter | Value | Why |
|---|---|---|
| Spindle | 2500 rpm | Standard for Ø5 end mills in soft material |
| Feed (body) | 400 mm/min | Contour milling |
| Feed (window/wings) | 300–350 mm/min | Slower for detail accuracy |
| Depth | 2 mm | Single full-depth pass |
| Workpiece zero | Top-center via G92 X0 Y0 Z40 then G92 Z20 | — |

## G & M codes used

| Code | Meaning |
|---|---|
| `G21` | Metric mm |
| `G90` | Absolute |
| `G92` | Set coordinate system (work offset) |
| `G00` | Rapid traverse |
| `G01` | Linear interpolation (cutting) |
| `G02` | Circular interpolation CW |
| `M03` | Spindle on CW |
| `M06` | Tool change |

---

## Files in this folder

| File | Size | What |
|---|---:|---|
| `CNC_Lab_Daniels_Skots_Lavs.doc` | 84 KB | **Full lab report** with complete G-code + screenshots + tool defs |
| `CNC_Lab_text.txt` | 2.3 KB | Text-only G-code for direct paste into CNC Sim Pro |
| `1001.nc`, `1002.nc` | 99 / 137 KB | Additional CAM-generated G-code samples (Fusion 360, T23 ball end mill) |
| `images/` | — | Figures used in this README |

---

## How to open & run

### View the report
Open `CNC_Lab_Daniels_Skots_Lavs.doc` in Word / LibreOffice.

### Run G-code in CNC Simulator Pro
1. Install **CNC Simulator Pro** (free demo or paid from CNCSimulator.com)
2. Launch → select **Mill** mode → **File → New**
3. Paste G-code from `CNC_Lab_text.txt` into editor
4. Click **Compile** (syntax check)
5. Click **Run** — workpiece rotates in 3D, tool traces path, removes material

Speed up / slow down with slider; pause to inspect a specific move.

---

## Skills demonstrated

- **Manual G-code programming** — complete CNC programs without CAM
- **G-code** — G00/G01/G02 (rapid/linear/circular), G21/G90 (units/mode), G92 (offsets)
- **M-codes** — M03 (spindle on), M06 (tool change)
- **CNC Simulator Pro setup commands** — `$Mill`, `$AddMillPart`, `$DefineMillTool`
- **Tool / feed / speed selection** per operation
- **Multi-tool job sequencing** — T6 contours then T7 detail
- **Work-coordinate system setup** — G92 offsets, zero on workpiece surface

---

## Latvian summary (LV)

CNC frēzes programmēšanas laboratorijas darbs (RTU, 3. kurss, 16.11.2025), kurā raķete ar zvaigznēm tika izstrādāta uz 150 × 100 × 20 mm sagataves, izmantojot manuāli rakstītu G-kodu CNC Simulator Pro vidē.

**Instrumenti:** T6 (Ø5 mm cilindriskā gala frēze ar plakanu galu) korpusam un kontūrai; T7 (Ø5 mm konusveida frēze) piecām zvaigznēm.

**Programmas struktūra:** CNC Simulator Pro definīcijas (`$Mill`, `$AddMillPart`, `$DefineMillTool`); galvene `G21`/`G90`/`G92`; T6 sekcija ar M03 ieslēgšanu, raķetes korpusa lineāro kontūru (G01), G02 apļveida loku logam, spārniem un liesmai; T7 sekcija ar zvaigžņu krustveida līnijām piecās pozīcijās.

Pilns G-koda pirmkods iekļauts `CNC_Lab_text.txt` un detalizētajā atskaitē `CNC_Lab_Daniels_Skots_Lavs.doc`.
