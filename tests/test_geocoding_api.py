import pytest
from services.weather_api import search_cities


def test_search_cities_filtering(mock_geo_api):
    """Garante que apenas cidades válidas e com população mínima retornem."""
    results = search_cities("São Paulo")

    assert len(results) > 0
    for city in results:
        # Valida se o filtro de população (> 100) e feature_code funcionou
        assert city["population"] >= 100
        assert city["lat"] is not None
        assert isinstance(city["name"], str)


def test_city_scoring_priority(mock_geo_api):
    """Valida se capitais (PPLC) aparecem antes de cidades comuns."""
    results = search_cities("Brasília")
    # No mock, Brasília é PPLC, deve estar no topo
    assert results[0]["feature_code"] == "PPLC"
