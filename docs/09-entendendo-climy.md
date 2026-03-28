# 🌤️ Guia 09: Entendendo o Projeto Climy

Este guia explica a arquitetura, estrutura e funcionamento do Climy passo a passo.

## 1. Visão Geral do Projeto

### O Que é o Climy?

Climy é uma **aplicação web de previsão do tempo** desenvolvida com:
- **Python** - Linguagem principal
- **Streamlit** - Framework para interface web
- **Open-Meteo API** - API gratuita de dados climáticos

### Funcionalidades Principais

1. **Busca de Cidades** - Autocomplete com validação
2. **Previsão Atual** - Temperatura, umidade, vento
3. **Previsão Horária** - Próximas 24 horas
4. **Previsão Diária** - Próximos 7 dias
5. **Cache Inteligente** - Reduz chamadas à API

## 2. Estrutura de Pastas

```
climy/
├── docs/                      # Documentação (esta pasta!)
├── services/                  # Integração com APIs externas
│   ├── __init__.py
│   └── weather_api.py         # API da Open-Meteo
│
├── src/                       # Código fonte principal
│   ├── __init__.py
│   ├── config.py              # Configurações globais
│   └── models/                # Modelos de dados
│       ├── __init__.py
│       └── weather.py         # Classes de dados climáticos
│
├── tests/                     # Testes automatizados
│   ├── __init__.py
│   ├── conftest.py            # Configuração do pytest
│   ├── test_*.py              # Arquivos de teste
│   └── mocks/                 # Dados mockados para testes
│       ├── __init__.py
│       └── mock_data.py
│
├── assets/                    # Recursos estáticos
│   └── style.css              # Estilos customizados
│
├── htmlcov/                   # Relatório de cobertura (gerado)
│
├── .env                       # Variáveis de ambiente (opcional)
├── .gitignore                 # Arquivos ignorados pelo Git
├── requirements.txt           # Dependências do projeto
├── pyproject.toml             # Configuração do projeto
├── pytest.ini                 # Configuração do pytest
├── run.py                     # Script de inicialização
└── streamlit_app.py           # Aplicação principal Streamlit
```

## 3. Arquivos Principais

### `requirements.txt` - Dependências

```txt
streamlit==1.28.0       # Framework web
requests==2.31.0        # Cliente HTTP para APIs
python-dotenv==1.0.0    # Variáveis de ambiente
pandas==2.0.3           # Manipulação de dados
pytest==7.4.3           # Framework de testes
pytest-cov==4.1.0       # Cobertura de testes
```

### `src/config.py` - Configurações Globais

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env

# Metadados
APP_NAME = "Climy"
APP_VERSION = "1.0.0"

# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

# APIs (endpoints fixos)
BASE_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
BASE_WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Timeouts e Cache
TIMEOUT = 5          # Segundos para requisição
CACHE_TTL = 300      # Segundos de cache (5 minutos)

# Unidades
TEMPERATURE_UNIT = "celsius"
WINDSPEED_UNIT = "kmh"

# Configurações de exibição
MAX_CITIES_RESULTS = 10
FORECAST_DAYS = 7
HOURLY_FORECAST_HOURS = 24
```

**Como usar:**
```python
from src.config import CACHE_TTL, TIMEOUT

print(f"Cache dura {CACHE_TTL} segundos")
print(f"Timeout de {TIMEOUT} segundos")
```

### `src/models/weather.py` - Modelos de Dados

Define classes para representar dados climáticos:

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Weather:
    """Condições climáticas atuais."""
    temperature: float
    windspeed: float
    winddirection: float
    time: str
    humidity: float | None = None
    weather_code: int | None = None

    @property
    def condition(self) -> str:
        """Retorna condição em português."""
        # Mapeia código WMO para texto
        return _WMO_CONDITIONS.get(self.weather_code, "Variável")

    @property
    def feels_like(self) -> float:
        """Calcula sensação térmica."""
        # Fórmula de wind chill ou heat index
        ...

@dataclass
class DailyForecast:
    """Previsão diária."""
    date: str
    temp_min: float
    temp_max: float
    weather_code: int

@dataclass
class WeatherForecast:
    """Previsão completa."""
    cidade: str
    latitude: float
    longitude: float
    current: Weather
    hourly: list
    daily: list
```

### `services/weather_api.py` - Integração com API

```python
import requests
from src.config import BASE_WEATHER_URL, TIMEOUT
from src.models.weather import Weather, WeatherForecast

def search_cities(query: str) -> list:
    """Busca cidades por nome."""
    params = {
        "name": query,
        "count": 10,
        "language": "pt",
        "format": "json"
    }

    response = requests.get(
        BASE_GEOCODING_URL,
        params=params,
        timeout=TIMEOUT
    )

    return response.json().get("results", [])

def get_weather(lat: float, lon: float) -> Weather:
    """Busca condições atuais."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "America/Sao_Paulo"
    }

    response = requests.get(
        BASE_WEATHER_URL,
        params=params,
        timeout=TIMEOUT
    )

    dados = response.json()["current_weather"]

    return Weather(
        temperature=dados["temperature"],
        windspeed=dados["windspeed"],
        winddirection=dados["winddirection"],
        time=dados["time"]
    )

def get_complete_forecast(cidade: str) -> WeatherForecast:
    """Busca previsão completa (atual + horária + diária)."""
    # 1. Busca coordenadas da cidade
    cidades = search_cities(cidade)
    if not cidades:
        raise ValueError(f"Cidade '{cidade}' não encontrada")

    cidade_escolhida = cidades[0]
    lat = cidade_escolhida["latitude"]
    lon = cidade_escolhida["longitude"]

    # 2. Busca previsão completa
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": ["temperature_2m", "relative_humidity_2m", "weather_code"],
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
        "timezone": "America/Sao_Paulo"
    }

    response = requests.get(BASE_WEATHER_URL, params=params, timeout=TIMEOUT)
    dados = response.json()

    # 3. Retorna objeto estruturado
    return WeatherForecast(
        cidade=cidade_escolhida["name"],
        latitude=lat,
        longitude=lon,
        current=Weather(...),
        hourly=dados["hourly"],
        daily=dados["daily"]
    )
```

### `streamlit_app.py` - Aplicação Principal

```python
import streamlit as st
from services.weather_api import search_cities, get_complete_forecast
from src.config import CACHE_TTL

# Configuração da página
st.set_page_config(
    page_title="Climy",
    page_icon="🌤️",
    layout="centered"
)

# Título
st.title("🌤️ Climy - Previsão do Tempo")

# Barra de busca
cidade = st.text_input("Digite uma cidade:")

if cidade:
    # Busca cidades
    resultados = search_cities(cidade)

    if resultados:
        # Seleciona primeira cidade
        cidade_escolhida = resultados[0]

        # Busca previsão
        previsao = get_complete_forecast(cidade_escolhida["name"])

        # Exibe dados
        st.write(f"📍 {previsao.cidade}")
        st.write(f"🌡️ {previsao.current.temperature}°C")
        st.write(f"💨 Vento: {previsao.current.windspeed} km/h")

        # Gráfico de temperatura horária
        st.line_chart(previsao.hourly["temperature_2m"])
```

## 4. Fluxo de Execução

### Passo a Passo

1. **Usuário abre aplicação**
   ```
   streamlit run streamlit_app.py
   ```

2. **Streamlit carrega página**
   - Executa `streamlit_app.py` do início
   - Configura layout
   - Exibe título e inputs

3. **Usuário digita cidade**
   - `st.text_input()` captura texto
   - Ao pressionar Enter, executa busca

4. **Busca cidades na API**
   ```python
   resultados = search_cities(cidade)
   ```
   - Faz GET em `geocoding-api.open-meteo.com`
   - Retorna lista de cidades matching

5. **Busca previsão completa**
   ```python
   previsao = get_complete_forecast(cidade)
   ```
   - Pega coordenadas (lat, lon)
   - Faz GET em `api.open-meteo.com`
   - Retorna dados atuais + horários + diários

6. **Exibe resultados**
   - Temperatura atual
   - Gráfico horário
   - Previsão de 7 dias

## 5. Sistema de Cache

### Por Que Cache?

- Reduz chamadas à API (limite de requisições)
- Melhora performance (dados em memória)
- Economiza banda

### Como Funciona

```python
import streamlit as st

@st.cache_data(ttl=CACHE_TTL)
def buscar_previsao_cache(cidade: str):
    """Função com cache automático do Streamlit."""
    return get_complete_forecast(cidade)

# Uso
previsao = buscar_previsao_cache("São Paulo")
# Primeira vez: chama API
# Segunda vez (em 5 min): usa cache
```

### TTL (Time To Live)

- `CACHE_TTL = 300` segundos (5 minutos)
- Após 5 minutos, cache expira
- Próxima chamada busca da API novamente

## 6. Tratamento de Erros

### Na API

```python
class WeatherAPIError(Exception):
    """Erro customizado para API."""
    pass

def get_weather(lat, lon):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return parse_response(response)
    except requests.Timeout:
        raise WeatherAPIError("Timeout na API")
    except requests.ConnectionError:
        raise WeatherAPIError("Erro de conexão")
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            raise WeatherAPIError("Local não encontrado")
        raise
```

### Na UI

```python
try:
    previsao = get_complete_forecast(cidade)
    st.success("Dados carregados!")
    exibir_dados(previsao)
except WeatherAPIError as e:
    st.error(f"❌ Erro na API: {e}")
except ValueError as e:
    st.error(f"❌ {e}")
except Exception as e:
    st.error(f"❌ Erro inesperado: {e}")
    st.exception(e)  # Mostra traceback
```

## 7. Testes

### Estrutura de Testes

```python
# tests/test_weather_api.py
import pytest
from services.weather_api import search_cities, get_weather

def test_search_cities():
    """Testa busca de cidades."""
    resultados = search_cities("São Paulo")

    assert len(resultados) > 0
    assert resultados[0]["name"] == "São Paulo"
    assert "latitude" in resultados[0]
    assert "longitude" in resultados[0]

def test_search_cities_vazio():
    """Testa busca que não retorna nada."""
    resultados = search_cities("xyz123abc")
    assert len(resultados) == 0
```

### Rodando Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=services --cov=src

# Relatório HTML
pytest --cov-report=html
# Abre htmlcov/index.html
```

## 8. Variáveis de Ambiente

### Arquivo `.env`

```bash
# Timeout em segundos
CLIMY_TIMEOUT=5

# Cache em segundos
CLIMY_CACHE_TTL=300

# Máximo de cidades na busca
CLIMY_MAX_CITIES=10

# Dias de previsão
CLIMY_FORECAST_DAYS=7

# Idioma da API
CLIMY_LANGUAGE=pt
```

### Carregando no Código

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega .env

timeout = os.getenv("CLIMY_TIMEOUT", "5")  # 5 é default
cache_ttl = int(os.getenv("CLIMY_CACHE_TTL", "300"))
```

## 9. Diagrama de Arquitetura

```
┌─────────────────────────────────────────┐
│         Streamlit (UI)                  │
│  streamlit_app.py                       │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  Input: Cidade                  │   │
│  │  ↓                              │   │
│  │  search_cities()                │   │
│  │  ↓                              │   │
│  │  get_complete_forecast()        │   │
│  │  ↓                              │   │
│  │  Exibir dados                   │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         Services Layer                  │
│  services/weather_api.py                │
│                                         │
│  • search_cities()                      │
│  • get_weather()                        │
│  • get_hourly()                         │
│  • get_daily()                          │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         Models Layer                    │
│  src/models/weather.py                  │
│                                         │
│  • Weather                              │
│  • DailyForecast                        │
│  • WeatherForecast                      │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         Open-Meteo API                  │
│  https://api.open-meteo.com             │
│                                         │
│  • Geocoding API                        │
│  • Forecast API                         │
└─────────────────────────────────────────┘
```

## 10. Como Contribuir

### Adicionando Nova Funcionalidade

1. **Crie branch**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

2. **Implemente no lugar certo**
   - Nova função de API → `services/weather_api.py`
   - Novo modelo → `src/models/`
   - Nova configuração → `src/config.py`
   - UI → `streamlit_app.py`

3. **Escreva testes**
   - Crie `tests/test_nova_funcionalidade.py`
   - Teste casos normais e erros

4. **Rode testes**
   ```bash
   pytest
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "feat: adiciona nova funcionalidade"
   git push
   ```

## 11. Próximos Passos

1. ✅ Leia o **Guia 10** para executar o Climy
2. ✅ Explore o **Guia 11** para entender o código fonte
3. ✅ Estude o **Guia 16** para escrever testes

---

**Próximo guia:** [10-executando-climy.md](./10-executando-climy.md) - Como rodar e debuggar
