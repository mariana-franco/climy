import pytest
from services.weather_api import _validate_coordinates


@pytest.mark.parametrize(
    "lat, lon",
    [
        (0, 0),
        (90, 180),
        (-90, -180),
        (45.5, 90.1),
    ],
)
def test_valid_coordinates(lat, lon):
    """Não deve levantar exceção para valores válidos."""
    _validate_coordinates(lat, lon)


@pytest.mark.parametrize(
    "lat, lon",
    [
        (91, 0),
        (-91, 0),
        (0, 181),
        (0, -181),
    ],
)
def test_invalid_coordinates_raises(lat, lon):
    """Deve levantar ValueError para limites geográficos impossíveis."""
    with pytest.raises(ValueError):
        _validate_coordinates(lat, lon)
