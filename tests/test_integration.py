import pytest
import responses
from services.weather_api import (
    search_cities,
    get_complete_forecast,
    get_weather,
    WeatherAPIError,
)
from src.config import BASE_GEOCODING_URL, BASE_WEATHER_URL
from tests.mocks.mock_data import MOCK_CITIES, MOCK_WEATHER_API_RESPONSE


@responses.activate
def test_full_weather_flow_integration():
    """Testa o fluxo completo: Busca de cidade -> Coordenadas -> Previsão."""

    # --- RESET DE CACHE ---
    # Garante que o teste não use dados de execuções anteriores
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()

    # Se get_complete_forecast tiver cache no futuro, limpamos aqui também
    if hasattr(get_complete_forecast, "cache_clear"):
        get_complete_forecast.cache_clear()

    # Mock 1: Geocoding (Busca de Cidade)
    responses.add(
        responses.GET, BASE_GEOCODING_URL, json={"results": MOCK_CITIES}, status=200
    )

    # Mock 2: Weather Forecast (Previsão Completa)
    responses.add(
        responses.GET, BASE_WEATHER_URL, json=MOCK_WEATHER_API_RESPONSE, status=200
    )

    # Passo 1: Buscar a cidade
    cities = search_cities("São Paulo")
    assert len(cities) > 0
    target_city = cities[0]

    # Valida se as coordenadas vieram do Mock de Geocoding
    assert target_city["lat"] == pytest.approx(-23.55, abs=1e-2)
    assert target_city["lon"] == pytest.approx(-46.63, abs=1e-2)

    # Passo 2: Usar as coordenadas da busca para pegar o clima completo
    forecast = get_complete_forecast(target_city["lat"], target_city["lon"])

    # Verificações de Integração (O "Contrato" entre as funções)
    assert forecast.current.temperature == 24.5
    assert len(forecast.daily) > 0
    assert forecast.daily[0].max_temp == 28.0
    # Verifica se a data do Mock está presente (ignorando microssegundos se houver)
    assert "2026-03-26" in forecast.current.time


@responses.activate
def test_integration_error_handling():
    """Testa como o sistema se comporta se a Geocoding funciona mas o Weather falha."""

    # Reset de cache para isolar o teste
    if hasattr(get_weather, "cache_clear"):
        get_weather.cache_clear()

    # Mock 1: Geocoding funciona
    responses.add(
        responses.GET, BASE_GEOCODING_URL, json={"results": MOCK_CITIES}, status=200
    )

    # Mock 2: Simula erro 503 (Serviço Indisponível) no Clima
    responses.add(responses.GET, BASE_WEATHER_URL, status=503)

    cities = search_cities("São Paulo")

    # Verifica se a exceção customizada é lançada corretamente no erro de integração
    with pytest.raises(WeatherAPIError) as excinfo:
        get_complete_forecast(cities[0]["lat"], cities[0]["lon"])

    assert "503" in str(excinfo.value)
