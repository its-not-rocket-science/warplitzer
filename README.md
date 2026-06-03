# Warplitzer

**Reconstructing Vinyl's Lost Groove**

Warplitzer is an experimental audio restoration toolkit that combines multiple recordings of the same vinyl record to reconstruct a cleaner, more accurate digital master.

Unlike traditional de-click and de-noise tools that operate on a single recording, Warplitzer exploits the fact that many vinyl playback errors are *not reproducible*. By comparing transfers made under different conditions—including different playback speeds, stylus profiles, cartridges, tracking forces, or even turntables—it becomes possible to identify and suppress defects while preserving the original musical signal.

The long-term goal is to create a restoration system that can recover audio hidden beneath surface noise, clicks, crackle, warp-induced distortion, wow, flutter, and other artifacts using a combination of digital signal processing (DSP), statistical methods, and machine learning.

---

## Why?

Traditional vinyl restoration assumes that a single recording contains all available information.

Warplitzer starts from a different premise:

> Every playback of a vinyl record is a slightly different observation of the same underlying signal.

A click that appears in one transfer may not appear in another.

A warp-induced speed fluctuation may be different on separate passes.

A stylus may track one damaged groove wall better than another.

By treating multiple transfers as independent measurements of the same source, we can potentially reconstruct a version closer to the original mastering than any individual recording.

---

## Core Idea

Imagine recording the same LP:

- Once at 33⅓ RPM
- Once at 45 RPM
- With two different cartridges
- With two different stylus profiles
- On two different turntables

Each recording contains:

```text
Observed Signal =
    Original Music
  + Surface Noise
  + Clicks/Pops
  + Tracking Errors
  + Speed Variations
  + Warp Effects
  + Equipment Colouration
```

The music is common to all recordings.

Most defects are not.

Warplitzer attempts to separate the shared signal from the unshared artifacts.

---

## Potential Sources of Additional Information

### Multi-Speed Transfers

Recording at different speeds changes the temporal characteristics of many defects.

Potential benefits:

- Better detection of clicks and pops
- Improved identification of speed instability
- Enhanced warp correction
- More robust alignment

### Multiple Playback Passes

Repeated recordings provide:

- Statistical confidence
- Outlier rejection
- Noise reduction through averaging

### Multiple Styli

Different stylus shapes contact different portions of the groove:

- Conical
- Elliptical
- Shibata
- MicroLine
- Fine Line

Damage missed by one stylus may be recoverable by another.

### Multiple Channels

Even mono records often contain useful differences between left and right channels that can assist reconstruction.

---

## Planned Processing Pipeline

### Stage 1: Import

Input recordings:

```text
recording_01.wav
recording_02.wav
recording_03.wav
...
```

Supported formats:

- WAV
- FLAC
- AIFF

Preferred format:

- 24-bit / 96 kHz WAV

---

### Stage 2: Speed Normalisation

Convert all recordings to a common reference speed.

Example:

```text
45 RPM -> 33⅓ RPM
78 RPM -> 33⅓ RPM
```

Techniques:

- High-quality resampling
- Pitch correction
- Time correction

---

### Stage 3: Coarse Alignment

Align recordings globally.

Methods:

- Cross-correlation
- FFT correlation
- Phase correlation

Goal:

```text
Sample Accurate Synchronisation
```

---

### Stage 4: Dynamic Alignment

Correct local timing differences caused by:

- Wow
- Flutter
- Off-centre pressings
- Warp

Methods:

- Dynamic Time Warping (DTW)
- Spectral feature matching
- Phase-locked alignment

---

### Stage 5: Defect Detection

Identify:

- Clicks
- Pops
- Crackle
- Groove damage
- Dropouts

Methods:

- Spectral anomaly detection
- Statistical outlier detection
- Machine learning classifiers

---

### Stage 6: Signal Fusion

Combine observations into a single reconstruction.

Potential approaches:

#### Simple Voting

Use the median observation.

#### Confidence Weighting

Choose the signal with the highest estimated quality.

#### Spectral Fusion

Select the best spectral components from each recording.

#### Bayesian Reconstruction

Estimate the most likely original signal.

---

### Stage 7: AI Enhancement

Future capability.

Potential models:

#### Click Detection Networks

Identify transient defects.

#### Source Reconstruction Models

Predict missing audio from surrounding context.

#### Restoration Confidence Models

Estimate reliability of reconstructed regions.

---

## Technical Architecture

```text
warplitzer/
│
├── core/
│   ├── alignment.py
│   ├── fusion.py
│   ├── reconstruction.py
│   └── defects.py
│
├── dsp/
│   ├── fft.py
│   ├── dtw.py
│   ├── filters.py
│   └── resampling.py
│
├── ai/
│   ├── click_detector.py
│   ├── confidence_model.py
│   └── restoration_model.py
│
├── cli/
│   └── main.py
│
├── tests/
│
└── examples/
```

---

## Research Areas

Warplitzer draws inspiration from:

### Astronomy

Combining multiple noisy observations to improve signal quality.

### Computational Photography

Image stacking and super-resolution.

### Radio Astronomy

Interferometric reconstruction from multiple observations.

### Audio Forensics

Evidence reconstruction from degraded recordings.

### Machine Learning

Signal separation and restoration.

---

## Stretch Goals

### Warp Mapping

Estimate physical record warp from audio characteristics.

### Groove Reconstruction

Infer groove geometry from multiple playback observations.

### Virtual Stylus

Combine recordings from different stylus profiles into a synthetic "ideal" stylus.

### Super-Resolution Audio

Recover detail hidden beneath noise through multi-observation fusion.

### Archival Restoration Mode

Target libraries, archives, and preservation projects.

---

## Example Usage

```bash
warplitzer \
    recording_33rpm.wav \
    recording_45rpm.wav \
    --output restored.wav
```

Future:

```bash
warplitzer \
    *.wav \
    --stylus-profile mixed \
    --warp-correction \
    --ai-enhance \
    --output master.wav
```

---

## Current Status

⚠️ Early-stage research project.

Current focus:

- Proof-of-concept alignment
- FFT-based synchronisation
- Dynamic time warping
- Multi-observation fusion
- Click/pop identification

Future focus:

- AI-assisted restoration
- Bayesian signal reconstruction
- Stylus profile modelling
- Warp and wow compensation

---

## Contributing

Contributions are welcome from:

- Audio engineers
- DSP specialists
- Machine learning practitioners
- Vinyl enthusiasts
- Digital archivists
- Signal processing researchers

Particularly valuable are:

- Test recordings
- Multi-speed transfers
- Damaged vinyl samples
- Stylus comparison datasets
- Restoration benchmarks

---

## License

MIT License

---

## Project Motto

> *"Every playback tells a slightly different story. Warplitzer listens to all of them."*
