"""Tiny pure-Python physics helpers that can be unit-tested without data access."""

from __future__ import annotations


def chirp_mass_solar_masses(m1: float, m2: float) -> float:
    """Binary chirp mass in solar masses, given positive component masses."""
    if m1 <= 0 or m2 <= 0:
        raise ValueError("Component masses must be positive")
    return (m1 * m2) ** (3 / 5) / (m1 + m2) ** (1 / 5)
