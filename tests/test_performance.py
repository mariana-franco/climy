import pytest
import time
from services.weather_api import _score_city, _parse_hourly
from tests.mocks.mock_data import MOCK_CITIES, MOCK_WEATHER_API_RESPONSE


@pytest.mark.benchmark(group="scoring")
def test_performance_city_scoring(benchmark):
    """Mede o tempo médio para pontuar uma cidade."""
    city = MOCK_CITIES[0]
    query = "São Paulo"

    # O benchmark executa a função repetidamente para obter uma média precisa
    result = benchmark(_score_city, city, query)

    assert result > 0
    # Garante que o processamento unitário é ultra rápido (sub-milissegundo)
    assert benchmark.stats.stats.mean < 0.001


@pytest.mark.benchmark(group="parsing")
def test_performance_weather_parsing(benchmark):
    """Mede a eficiência do processamento de 24h de dados (zip e listas)."""
    hourly_data = MOCK_WEATHER_API_RESPONSE["hourly"]

    result = benchmark(_parse_hourly, hourly_data)

    assert len(result) <= 24
    assert benchmark.stats.stats.mean < 0.002


def test_response_time_mocked():
    """Teste simples de latência para garantir que não há sleeps acidentais."""
    start_time = time.perf_counter()

    # Simula o processamento de 100 cidades
    for _ in range(100):
        _score_city(MOCK_CITIES[0], "São Paulo")

    end_time = time.perf_counter()
    duration = end_time - start_time

    # 100 scorings não devem levar mais que 0.1s em uma CPU moderna
    assert duration < 0.1
