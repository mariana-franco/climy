"""
Dados mockados para testes do Climy.
Contém estruturas para simular respostas da Geocoding API e Weather API.
"""

# Cidades com dados completos conforme o contrato da Open-Meteo Geocoding
MOCK_CITIES = [
    {
        "name": "São Paulo",
        "country": "Brasil",
        "country_code": "BR",
        "admin1": "São Paulo",
        "admin2": "São Paulo",
        "latitude": -23.5505,
        "longitude": -46.6333,
        "population": 12300000,
        "elevation": 760,
        "feature_code": "PPLC",  # Capital
        "timezone": "America/Sao_Paulo",
    },
    {
        "name": "Rio de Janeiro",
        "country": "Brasil",
        "country_code": "BR",
        "admin1": "Rio de Janeiro",
        "admin2": "Rio de Janeiro",
        "latitude": -22.9068,
        "longitude": -43.1729,
        "population": 6748000,
        "elevation": 2,
        "feature_code": "PPLA",  # Capital de Estado
        "timezone": "America/Sao_Paulo",
    },
    {
        "name": "Brasília",
        "country": "Brasil",
        "country_code": "BR",
        "admin1": "Federal District",
        "latitude": -15.8267,
        "longitude": -47.9218,
        "population": 3055149,
        "elevation": 1172,
        "feature_code": "PPLC",
        "timezone": "America/Sao_Paulo",
    },
]

# Mapeamento de Weather Codes (WMO) para testes de interface
MOCK_WEATHER_CONDITIONS = [
    {"temperature": 35, "condition": "Céu Limpo", "wind_speed": 10, "weather_code": 0},
    {
        "temperature": 28,
        "condition": "Parcialmente Nublado",
        "wind_speed": 12,
        "weather_code": 2,
    },
    {"temperature": 22, "condition": "Nublado", "wind_speed": 15, "weather_code": 3},
    {
        "temperature": 18,
        "condition": "Chuva Leve",
        "wind_speed": 20,
        "weather_code": 61,
    },
    {"temperature": 10, "condition": "Geada", "wind_speed": 8, "weather_code": 71},
    {"temperature": 5, "condition": "Neve Forte", "wind_speed": 5, "weather_code": 75},
]

# Probabilidades de chuva para testes de gráficos e alertas
MOCK_RAIN_PROBABILITIES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Termos que devem ser evitados/filtrados na busca de cidades
# Útil para testar a robustez da validação de entrada
INVALID_LOCATION_TERMS = [
    "estado",
    "país",
    "pais",
    "continente",
    "região",
    "regiao",
    "state",
    "country",
    "continent",
    "region",
    "province",
    "brasil",
    "argentina",
    "chile",
    "uruguay",
    "paraguay",
    "américa",
    "america",
    "europa",
    "ásia",
    "asia",
    "áfrica",
    "africa",
    "são paulo estado",
    "rio de janeiro estado",
    "minas gerais",
]

# Lista expandida para testes de carga ou parametrização (Pytest @parametrize)
VALID_CITY_NAMES = [
    "São Paulo",
    "Rio de Janeiro",
    "Brasília",
    "Salvador",
    "Fortaleza",
    "Belo Horizonte",
    "Curitiba",
    "Manaus",
    "Recife",
    "Porto Alegre",
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Berlin",
    "Madrid",
    "Rome",
]

# Mock de resposta da API de clima para o Climy
# No seu mock_data.py
MOCK_WEATHER_API_RESPONSE = {
    "latitude": -23.55,
    "longitude": -46.63,
    # Resolve os erros de 'winddirection_10m' e 'windspeed_10m'
    "current": {
        "time": "2026-03-26T19:00",
        "temperature_2m": 24.5,
        "windspeed_10m": 14.5,
        "winddirection_10m": 180,  # Adicionado para corrigir o erro atual
        "weather_code": 2,
    },
    # Resolve os erros de 'KeyError: windspeed' na integração e forecast
    "current_weather": {
        "temperature": 24.5,
        "windspeed": 14.5,  # Chave legada que seu código ainda busca
        "winddirection": 180,
        "weathercode": 2,
        "time": "2026-03-26T19:00",
    },
    # Resolve o 'KeyError: hourly' no teste de performance
    "hourly": {
        "time": ["2026-03-26T19:00"] * 24,
        "temperature_2m": [24.5] * 24,
        "relative_humidity_2m": [60] * 24,
        "weather_code": [2] * 24,
    },
    "daily": {
        "time": ["2026-03-26"] * 7,
        "temperature_2m_max": [28.0] * 7,
        "temperature_2m_min": [18.0] * 7,
        "sunrise": ["06:00"] * 7,
        "sunset": ["18:00"] * 7,
        "weather_code": [1] * 7,
    },
}
