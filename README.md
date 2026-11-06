# Gravitational Waves: GW150914

## Long-term research question

How robustly can selected gravitational-wave parameters or signals be recovered as a function of signal-to-noise ratio, waveform assumptions, and signal-processing choices?

First milestone: a visualization, *not* a matched-filter detection or parameter estimate.

## Data source and attribution

- GWOSC: https://gwosc.org/
- Tutorials: https://gwosc.org/tutorials/
- GWpy v4.1.0 quickstart: https://gwpy.readthedocs.io/en/v4.1.0/quickstart/
- GWpy filtering tutorial: https://gwpy.readthedocs.io/en/v4.1.0/examples/signal/gw150914/
- Event: GW150914 (2015-09-14), event GPS time approximately `1126259462.4`.
- GWOSC event data is under CC BY 4.0. Consult its acknowledgement guidance and cite the specific version of the event data used.

Use **corrected** datasets/releases when estimating phase or performing publication-quality work. The GWOSC preliminary v1 **4 kHz data** have a documented downsampling phase error, corrected in v2+. `TimeSeries.get()` discovers publicly available data; for a formal analysis record the actual URLs/release versions and cache the exact datasets.

## First commands

```bash
uv sync
uv run pytest -q
uv run gw-plot
```

Output: `figures/GW150914_firstlook.png`.

This plots filtered and whitened strain from the Hanford (H1) and Livingston (L1) interferometers **separately**, without time alignment or orientation correction. It cannot by itself establish a detection or quantify signal significance. Basic filtering can introduce edge artifacts. Avoid inferring astrophysical parameters from this plot.

## Research milestones

1. **Baseline:** visualize GW150914 public strain from H1 and L1 and document the event/release/version.
2. **Reproduction:** follow and understand GWpy's filtering tutorial; compare raw, bandpassed, whitened, and spectrogram views. Account for filter transients and frequency-dependent noise.
3. **Signals in noise:** generate a known waveform and inject it into representative *off-source* noise. Implement a simple frequency-domain matched filter with a measured power spectral density (PSD).
4. **Validation:** measure signal recovery and false alarms across injections, noise realizations, waveform assumptions, and chosen thresholds. Do not tune preprocessing on a held-out test set.
5. **Cross-check:** compare your implementations to established GWpy/PyCBC results; only then evaluate real event estimates and detector consistency.
6. **Write-up:** state noise assumptions, uncertainties, calibration/data-quality issues, and possible failure modes.

**Potential research angle:** quantify how PSD estimation length and whitening choices affect the mass or chirp recovery of synthetic compact binary signals in realistic open detector noise. Seek an advisor's guidance to make a narrow original question from existing literature.