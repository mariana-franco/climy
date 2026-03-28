# 📖 Guia 11: Análise do Código Fonte do Climy

Análise detalhada, linha por linha, de cada arquivo do Climy.

## 1. Arquivo: `src/config.py`

### Código Completo

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do arquivo .env


def _int(name: str, default: int) -> int:
    """Converte variável de ambiente para int com fallback."""
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


# --- Metadados ---
APP_NAME = "Climy"
APP_VERSION = "1.0.0"

# --- Caminhos ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- APIs (Endpoints Fixos) ---
BASE_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
BASE_WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# --- Timeouts e Cache ---
TIMEOUT = _int("CLIMY_TIMEOUT", 5)
CACHE_TTL = _int("CLIMY_CACHE_TTL", 300)

# --- Unidades ---
TEMPERATURE_UNIT = "celsius"
WINDSPEED_UNIT = "kmh"

# --- Configurações de exibição ---
MAX_CITIES_RESULTS = _int("CLIMY_MAX_CITIES", 10)
FORECAST_DAYS = _int("CLIMY_FORECAST_DAYS", 7)
HOURLY_FORECAST_HOURS = _int("CLIMY_HOURLY_HOURS", 24)

# --- Idioma ---
API_LANGUAGE = os.getenv("CLIMY_LANGUAGE", "pt")
```

### Análise Linha por Linha

**Imports:**
```python
import os
from pathlib import Path
from dotenv import load_dotenv
```
- `os`: Acessa variáveis de ambiente do sistema
- `Path`: Manipulação moderna de paths (Python 3.4+)
- `load_dotenv`: Carrega arquivo `.env` para variáveis de ambiente

**Função `_int`:**
```python
def _int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default
```
- **Propósito:** Converter variável de ambiente para inteiro
- **Por quê:** Usuário pode não configurar .env, precisa de valor padrão
- **Exceção:** Se valor não for número válido, retorna default

**Metadados:**
```python
APP_NAME = "Climy"
APP_VERSION = "1.0.0"
```
- Constantes em MAIÚSCULO (PEP 8)
- Usado em logs, título, etc.

**BASE_DIR:**
```python
BASE_DIR = Path(__file__).resolve().parent.parent
```
- `__file__`: Path deste arquivo (config.py)
- `.resolve()`: Path absoluto
- `.parent.parent`: Sobe 2 níveis (de src/ para raiz)
- **Uso:** `BASE_DIR / "assets" / "style.css"`

**URLs da API:**
```python
BASE_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
BASE_WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
```
- `geocoding`: Converte nome de cidade → coordenadas
- `forecast`: Busca previsão do tempo

**Configurações Numéricas:**
```python
TIMEOUT = _int("CLIMY_TIMEOUT", 5)
CACHE_TTL = _int("CLIMY_CACHE_TTL", 300)
```
- Tenta ler do `.env`
- Se não existir, usa 5 segundos e 300 segundos (5 min)

## 2. Arquivo: `src/models/weather.py`

### Estrutura Principal

```python
from dataclasses import dataclass
from datetime import datetime, date
from typing import Any

_WMO_CONDITIONS: dict[int, str] = {
    0: "Céu limpo",
    1: "Principalmente limpo",
    # ... mais códigos
}

@dataclass
class Weather:
    temperature: float
    windspeed: float
    winddirection: float
    time: str
    humidity: float | None = None

    @property
    def condition(self) -> str:
        if self.weather_code is not None:
            return _WMO_CONDITIONS.get(self.weather_code, "Tempo variável")
        # Fallback
        if self.temperature >= 30:
            return "Muito Quente"
        return "Tempo ameno"

    @property
    def feels_like(self) -> float:
        # Calcula sensação térmica
        if self.temperature <= 10 and self.windspeed > 4.8:
            # Wind chill formula
            v = self.windspeed**0.16
            return round(13.12 + 0.6215 * self.temperature - ..., 1)
        return round(self.temperature, 1)
```

### Análise

**Dataclass:**
```python
@dataclass
class Weather:
```
- `@dataclass`: Decorator que gera métodos automaticamente
- Gera `__init__`, `__repr__`, `__eq__` automaticamente
- Menos código boilerplate

**Properties:**
```python
@property
def condition(self) -> str:
```
- Acessa como atributo: `weather.condition` (não `weather.condition()`)
- Calcula valor dinamicamente
- Type hint de retorno: `-> str`

**Sensação Térmica:**
```python
if self.temperature <= 10 and self.windspeed > 4.8:
    # Wind Chill (frio + vento)
    v = self.windspeed**0.16
    return round(13.12 + 0.6215 * self.temperature - ..., 1)
```
- Fórmula científica de wind chill
- Só aplica se temp ≤ 10°C E vento > 4.8 km/h
- `round(..., 1)`: 1 casa decimal

## 3. Arquivo: `services/weather_api.py`

### Estrutura

```python
import requests
from typing import Any
from src.config import BASE_GEOCODING_URL, TIMEOUT
from src.models.weather import Weather

class WeatherAPIError(Exception):
    """Erro customizado para API."""
    pass

def search_cities(query: str) -> list[dict]:
    """Busca cidades por nome na API."""
    params = {
        "name": query,
        "count": 10,
        "language": "pt"
    }

    try:
        response = requests.get(
            BASE_GEOCODING_URL,
            params=params,
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException as e:
        raise WeatherAPIError(f"Erro na busca: {e}")
```

### Análise

**Classe de Exceção:**
```python
class WeatherAPIError(Exception):
```
- Exceção customizada
- Permite capturar só erros da API: `except WeatherAPIError:`

**Função `search_cities`:**

1. **Prepara parâmetros:**
   ```python
   params = {
       "name": query,
       "count": 10,
       "language": "pt"
   }
   ```
   - `query`: Nome da cidade digitado
   - `count`: Máximo de resultados
   - `language`: Respostas em português

2. **Faz requisição:**
   ```python
   response = requests.get(
       BASE_GEOCODING_URL,
       params=params,
       timeout=TIMEOUT
   )
   ```
   - GET para URL da API
   - `params`: Adiciona à URL como query string
   - `timeout`: Máximo de segundos antes de falhar

3. **Verifica status:**
   ```python
   response.raise_for_status()
   ```
   - Lança HTTPError se status >= 400
   - 200 = OK, 404 = Não encontrado, 500 = Erro servidor

4. **Retorna resultados:**
   ```python
   return response.json().get("results", [])
   ```
   - `.json()`: Converte resposta para dict Python
   - `.get("results", [])`: Pega chave "results", ou lista vazia

## 4. Arquivo: `streamlit_app.py`

### Estrutura Principal

```python
import streamlit as st
from services.weather_api import search_cities, get_complete_forecast
from src.config import CACHE_TTL

st.set_page_config(
    page_title="Climy",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Climy")

# Input
cidade = st.text_input("Digite uma cidade:")

if cidade:
    # Busca com cache
    @st.cache_data(ttl=CACHE_TTL)
    def buscar(cidade):
        return get_complete_forecast(cidade)

    previsao = buscar(cidade)

    # Exibe dados
    st.metric("Temperatura", f"{previsao.current.temperature}°C")
    st.metric("Vento", f"{previsao.current.windspeed} km/h")
```

### Análise

**Configuração da Página:**
```python
st.set_page_config(
    page_title="Climy",
    page_icon="🌤️",
    layout="centered"
)
```
- Deve ser o primeiro comando Streamlit
- `page_title`: Título da aba do navegador
- `page_icon`: Ícone da aba
- `layout`: "centered" ou "wide"

**Input do Usuário:**
```python
cidade = st.text_input("Digite uma cidade:")
```
- Cria campo de texto
- Retorna valor digitado
- Reexecuta script quando muda

**Cache:**
```python
@st.cache_data(ttl=CACHE_TTL)
def buscar(cidade):
    return get_complete_forecast(cidade)

previsao = buscar(cidade)
```
- `@st.cache_data`: Decorador de cache
- `ttl=CACHE_TTL`: Expira após 300 segundos
- Primeira chamada: Executa função
- Chamadas seguintes (em 5 min): Retorna do cache

**Exibição de Métricas:**
```python
st.metric("Temperatura", f"{previsao.current.temperature}°C")
```
- Widget de métrica do Streamlit
- Mostra valor com destaque
- Opcional: delta para variação

## 5. Diagrama de Fluxo

```
streamlit_app.py (UI)
    ↓
    st.text_input() → Usuário digita "São Paulo"
    ↓
    buscar(cidade) → Chama função com cache
    ↓
services/weather_api.py
    ↓
    search_cities("São Paulo")
    ↓
    requests.get(BASE_GEOCODING_URL, params)
    ↓
    Open-Meteo API
    ↓
    Retorna: [{"name": "São Paulo", "lat": -23.55, ...}]
    ↓
    get_complete_forecast("São Paulo")
    ↓
    requests.get(BASE_WEATHER_URL, params)
    ↓
    Retorna: {current_weather: {...}, hourly: {...}, daily: {...}}
    ↓
src/models/weather.py
    ↓
    Weather(**dados) → Cria objeto Weather
    ↓
    WeatherForecast(cidade, current, hourly, daily)
    ↓
streamlit_app.py
    ↓
    st.metric(), st.line_chart(), st.write()
    ↓
    Exibe no navegador
```

## 6. Pontos Importantes

### 1. Separação de Responsabilidades

- **models:** Só definem estrutura de dados
- **services:** Só integram com APIs externas
- **app:** Só cuida da UI (não tem lógica de negócio)

### 2. Tratamento de Erros

```python
try:
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()
except requests.Timeout:
    raise WeatherAPITimeoutError()
except requests.ConnectionError:
    raise WeatherAPIConnectionError()
```

### 3. Type Hints em Todo Lugar

```python
def search_cities(query: str) -> list[dict]:
def get_weather(lat: float, lon: float) -> Weather:
```

### 4. Docstrings

```python
def search_cities(query: str) -> list[dict]:
    """
    Busca cidades por nome na API Open-Meteo.

    Args:
        query: Nome da cidade para buscar

    Returns:
        Lista de dicts com dados das cidades

    Raises:
        WeatherAPIError: Se API retornar erro
    """
```

## 7. Como Estudar Este Código

### Passo 1: Entenda Models
1. Leia `src/models/weather.py`
2. Crie objetos Weather manualmente
3. Teste properties (`condition`, `feels_like`)

### Passo 2: Entenda Services
1. Leia `services/weather_api.py`
2. Chame funções no terminal Python
3. Veja respostas da API

### Passo 3: Entenda UI
1. Leia `streamlit_app.py`
2. Execute com `streamlit run`
3. Modifique UI e veja mudanças

### Passo 4: Junte Tudo
1. Trace execução completa
2. Use debugger do VS Code
3. Veja fluxo de dados

## Próximos Passos

1. ✅ Leia cada arquivo completo no VS Code
2. ✅ Adicione prints para ver fluxo
3. ✅ Use debugger para step-by-step
4. ✅ Avance para o **Guia 12** (Git e GitHub)

---

**Próximo guia:** [12-git-github.md](./12-git-github.md) - Controle de versão
