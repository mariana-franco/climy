import pytest
from services.weather_api import validate_city, _validate_coordinates


def test_validate_coordinates_error():
    """Garante que latitudes/longitudes impossíveis lancem erro."""
    with pytest.raises(ValueError):
        _validate_coordinates(100, 0)  # Lat > 90
    with pytest.raises(ValueError):
        _validate_coordinates(0, 200)  # Lon > 180


def test_validate_city_flow(mock_geo_api):
    """Testa a string de retorno para o usuário no dashboard."""
    success, message = validate_city("São Paulo")

    assert success is True
    assert "Cidade encontrada" in message
    assert "12.300.000 hab" in message  # Verificando a formatação de milhar
