# 🚀 Guia 10: Executando e Debuggando o Climy

Guia prático para rodar, testar e debuggar o Climy.

## 1. Pré-requisitos

Antes de executar, certifique-se de que:

✅ Python 3.10+ instalado
✅ Ambiente virtual criado e ativado
✅ Dependências instaladas
✅ Conexão com internet (para API)

## 2. Executando o Climy

### Método 1: Streamlit Direto

```powershell
# Com ambiente virtual ativado
streamlit run streamlit_app.py
```

**O que acontece:**
- Streamlit inicia servidor local
- Abre navegador em `http://localhost:8501`
- Aplicação fica rodando

**Para parar:**
- Pressione `Ctrl+C` no terminal

### Método 2: Script run.py

```powershell
python run.py
```

**Vantagens:**
- Verifica dependências antes
- Verifica conexão com API
- Informa erros de forma amigável

### Método 3: VS Code (Recomendado)

1. Abra `streamlit_app.py` no VS Code
2. Pressione `Ctrl+F5` (Run without debugging)
3. Ou clique no botão "Run" no topo direito

**Configuração recomendada (.vscode/launch.json):**

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Streamlit",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "console": "integratedTerminal",
            "args": [
                "run",
                "streamlit_app.py"
            ]
        }
    ]
}
```

## 3. Configurando Ambiente

### Arquivo .env (Opcional)

Crie `.env` na raiz do projeto:

```bash
# Configurações do Climy
CLIMY_TIMEOUT=5
CLIMY_CACHE_TTL=300
CLIMY_MAX_CITIES=10
CLIMY_FORECAST_DAYS=7
CLIMY_HOURLY_HOURS=24
CLIMY_LANGUAGE=pt
```

### Verificando se .env Funciona

```python
# Teste rápido
from dotenv import load_dotenv
import os

load_dotenv()

print(f"Timeout: {os.getenv('CLIMY_TIMEOUT')}")
print(f"Cache TTL: {os.getenv('CLIMY_CACHE_TTL')}")
```

## 4. Debugging no VS Code

### Configurando Debugger

Crie `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Streamlit",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "console": "integratedTerminal",
            "args": [
                "run",
                "streamlit_app.py",
                "--server.headless",
                "true"
            ],
            "justMyCode": false
        },
        {
            "name": "Python: Testes",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "console": "integratedTerminal",
            "args": [
                "tests/",
                "-v"
            ]
        }
    ]
}
```

### Usando Breakpoints

1. **Adicionar breakpoint:**
   - Clique na margem esquerda (bolinha vermelha)
   - Ou pressione `F9` na linha desejada

2. **Iniciar debug:**
   - Pressione `F5`
   - Ou clique em "Run and Debug"

3. **Controles:**
   - `F5` - Continua execução
   - `F10` - Step over (próxima linha)
   - `F11` - Step into (entra na função)
   - `Shift+F11` - Step out (sai da função)
   - `Shift+F5` - Para debug

### Exemplo de Debug

```python
# streamlit_app.py
def processar_cidade(cidade: str):
    # breakpoint aqui (F9)
    print(f"Buscando: {cidade}")  # linha 50

    # Ao pressionar F10, executa linha 50
    resultados = search_cities(cidade)  # linha 52

    # Ao pressionar F11, entra em search_cities()
    if resultados:
        return resultados[0]

    return None
```

### Inspecionando Variáveis

**Durante debug:**

1. **Hover:** Passe mouse sobre variável
2. **Run view:** Veja variáveis no painel esquerdo
3. **Debug console:** Digite expressões Python

```python
# No Debug Console, durante execução:
> cidade
'São Paulo'

> len(resultados)
5

> resultados[0]['name']
'São Paulo'

> resultados[0].keys()
dict_keys(['name', 'latitude', 'longitude', ...])
```

## 5. Logging para Debug

### Configurando Logging

```python
# streamlit_app.py
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('climy.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Usar no código
logger.debug(f"Buscando cidade: {cidade}")
logger.info(f"Encontrados {len(resultados)} resultados")
logger.error(f"Erro na API: {e}")
```

### Níveis de Logging

```python
logger.debug("Detalhes para debug")      # Mais verboso
logger.info("Informação geral")          # Padrão
logger.warning("Aviso importante")       # Algo potencialmente problemático
logger.error("Erro ocorreu")             # Erro recuperável
logger.critical("Erro crítico")          # Erro grave
```

### Exemplo Prático

```python
def buscar_previsao(cidade: str):
    logger.debug(f"Iniciando busca para: {cidade}")

    try:
        logger.debug(f"Chamando search_cities('{cidade}')")
        resultados = search_cities(cidade)
        logger.info(f"Encontradas {len(resultados)} cidades")

        if not resultados:
            logger.warning(f"Cidade não encontrada: {cidade}")
            return None

        cidade_escolhida = resultados[0]
        logger.debug(f"Cidade: {cidade_escolhida['name']}")

        logger.debug("Buscando previsão completa...")
        previsao = get_complete_forecast(cidade_escolhida['name'])
        logger.info("Previsão obtida com sucesso!")

        return previsao

    except Exception as e:
        logger.error(f"Erro inesperado: {e}", exc_info=True)
        raise
```

## 6. Testando Manualmente

### Teste 1: Busca de Cidades

```python
# No terminal Python
from services.weather_api import search_cities

resultados = search_cities("São Paulo")
print(f"Encontradas: {len(resultados)} cidades")
print(f"Primeira: {resultados[0]['name']}")
print(f"Lat/Lon: {resultados[0]['latitude']}, {resultados[0]['longitude']}")
```

### Teste 2: Previsão Atual

```python
from services.weather_api import get_weather

weather = get_weather(-23.5505, -46.6333)
print(f"Temperatura: {weather.temperature}°C")
print(f"Vento: {weather.windspeed} km/h")
print(f"Condição: {weather.condition}")
```

### Teste 3: Previsão Completa

```python
from services.weather_api import get_complete_forecast

previsao = get_complete_forecast("São Paulo")
print(f"Cidade: {previsao.cidade}")
print(f"Temperatura atual: {previsao.current.temperature}°C")
print(f"Horas disponíveis: {len(previsao.hourly)}")
print(f"Dias disponíveis: {len(previsao.daily)}")
```

## 7. Rodando Testes Automatizados

### Comandos Básicos

```powershell
# Todos os testes
pytest

# Verbose (mostra detalhes)
pytest -v

# Com cobertura de código
pytest --cov=services --cov=src

# Cobertura + HTML report
pytest --cov=services --cov=src --cov-report=html

# Abrir relatório
start htmlcov\index.html  # Windows
open htmlcov/index.html   # macOS/Linux
```

### Testar Arquivo Específico

```powershell
# Um arquivo de teste
pytest tests/test_weather_api.py -v

# Uma função específica
pytest tests/test_weather_api.py::test_search_cities -v

# Múltiplos arquivos
pytest tests/test_weather_api.py tests/test_config.py -v
```

### Opções Úteis

```powershell
# Parar no primeiro erro
pytest -x

# Mostrar variáveis locais em erro
pytest -l

# Mostrar print() dos testes
pytest -s

# Rodar testes marcados
pytest -m "not slow"

# Rodar só testes que falharam
pytest --lf
```

## 8. Solução de Problemas

### Problema: "ModuleNotFoundError"

**Sintoma:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solução:**
```powershell
# Verifique se ambiente virtual está ativo
# Deve aparecer (venv) no terminal

# Reinstale dependências
pip install -r requirements.txt

# Verifique interpretador do VS Code
# Ctrl+Shift+P → "Python: Select Interpreter"
# Selecione .\venv\Scripts\python.exe
```

### Problema: "Connection Timeout"

**Sintoma:**
```
requests.exceptions.Timeout: HTTPConnectionPool...
```

**Solução:**
```python
# Verifique conexão
import requests
response = requests.get("https://www.google.com", timeout=5)
print(response.status_code)  # 200 = OK

# Aumente timeout (em src/config.py)
TIMEOUT = 10  # Em vez de 5

# Verifique firewall/antivírus
```

### Problema: "Cidade não encontrada"

**Sintoma:**
```
ValueError: Cidade 'xyz' não encontrada
```

**Solução:**
- Verifique ortografia
- Use nome completo (ex: "Rio de Janeiro" não "Rio")
- API pode não ter cidade pequena
- Tente coordenadas diretas (lat, lon)

### Problema: Streamlit não abre navegador

**Solução:**
```powershell
# Rode manualmente
streamlit run streamlit_app.py

# Acesse no navegador
# http://localhost:8501

# Ou force abrir
streamlit run streamlit_app.py --server.headless false
```

### Problema: Cache não atualiza

**Solução:**
```python
# Limpe cache do Streamlit
import streamlit as st
st.cache_data.clear()

# Ou recarregue página (R no navegador)
# Ou reinicie servidor (Ctrl+C, depois streamlit run)
```

## 9. Performance e Otimização

### Medindo Tempo de Execução

```python
import time
from functools import wraps

def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} levou {fim-inicio:.3f}s")
        return resultado
    return wrapper

@medir_tempo
def buscar_previsao(cidade):
    return get_complete_forecast(cidade)

# Uso
buscar_previsao("São Paulo")
# buscar_previsao levou 1.234s
```

### Profile com cProfile

```python
import cProfile
import pstats

def main():
    buscar_previsao("São Paulo")
    buscar_previsao("Rio de Janeiro")
    buscar_previsao("Belo Horizonte")

# Rodar profile
cProfile.run('main()', 'output.prof')

# Analisar resultados
stats = pstats.Stats('output.prof')
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 funções mais lentas
```

## 10. Checklist de Debug

Quando algo der errado:

- [ ] Ambiente virtual está ativo? (`(venv)` no terminal)
- [ ] Dependências instaladas? (`pip list`)
- [ ] Internet funcionando? (`ping google.com`)
- [ ] API no ar? (teste no navegador)
- [ ] .env configurado? (se usar variáveis)
- [ ] Logs verificados? (`climy.log`)
- [ ] Testes passando? (`pytest`)
- [ ] Cache limpo? (reinicie Streamlit)

## 11. Comandos Úteis do Dia a Dia

```powershell
# Iniciar aplicação
streamlit run streamlit_app.py

# Rodar testes
pytest

# Testes com cobertura
pytest --cov --cov-report=html

# Ver logs em tempo real
Get-Content climy.log -Wait -Tail 50  # PowerShell
tail -f climy.log                      # Linux/Mac

# Limpar cache
Remove-Item -Recurse -Force .pytest_cache  # PowerShell
rm -rf .pytest_cache                        # Linux/Mac

# Atualizar dependências
pip install --upgrade -r requirements.txt

# Gerar novo requirements.txt
pip freeze > requirements.txt
```

## 12. Próximos Passos

1. ✅ Execute o Climy com `streamlit run streamlit_app.py`
2. ✅ Adicione breakpoints e debuggue
3. ✅ Rode testes com `pytest`
4. ✅ Estude o **Guia 11** para entender código fonte linha por linha

---

**Próximo guia:** [11-codigo-fonte-climy.md](./11-codigo-fonte-climy.md) - Análise detalhada do código
