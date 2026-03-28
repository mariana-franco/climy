# 🧪 Guia 16: Testes e Debugging Avançado

Aprenda a escrever testes robustos e debuggar como um profissional.

## 1. Por Que Testes?

### Benefícios

✅ **Confiança** - Mudanças não quebram funcionalidades existentes
✅ **Documentação** - Testes mostram como usar o código
✅ **Refatoração** - Permite melhorar código sem medo
✅ **Qualidade** - Encontra bugs antes dos usuários

## 2. Pytest - Framework de Testes

### Instalação

```bash
pip install pytest pytest-cov
```

### Primeiro Teste

```python
# tests/test_soma.py
def test_soma_dois_numeros():
    resultado = 2 + 2
    assert resultado == 4

def test_soma_negativos():
    resultado = -5 + -3
    assert resultado == -8
```

### Rodando Testes

```bash
# Todos os testes
pytest

# Verbose
pytest -v

# Com cobertura
pytest --cov=src --cov=services

# Relatório HTML
pytest --cov-report=html
```

## 3. Escrevendo Testes Eficazes

### 3.1 Nomeclatura

✅ **CERTO:**
```python
def test_search_cities_retorna_lista_para_cidade_valida():
    pass

def test_search_cities_retorna_lista_vazia_para_cidade_invalida():
    pass

def test_get_weather_levanta_erro_para_coordenadas_invalidas():
    pass
```

❌ **ERRADO:**
```python
def test_cidade():  # Muito vago
    pass

def test_weather():  # O que testa?
    pass
```

### 3.2 Estrutura AAA (Arrange-Act-Assert)

```python
def test_calcula_media():
    # Arrange (prepara)
    numeros = [10, 20, 30, 40]

    # Act (age)
    resultado = calcular_media(numeros)

    # Assert (verifica)
    assert resultado == 25.0
```

### 3.3 Teste de Sucesso (Happy Path)

```python
def test_search_cities_cidade_valida():
    """Testa cenário normal."""
    # Arrange
    cidade = "São Paulo"

    # Act
    resultados = search_cities(cidade)

    # Assert
    assert len(resultados) > 0
    assert resultados[0]["name"] == "São Paulo"
    assert "latitude" in resultados[0]
    assert "longitude" in resultados[0]
```

### 3.4 Teste de Erro

```python
def test_search_cities_cidade_invalida():
    """Testa quando cidade não existe."""
    # Arrange
    cidade = "xyz123abc"

    # Act
    resultados = search_cities(cidade)

    # Assert
    assert len(resultados) == 0
    assert isinstance(resultados, list)
```

### 3.5 Teste de Exceção

```python
def test_get_weather_levanta_erro_coordenadas_invalidas():
    """Testa que exceção é levantada."""
    # Arrange
    lat_invalida = 999
    lon_invalida = 999

    # Act & Assert
    with pytest.raises(WeatherAPIError):
        get_weather(lat_invalida, lon_invalida)
```

## 4. Fixtures

Fixtures preparam dados para testes.

### 4.1 Fixtures Simples

```python
# tests/conftest.py
import pytest

@pytest.fixture
def cidade_valida():
    return "São Paulo"

@pytest.fixture
def cidade_invalida():
    return "xyz123abc"

@pytest.fixture
def coordenadas_sao_paulo():
    return (-23.5505, -46.6333)

# tests/test_weather.py
def test_busca_cidade_valida(cidade_valida):
    resultados = search_cities(cidade_valida)
    assert len(resultados) > 0

def test_busca_cidade_invalida(cidade_invalida):
    resultados = search_cities(cidade_invalida)
    assert len(resultados) == 0
```

### 4.2 Fixtures com Setup/Teardown

```python
@pytest.fixture
def arquivo_temporario(tmp_path):
    """Cria arquivo temporário para teste."""
    # Setup
    arquivo = tmp_path / "dados.txt"
    arquivo.write_text("22.5\n25.0\n28.3")

    yield arquivo  # Teste usa aqui

    # Teardown (opcional, tmp_path já limpa)
    # arquivo.unlink()
```

### 4.3 Fixtures Complexas

```python
@pytest.fixture
def mock_weather_data():
    """Dados mockados de clima."""
    return {
        "current_weather": {
            "temperature": 28.5,
            "windspeed": 12.3,
            "winddirection": 180,
            "time": "2026-03-28T10:00"
        },
        "hourly": {
            "time": ["2026-03-28T00:00", "2026-03-28T01:00"],
            "temperature_2m": [22.5, 21.8],
            "relative_humidity_2m": [65, 68]
        },
        "daily": {
            "time": ["2026-03-28", "2026-03-29"],
            "temperature_2m_max": [28.5, 30.1],
            "temperature_2m_min": [18.2, 19.5]
        }
    }

def test_processa_dados(mock_weather_data):
    resultado = processar_dados_api(mock_weather_data)
    assert resultado.temperature == 28.5
```

## 5. Mocking

Mocks simulam comportamentos sem chamar APIs reais.

### 5.1 Mock Simples

```python
from unittest.mock import Mock

def test_com_mock():
    # Cria mock
    api_mock = Mock()
    api_mock.search_cities.return_value = [
        {"name": "São Paulo", "latitude": -23.55}
    ]

    # Usa mock
    resultados = api_mock.search_cities("São Paulo")

    # Assert
    assert len(resultados) == 1
    assert resultados[0]["name"] == "São Paulo"

    # Verifica se foi chamado
    api_mock.search_cities.assert_called_once_with("São Paulo")
```

### 5.2 Patch de Funções

```python
from unittest.mock import patch

@patch('requests.get')
def test_busca_temperatura_com_mock(mock_get):
    """Testa sem chamar API real."""
    # Configura resposta mockada
    mock_response = Mock()
    mock_response.json.return_value = {
        "current_weather": {
            "temperature": 28.5,
            "windspeed": 12.3
        }
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Chama função
    resultado = get_weather(-23.55, -46.63)

    # Assert
    assert resultado.temperature == 28.5

    # Verifica se requests.get foi chamado
    assert mock_get.called
```

### 5.3 Context Manager com Patch

```python
def test_com_patch_context_manager():
    with patch('services.weather_api.requests.get') as mock_get:
        # Configura mock
        mock_get.return_value.json.return_value = {
            "results": [{"name": "Test City"}]
        }

        # Testa
        resultados = search_cities("Test")
        assert len(resultados) == 1
```

## 6. Testes Parametrizados

Testa múltiplos inputs com mesmo código.

```python
import pytest

@pytest.mark.parametrize(
    "temperatura,esperado",
    [
        (30, "Quente"),
        (25, "Agradável"),
        (15, "Frio"),
        (0, "Congelante"),
        (-10, "Congelante"),
    ]
)
def test_classificar_temperatura(temperatura, esperado):
    resultado = classificar_temperatura(temperatura)
    assert resultado == esperado
```

### Múltiplos Parâmetros

```python
@pytest.mark.parametrize(
    "peso,altura,imc_esperado",
    [
        (70, 1.75, 22.86),
        (50, 1.60, 19.53),
        (90, 1.80, 27.78),
    ]
)
def test_calcular_imc(peso, altura, imc_esperado):
    imc = calcular_imc(peso, altura)
    assert abs(imc - imc_esperado) < 0.01
```

## 7. Testes de Integração

### Testando com API Real (Opcional)

```python
import pytest

@pytest.mark.integration  # Marca para pular em testes rápidos
def test_busca_cidade_api_real():
    """Testa com API real (requer internet)."""
    resultados = search_cities("São Paulo")

    assert len(resultados) > 0
    assert resultados[0]["country"] == "BR"

# Pular testes marcados como integration
# pytest -m "not integration"
```

### Testando Banco de Dados

```python
@pytest.fixture
def banco_temporario(tmp_path):
    """Cria banco SQLite temporário."""
    db_path = tmp_path / "teste.db"

    # Cria banco
    conn = sqlite3.connect(db_path)
    criar_tabelas(conn)

    yield conn

    # Limpa
    conn.close()

def test_salvar_cidade(banco_temporario):
    cidade = {"nome": "Test", "lat": -23.55}
    salvar_cidade(banco_temporario, cidade)

    cidades = listar_cidades(banco_temporario)
    assert len(cidades) == 1
```

## 8. Cobertura de Testes

### Gerando Relatório

```bash
# Cobertura de código
pytest --cov=src --cov=services --cov-report=term-missing

# + HTML
pytest --cov=src --cov=services --cov-report=html

# Abrir relatório
start htmlcov\index.html  # Windows
```

### Interpretando Cobertura

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/config.py                25      0   100%
src/models/weather.py        45      2    96%   45-46
services/weather_api.py      80      5    94%   120-125
-------------------------------------------------------
TOTAL                       150      7    95%
```

**Meta:** 80%+ de cobertura

### Forçar Cobertura Mínima

```ini
# pytest.ini
[pytest]
addopts = --cov=src --cov-fail-under=80
```

## 9. Debugging Avançado

### 9.1 Print Debugging (Simples)

```python
def processar_temperaturas(temps):
    print(f"DEBUG: Recebidas {len(temps)} temperaturas")

    for i, temp in enumerate(temps):
        print(f"DEBUG [{i}]: {temp}")

    resultado = sum(temps) / len(temps)
    print(f"DEBUG: Média = {resultado}")

    return resultado
```

### 9.2 Logging (Profissional)

```python
import logging

logger = logging.getLogger(__name__)

def processar_temperaturas(temps):
    logger.debug(f"Processando {len(temps)} temperaturas")

    try:
        for i, temp in enumerate(temps):
            logger.debug(f"Temp {i}: {temp}°C")

        media = sum(temps) / len(temps)
        logger.info(f"Média calculada: {media:.2f}°C")

        return media

    except Exception as e:
        logger.error(f"Erro ao processar: {e}", exc_info=True)
        raise
```

### 9.3 Debugger do Python (pdb)

```python
import pdb

def funcao_complexa(dados):
    resultado = processar(dados)

    pdb.set_trace()  # Breakpoint

    # No prompt do debugger:
    # > dados (vê variável)
    # > n (next line)
    # > s (step into)
    # > c (continue)
    # > q (quit)

    return resultado
```

### 9.4 Debugger do VS Code

**Configuração (.vscode/launch.json):**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug Testes",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "console": "integratedTerminal",
            "args": [
                "tests/",
                "-v",
                "-s"  # Mostra prints
            ],
            "justMyCode": false
        }
    ]
}
```

**Usando:**
1. Adicione breakpoints (F9)
2. Run → Start Debugging (F5)
3. Use controles:
   - F5: Continue
   - F10: Step Over
   - F11: Step Into
   - Shift+F11: Step Out

### 9.5 Debugging de Testes Falhando

```python
def test_falhando():
    resultado = calcular(5, 3)

    # Se falhar, mostra detalhes
    try:
        assert resultado == 8
    except AssertionError:
        print(f"DEBUG: resultado={resultado}, esperado=8")
        print(f"DEBUG: type={type(resultado)}")
        raise  # Relança erro
```

## 10. Testes Específicos para Climy

### 10.1 Testando Modelos

```python
# tests/test_models.py
import pytest
from src.models.weather import Weather

def test_weather_condition():
    weather = Weather(
        temperature=28.5,
        windspeed=12.3,
        winddirection=180,
        time="2026-03-28T10:00",
        weather_code=0
    )

    assert weather.condition == "Céu limpo"
    assert weather.feels_like > 28  # Sensação > temp

def test_weather_feels_like_frio():
    """Testa wind chill em temperaturas baixas."""
    weather = Weather(
        temperature=5,
        windspeed=20,
        winddirection=0,
        time="2026-03-28T10:00"
    )

    # Sensação térmica deve ser menor que temperatura
    assert weather.feels_like < weather.temperature
```

### 10.2 Testando API

```python
# tests/test_weather_api.py
import pytest
from unittest.mock import patch
from services.weather_api import search_cities, get_weather

@patch('services.weather_api.requests.get')
def test_search_cities_sucesso(mock_get):
    """Testa busca de cidades com mock."""
    # Configura mock
    mock_response = Mock()
    mock_response.json.return_value = {
        "results": [
            {"name": "São Paulo", "latitude": -23.55, "longitude": -46.63}
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Testa
    resultados = search_cities("São Paulo")

    # Assert
    assert len(resultados) == 1
    assert resultados[0]["name"] == "São Paulo"
    mock_get.assert_called_once()

@patch('services.weather_api.requests.get')
def test_get_weather_timeout(mock_get):
    """Testa timeout na API."""
    import requests

    mock_get.side_effect = requests.Timeout()

    with pytest.raises(WeatherAPITimeoutError):
        get_weather(-23.55, -46.63)
```

### 10.3 Testando Configurações

```python
# tests/test_config.py
import os
import pytest
from src import config

def test_cache_ttl_valido():
    """Testa que CACHE_TTL é inteiro positivo."""
    assert isinstance(config.CACHE_TTL, int)
    assert config.CACHE_TTL > 0

def test_timeout_valido():
    """Testa que TIMEOUT é inteiro positivo."""
    assert isinstance(config.TIMEOUT, int)
    assert config.TIMEOUT > 0

def test_urls_configuradas():
    """Testa que URLs de API estão configuradas."""
    assert config.BASE_GEOCODING_URL.startswith("https://")
    assert config.BASE_WEATHER_URL.startswith("https://")
```

### 10.4 Testes de Integração

```python
# tests/test_integration.py
import pytest

@pytest.mark.integration
def test_fluxo_completo_busca_cidade():
    """Testa fluxo completo: busca → previsão."""
    # Busca cidade
    cidades = search_cities("São Paulo")
    assert len(cidades) > 0

    cidade = cidades[0]

    # Busca previsão
    previsao = get_complete_forecast(cidade["name"])

    # Verifica dados
    assert previsao.cidade == "São Paulo"
    assert isinstance(previsao.current.temperature, float)
    assert len(previsao.hourly) > 0
    assert len(previsao.daily) > 0
```

## 11. Continuous Integration (CI)

### GitHub Actions

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest -v --cov=src --cov=services --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

## 12. Checklist de Testes

Antes de considerar testes completos:

- [ ] **Happy path** testado
- [ ] **Casos de erro** testados
- [ ] **Edge cases** (valores limites)
- [ ] **Exceções** levantadas corretamente
- [ ] **Fixtures** reutilizáveis
- [ ] **Mocks** onde apropriado
- [ ] **Cobertura** > 80%
- [ ] **Nomes claros** nos testes
- [ ] **Testes rápidos** (< 3s cada)
- [ ] **Testes independentes** (não dependem de ordem)

## 13. Resumo

| Conceito | Exemplo |
|----------|---------|
| Teste simples | `assert x == 5` |
| Fixture | `@pytest.fixture` |
| Mock | `@patch('module.func')` |
| Parametrizado | `@pytest.mark.parametrize` |
| Exceção | `with pytest.raises(Error)` |
| Cobertura | `pytest --cov=src` |
| Debug | `pdb.set_trace()` |

## Próximos Passos

1. ✅ Escreva testes para Climy
2. ✅ Configure cobertura
3. ✅ Use fixtures e mocks
4. ✅ Estude o **Guia 17** (Troubleshooting)

---

**Próximo guia:** [17-dicas-troubleshooting.md](./17-dicas-troubleshooting.md) - Problemas comuns e soluções
