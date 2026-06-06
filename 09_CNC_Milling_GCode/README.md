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
**Machine simulated** HobbyMill (vertical CNC milling machine)
**Workpiece** 150 × 100 × 20 mm

---

## The exercise

Hand-write a complete G-code program from scratch that machines a recognizable pattern — "rocket with stars" — on a 150 × 100 × 20 mm workpiece, using **two cutting tools**:

- **T6** — Ø5 mm cylindrical flat end mill (for the rocket body and contours)
- **T7** — Ø5 mm conical / pointed end mill (for the stars)

The result is verified in CNC Simulator Pro, which renders the toolpath, the workpiece geometry, and the resulting cut surface in 3D.

This is foundational CNC programming — no CAM software involved. Just G-code typed manually, line by line, including all the bookkeeping commands a real CNC machine requires.

---

## The result

![CNC rocket result](images/09_cnc_rocket.png)

*Fig. 1 — Final result in CNC Simulator Pro after all T6 and T7 passes complete: rocket body with windows and wings (T6), five stars (T7). The 3D rendering shows the cut surfaces on the 150 × 100 × 20 mm workpiece.*

---

## The G-code structure

The program has four sections, in order:

### 1. CNC Simulator Pro setup commands

These are `$`-prefixed commands specific to CNC Simulator Pro that define the simulation environment before any G-code runs:

```
(Daniels Skots Lavs RMCE01 3. kurss, 16.11.2025)
$Message "Raķete" 1 0           (Detail name)
$Millimeters                    (Use mm scale)
$Mill                           (Use milling station)
$AddMillPart 170 120 20 0 0 0 0 0 190 218 218 0 1   (Define workpiece)
$DefineMillTool "N:Drill mm" 6 0 5 50 5 15 0        (T6: Ø5 flat end mill)
$DefineMillTool "N:Drill mm" 7 30 5 50 5 15 2       (T7: Ø5 conical end mill)
$ReadTasDefinedTool             (Allow T command to use defined tools)
```

### 2. Initialization

```gcode
G92 Z20            (Tool offset for clearance height)
T6 M6              (Select T6)
M03 S2500 F50      (Spindle on @ 2500 rpm, feed 50 mm/min)

G21                (Metric units - mm)
G90                (Absolute coordinates)
G92 X0 Y0 Z40
G92 Z20            (Zero on the workpiece surface)
```

### 3. T6 — rocket body, window, wings, flame

The body is a closed contour with five corner points, executed with linear `G01` moves at F400:

```gcode
T6 M6
M03 S2500

(Body contour - 5-point silhouette)
G00 X75 Y80 Z2     (rapid to start)
G01 Z-2 F400       (plunge down to depth)
G01 X65 Y60        (top-left)
G01 X65 Y30        (left side)
G01 X70 Y25
G01 X75 Y20        (bottom point)
G01 X80 Y25
G01 X85 Y30        (right side)
G01 X85 Y60        (top-right)
G01 X75 Y80        (back to start)
G01 Z2             (retract)
```

The **window** is a circular arc done with `G02` clockwise circular interpolation:

```gcode
(Window - circular arc)
G00 X80 Y60 Z2
G01 Z-2 F300
G02 X75 Y60 I-5 J0    (G02 with I/J center offset)
G01 Z2
```

Wings (left + right) are symmetric three-point linear contours. The flame at the bottom is a triangular profile.

### 4. T7 — five stars at different positions

```gcode
T7 M6
M03 S2500

(Star 1 - top-left)
G00 X40 Y77 Z2
G01 Z-2 F300
G01 X40 Y83        (vertical line)
G01 Z2
G00 X37 Y80 Z2
G01 Z-2 F300
G01 X43 Y80        (horizontal line - cross with vertical)
G01 Z2
```

Each star is a two-line cross (horizontal + vertical) made with the conical tool — gives the characteristic "star" appearance. Five stars at five positions around 