"""Plot two independently filtered detector strains near GW150914.

Requires public internet access to GWOSC on first run.
This is a first-look demonstration, not a detection or parameter estimate.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries

ROOT = Path(__file__).resolve().parents[2]
GPS_EVENT = 1126259462.4
GPS_START = 1126259446
GPS_END = 1126259478


def main() -> None:
    fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    for ax, detector in zip(axes, ("H1", "L1"), strict=True):
        print(f"Fetching {detector} public strain near GW150914")
        raw = TimeSeries.get(detector, GPS_START, GPS_END)
        # This minimal conditioning follows the GWpy quickstart. It is not
        # sufficient for significance, parameter inference, or timing claims.
        filtered = raw.bandpass(50, 250).whiten()
        segment = filtered.crop(GPS_EVENT - 0.2, GPS_EVENT + 0.4)
        seconds_relative = segment.times.value - GPS_EVENT
        ax.plot(seconds_relative, segment.value, linewidth=0.8)
        ax.set_title(f"{detector}: filtered/whitened detector strain")
        ax.set_ylabel("Whitened strain")
        ax.grid(alpha=0.25)
    axes[-1].set_xlabel("Time relative to GW150914 [s]")
    fig.suptitle("GW150914 first look (not a matched-filter detection)")
    fig.tight_layout()
    destination = ROOT / "figures" / "GW150914_firstlook.png"
    destination.parent.mkdir(exist_ok=True)
    fig.savefig(destination, dpi=200)
    plt.close(fig)
    print(f"Saved {destination}")


if __name__ == "__main__":
    main()
