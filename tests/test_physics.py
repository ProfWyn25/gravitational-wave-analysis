import pytest

from gwresearch.physics import chirp_mass_solar_masses


def test_chirp_mass_symmetric() -> None:
    assert chirp_mass_solar_masses(30, 40) == pytest.approx(chirp_mass_solar_masses(40, 30))


def test_equal_mass_chirp() -> None:
    mass = 30.0
    assert chirp_mass_solar_masses(mass, mass) == pytest.approx(mass / 2**(1/5))


def test_reject_nonpositive_mass() -> None:
    with pytest.raises(ValueError):
        chirp_mass_solar_masses(0, 30)
