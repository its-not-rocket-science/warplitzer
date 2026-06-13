# Warplitzer

> Experimental multi-transfer vinyl restoration.  
> Status: early research prototype.

Warplitzer explores a simple idea:

> Every playback of a vinyl record is a slightly different observation of the same underlying signal.

A click may appear in one transfer and not another. A warp may distort one pass differently from the next. A cartridge or stylus may track one damaged groove wall better than another.

Warplitzer treats multiple transfers of the same record as independent observations, then tries to align them and separate the shared musical signal from unshared defects.

## What it is

Warplitzer is an experimental audio restoration toolkit for combining recordings made under different playback conditions, such as:

- 33⅓ RPM and 45 RPM transfers;
- repeated passes at the same speed;
- different cartridges;
- different stylus profiles;
- different tracking forces;
- different turntables.

The long-term goal is to improve restoration of:

- clicks and pops;
- crackle;
- surface noise;
- wow and flutter;
- warp-induced speed variation;
- tracking errors;
- transient defects.

## What it is not

Warplitzer is not currently:

- a polished desktop audio application;
- a VST/AU plugin;
- a replacement for mature tools such as iZotope RX;
- a guaranteed restoration method for every damaged record.

It is an early DSP and machine-learning experiment.

## Core model

```text
Observed transfer =
    original music
  + surface noise
  + clicks and pops
  + tracking errors
  + speed variation
  + warp effects
  + equipment colouration
```

The music should be common across transfers. Many defects should not be.

Warplitzer therefore aims to:

1. resample transfers to a common time base;
2. align them at fine temporal resolution;
3. identify shared versus unshared components;
4. suppress outliers and non-reproducible defects;
5. reconstruct a cleaner master.

## Why multi-speed recording may help

Recording the same disc at different speeds changes the time and frequency behaviour of playback defects.

Potential advantages:

- clicks and pops become easier to identify as outliers;
- speed instability can be estimated from disagreement between passes;
- warp effects can be modelled more explicitly;
- alignment can use redundant information from more than one observation;
- persistent groove information can be separated from pass-specific playback errors.

## Likely technical approach

Warplitzer is expected to combine:

- FFT-based analysis;
- cross-correlation and dynamic time warping;
- phase-aware alignment;
- outlier rejection;
- robust averaging;
- source separation;
- optional neural denoising or masking.

## Repository status

This repository is intentionally small at present. It should be read as an exploratory seed project rather than a finished package.

Next useful milestones:

- define a standard input folder structure for multiple transfers;
- add a reproducible demo using short synthetic audio;
- implement coarse alignment;
- implement fine alignment;
- add click/outlier rejection;
- compare single-transfer restoration against multi-transfer reconstruction.

## Licence

MIT — see `LICENSE`.
