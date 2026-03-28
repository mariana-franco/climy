# 📚 Guia 15: Boas Práticas - PEP 8 e Clean Code

Escreva código Python profissional, legível e sustentável.

## 1. PEP 8 - Guia de Estilo Python

PEP 8 é o guia de estilo oficial do Python.

### 1.1 Nomes de Variáveis e Funções

✅ **CERTO (snake_case):**
```python
nome_usuario = "Maria"
idade_cliente = 25
calcular_media()
buscar_dados_api()
```

❌ **ERRADO:**
```python
NomeUsuario = "Maria"      # PascalCase para variáveis
idadeCliente = 25          # camelCase
calcularMedia()            # camelCase para funções
```

### 1.2 Nomes de Classes

✅ **CERTO (PascalCase):**
```python
class Usuario:
    pass

class CalculadoraCientifica:
    pass

class GerenciadorDeBancoDeDados:
    pass
```

❌ **ERRADO:**
```python
class usuario:              # Minúscula
class Calculadora_cientifica:  # snake_case
```

### 1.3 Constantes

✅ **CERTO (UPPER_CASE):**
```python
MAX_TENTATIVAS = 3
TAMANHO_PAGINA = 50
API_URL = "https://api.exemplo.com"
```

❌ **ERRADO:**
```python
max_tentativas = 3    # Parece variável
Max_Tentativas = 3    # Não é constante
```

### 1.4 Indentação

✅ **CERTO (4 espaços):**
```python
def saudacao():
    if True:
        print("Olá")  # 4 espaços
        if True:
            print("Mundo")  # 8 espaços (2 níveis)
```

❌ **ERRADO:**
```python
def saudacao():
  print("Olá")  # 2 espaços
    if True:
        print("Mundo")  # Mistura de tabs e espaços
```

**Configurar VS Code:**
```json
{
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.detectIndentation": false
}
```

### 1.5 Linhas em Branco

✅ **CERTO:**
```python
class Calculadora:
    """Docstring da classe."""

    def __init__(self):
        self.valor = 0

    def somar(self, x, y):
        """Soma dois números."""
        return x + y

    def subtrair(self, x, y):
        """Subtrai dois números."""
        return x - y


def funcao_fora_da_classe():
    """Função módulo."""
    pass
```

**Regras:**
- 2 linhas em branco entre funções/métodos de topo
- 1 linha em branco entre métodos da mesma classe
- 1 linha em branco dentro de função para separar lógica

### 1.6 Imports

✅ **CERTO:**
```python
# 1. Imports da biblioteca padrão
import os
import sys
from datetime import datetime
from typing import List, Dict

# 2. Imports de bibliotecas de terceiros
import requests
import numpy as np
from pandas import DataFrame

# 3. Imports locais
from src.models import Weather
from services import weather_api

# 4. Imports específicos do módulo atual
from . import utils
from .utils import formatar_temperatura
```

❌ **ERRADO:**
```python
import os, sys, datetime  # Múltiplos imports em uma linha
from .utils import *      # Wildcard import (evite!)
import requests
from src.models import Weather  # Ordem errada
```

### 1.7 Comprimento de Linha

✅ **CERTO (máx 79-99 caracteres):**
```python
# Quebre linhas longas
resultado = (
    "Texto muito longo que não cabe em uma linha "
    "então dividimos em múltiplas linhas"
)

# Ou use parênteses
if (condicao_muito_longa and
    outra_condicao_longa and
    mais_uma_condicao):
    fazer_algo()
```

**Configurar VS Code:**
```json
{
    "editor.rulers": [88],
    "python.formatting.blackArgs": ["--line-length", "88"]
}
```

### 1.8 Espaços em Branco

✅ **CERTO:**
```python
# Operações
x = 5 + 3      # Espaços em volta de operadores
y = a * b - c

# Funções
def calcular(a, b):  # Espaço após vírgula
    return a + b

# Colchetes e parênteses
lista = [1, 2, 3]  # Sem espaço após [
dicionario = {"chave": "valor"}
```

❌ **ERRADO:**
```python
x=5+3              # Sem espaços
def calcular(a,b): # Sem espaço após vírgula
lista = [ 1, 2, 3] # Espaço após [
```

## 2. Clean Code - Código Limpo

### 2.1 Nomes Significativos

✅ **CERTO:**
```python
dias_para_expiracao = 30
temperatura_maxima = 28.5
usuarios_ativos = buscar_usuarios(ativo=True)
```

❌ **ERRADO:**
```python
d = 30                    # O que é d?
temp = 28.5               # temp é ambíguo
u = buscar_usuarios()     # u não diz nada
```

### 2.2 Funções Pequenas

✅ **CERTO:**
```python
def calcular_imc(peso, altura):
    """Calcula Índice de Massa Corporal."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica IMC em categorias."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"

# Uso
imc = calcular_imc(70, 1.75)
classificacao = classificar_imc(imc)
```

❌ **ERRADO:**
```python
def processar_dados():
    # Faz 10 coisas diferentes
    # Lê arquivo
    # Valida dados
    # Calcula IMC
    # Classifica
    # Salva
    # Envia email
    # ... (200 linhas)
    pass
```

### 2.3 Uma Responsabilidade por Função

✅ **CERTO:**
```python
def ler_arquivo(caminho):
    """Lê conteúdo do arquivo."""
    with open(caminho, 'r') as f:
        return f.read()

def validar_dados(dados):
    """Valida estrutura dos dados."""
    return 'temperatura' in dados and 'umidade' in dados

def salvar_no_banco(dados):
    """Salva dados no banco."""
    # lógica de banco
    pass

# Uso
dados = ler_arquivo("dados.txt")
if validar_dados(dados):
    salvar_no_banco(dados)
```

### 2.4 Comentários Úteis

✅ **CERTO (comentário explica PORQUÊ):**
```python
# Usamos 5 segundos de timeout para evitar travar UI
TIMEOUT = 5

# API limita a 100 requisições/hora, então usamos cache
CACHE_TTL = 300
```

❌ **ERRADO (comentário óbvio):**
```python
# Soma a e b
resultado = a + b

# Abre arquivo
arquivo = open("dados.txt")

# Retorna verdadeiro
return True
```

### 2.5 Docstrings

✅ **CERTO:**
```python
def buscar_temperatura(cidade: str, timeout: int = 5) -> dict:
    """
    Busca temperatura atual na API Open-Meteo.

    Args:
        cidade: Nome da cidade para busca
        timeout: Timeout da requisição em segundos (default: 5)

    Returns:
        dict com dados climáticos contendo:
        - temperatura: float
        - umidade: float
        - vento: float

    Raises:
        WeatherAPIError: Se API retornar erro
        TimeoutError: Se requisição exceder timeout

    Example:
        >>> buscar_temperatura("São Paulo")
        {'temperatura': 28.5, 'umidade': 65}
    """
    pass
```

## 3. Type Hints (Dicas de Tipo)

### 3.1 Básico

✅ **CERTO:**
```python
def saudacao(nome: str) -> str:
    return f"Olá, {nome}"

def soma(a: int, b: int) -> int:
    return a + b

def calcular_media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)
```

### 3.2 Tipos Complexos

```python
from typing import List, Dict, Optional, Union, Tuple

def buscar_usuario(id: int) -> Optional[dict]:
    """Retorna dict ou None se não encontrar."""
    pass

def processar_dados(
    dados: List[dict]
) -> Dict[str, Union[int, float]]:
    """Processa lista de dicts."""
    pass

def retornar_multiplas_coisas() -> Tuple[str, int, float]:
    """Retorna múltiplos valores."""
    return "texto", 42, 3.14
```

### 3.3 Dataclasses com Type Hints

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Weather:
    """Dados climáticos."""
    temperature: float
    umidade: float
    vento: float
    condicao: Optional[str] = None
    pressao: Optional[float] = None
```

## 4. Tratamento de Erros

### 4.1 Capture Erros Específicos

✅ **CERTO:**
```python
try:
    resultado = int(valor) / divisor
except ValueError:
    print("Valor deve ser numérico")
except ZeroDivisionError:
    print("Não divida por zero")
```

❌ **ERRADO:**
```python
try:
    resultado = int(valor) / divisor
except:  # Captura TUDO, até KeyboardInterrupt
    print("Erro")
```

### 4.2 Use Exceções Customizadas

```python
class ClimyError(Exception):
    """Erro base para Climy."""
    pass

class WeatherAPIError(ClimyError):
    """Erro na API de clima."""
    pass

class ValidationError(ClimyError):
    """Erro de validação."""
    pass

# Uso
def buscar_cidade(nome: str) -> dict:
    if not nome:
        raise ValidationError("Nome não pode ser vazio")

    try:
        return api_search(nome)
    except requests.RequestException as e:
        raise WeatherAPIError(f"Erro na API: {e}")
```

## 5. Boas Práticas Específicas para Climy

### 5.1 Configurações

✅ **CERTO:**
```python
# src/config.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Use variáveis de ambiente com fallback
TIMEOUT = int(os.getenv("CLIMY_TIMEOUT", "5"))
CACHE_TTL = int(os.getenv("CLIMY_CACHE_TTL", "300"))

# Constantes em maiúsculo
MAX_CITIES_RESULTS = 10
FORECAST_DAYS = 7
```

### 5.2 Nomes de Funções

✅ **CERTO:**
```python
# services/weather_api.py
def search_cities(query: str) -> List[dict]:
    """Busca cidades por nome."""
    pass

def get_weather(lat: float, lon: float) -> Weather:
    """Busca condições atuais."""
    pass

def get_complete_forecast(cidade: str) -> WeatherForecast:
    """Busca previsão completa."""
    pass
```

### 5.3 Estrutura de Pastas

```
climy/
├── services/          # Integração externa (APIs)
├── src/               # Lógica de negócio
│   ├── models/        # Modelos de dados
│   └── utils/         # Utilitários
├── tests/             # Testes
└── streamlit_app.py   # UI (apenas UI)
```

**Regra:** UI não deve ter lógica de negócio!

❌ **ERRADO:**
```python
# streamlit_app.py
def calcular_sensacao_termica(temp, umidade):
    # Lógica de negócio na UI!
    pass
```

✅ **CERTO:**
```python
# src/models/weather.py
class Weather:
    @property
    def feels_like(self) -> float:
        # Lógica no modelo
        pass

# streamlit_app.py
st.write(f"Sensação: {weather.feels_like}°C")  # Só exibe
```

## 6. Testes

### 6.1 Nomeie Testes Claramente

✅ **CERTO:**
```python
def test_search_cities_retorna_lista_vazia_para_nome_invalido():
    resultados = search_cities("xyz123abc")
    assert len(resultados) == 0

def test_get_weather_retorna_temperatura_valida():
    weather = get_weather(-23.55, -46.63)
    assert isinstance(weather.temperature, float)
```

### 6.2 Use Fixtures

```python
# tests/conftest.py
import pytest

@pytest.fixture
def cidade_valida():
    return "São Paulo"

@pytest.fixture
def coordenadas_sao_paulo():
    return (-23.5505, -46.6333)

# tests/test_weather.py
def test_busca_cidade(cidade_valida):
    resultados = search_cities(cidade_valida)
    assert len(resultados) > 0
```

## 7. Performance

### 7.1 Use Generators para Listas Grandes

✅ **CERTO:**
```python
# Generator (econômico memória)
def ler_temperaturas(arquivo):
    with open(arquivo) as f:
        for linha in f:
            yield float(linha.strip())

# Uso
for temp in ler_temperaturas("dados.txt"):
    processar(temp)
```

❌ **ERRADO:**
```python
# Lista (carrega tudo na memória)
def ler_temperaturas(arquivo):
    with open(arquivo) as f:
        return [float(linha.strip()) for linha in f]
```

### 7.2 Cache Resultados

```python
import streamlit as st

@st.cache_data(ttl=300)
def buscar_previsao(cidade: str):
    """Cache por 5 minutos."""
    return get_complete_forecast(cidade)
```

## 8. Checklist de Code Review

Antes de commitar, verifique:

### Código
- [ ] Segue PEP 8?
- [ ] Nomes significativos?
- [ ] Funções pequenas (< 50 linhas)?
- [ ] Type hints adicionados?
- [ ] Docstrings completas?

### Erros
- [ ] Tratamento de erros adequado?
- [ ] Exceções específicas?
- [ ] Logging em vez de prints?

### Testes
- [ ] Testes escritos?
- [ ] Casos de erro cobertos?
- [ ] Edge cases testados?

### Performance
- [ ] Cache onde apropriado?
- [ ] Sem loops desnecessários?
- [ ] Memory leaks?

## 9. Ferramentas

### Auto-Formatação

```bash
# Black (formatador)
pip install black
black .

# isort (organiza imports)
pip install isort
isort .

# No VS Code, configure format on save
```

### Linters

```bash
# Flake8 (verifica PEP 8)
pip install flake8
flake8 .

# Pylint (análise completa)
pip install pylint
pylint src/

# MyPy (verifica type hints)
pip install mypy
mypy src/
```

### Pre-commit Hooks

```bash
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
```

## 10. Resumo

| Prática | Exemplo |
|---------|---------|
| snake_case | `nome_variavel` |
| PascalCase | `NomeClasse` |
| UPPER_CASE | `CONSTANTE` |
| Indentação | 4 espaços |
| Linha máx | 88 caracteres |
| Docstring | Google style |
| Type hints | `def f(x: int) -> str:` |
| Testes | `test_[funcao]_[caso]` |

## Próximos Passos

1. ✅ Configure auto-format no VS Code
2. ✅ Rode `black .` no Climy
3. ✅ Adicione type hints onde faltar
4. ✅ Estude o **Guia 16** (Testes com Pytest)

---

**Próximo guia:** [16-testing-debugging.md](./16-testing-debugging.md) - Testes unitários e debugging avançado
