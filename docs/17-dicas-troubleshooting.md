# 🔧 Guia 17: Dicas e Troubleshooting

Solução de problemas comuns que você encontrará no caminho.

## 1. Problemas de Instalação

### "python não é reconhecido"

**Sintoma:**
```powershell
python --version
# 'python' não é reconhecido como um comando
```

**Solução Windows:**

1. **Reinstale Python marcando PATH:**
   - Execute instalador do Python
   - Marque "Add Python to PATH"
   - Instale

2. **Ou adicione manualmente:**
   - Painel de Controle → Sistema
   - Configurações Avançadas → Variáveis de Ambiente
   - Em "Path", adicione:
     ```
     C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python312\
     C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python312\Scripts\
     ```

3. **Reinicie terminal**

### "pip não é reconhecido"

**Solução:**
```powershell
# Tente python -m pip
python -m pip --version

# Ou python3 -m pip
python3 -m pip --version

# Se não funcionar, reinstale Python
```

### "ModuleNotFoundError"

**Sintoma:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solução:**
```powershell
# 1. Verifique se ambiente virtual está ativo
# Deve aparecer (venv) no terminal

# 2. Se não estiver ativo
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux

# 3. Instale dependências
pip install -r requirements.txt

# 4. Verifique interpretador do VS Code
# Ctrl+Shift+P → "Python: Select Interpreter"
# Selecione .\venv\Scripts\python.exe
```

## 2. Problemas com Ambiente Virtual

### Ambiente não ativa

**Windows PowerShell:**
```powershell
# Erro: Activate.ps1 não pode ser carregado
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois ative
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
# Se não ativar
source venv/bin/activate

# Verifique se venv existe
ls -la venv/bin/activate
```

### VS Code não reconhece venv

**Solução:**
1. Feche e reabra VS Code
2. Ctrl+Shift+P → "Python: Select Interpreter"
3. Selecione manualmente:
   - Windows: `.\venv\Scripts\python.exe`
   - macOS/Linux: `./venv/bin/python`

4. Se não aparecer, clique em "Enter interpreter path"
5. Navegue até o arquivo python do venv

## 3. Problemas com Streamlit

### Streamlit não abre navegador

**Solução:**
```powershell
# 1. Rode manualmente
streamlit run streamlit_app.py

# 2. Acesse no navegador
# http://localhost:8501

# 3. Se não abrir, force
streamlit run streamlit_app.py --server.headless false

# 4. Verifique se porta não está em uso
netstat -ano | findstr :8501

# 5. Use outra porta
streamlit run streamlit_app.py --server.port 8502
```

### "Already running on port"

**Solução:**
```powershell
# Mate processo na porta 8501
netstat -ano | findstr :8501
# Anote PID (última coluna)
taskkill /PID <PID> /F

# Ou use outra porta
streamlit run streamlit_app.py --server.port 8502
```

### Streamlit lento

**Solução:**
```python
# 1. Use cache
@st.cache_data
def buscar_dados():
    return get_complete_forecast(cidade)

# 2. Reduza TTL
CACHE_TTL = 60  # Em vez de 300

# 3. Limpe cache
import streamlit as st
st.cache_data.clear()
```

### Alterações não aparecem

**Solução:**
- Pressione `R` no navegador (recarrega)
- Ou `Ctrl+R`
- Ou reinicie servidor (`Ctrl+C`, depois `streamlit run`)

## 4. Problemas com API

### "Connection Timeout"

**Sintoma:**
```
requests.exceptions.Timeout: HTTPConnectionPool...
```

**Solução:**
```python
# 1. Verifique internet
import requests
try:
    response = requests.get("https://www.google.com", timeout=5)
    print("Internet OK")
except:
    print("Sem internet")

# 2. Aumente timeout (src/config.py)
TIMEOUT = 10  # Em vez de 5

# 3. Verifique firewall/antivírus
# Pode estar bloqueando Python

# 4. Teste API no navegador
# https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true
```

### "Cidade não encontrada"

**Sintoma:**
```
ValueError: Cidade 'xyz' não encontrada
```

**Solução:**
- Verifique ortografia
- Use nome completo: "Rio de Janeiro" não "Rio"
- API pode não ter cidades muito pequenas
- Tente coordenadas diretas:
  ```python
  get_weather(-23.5505, -46.6333)  # Em vez de buscar por nome
  ```

### API retornando erro 404

**Solução:**
```python
# Verifique URL
print(f"URL: {BASE_WEATHER_URL}")
# Deve ser: https://api.open-meteo.com/v1/forecast

# Verifique parâmetros
params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True
}
print(f"Params: {params}")

# Teste URL completa no navegador
```

## 5. Problemas com Testes

### "No tests ran"

**Solução:**
```powershell
# 1. Verifique nome dos arquivos
# Devem ser: test_*.py ou *_test.py

# 2. Verifique nome das funções
# Devem ser: test_*()

# 3. Verifique pasta
# Testes devem estar em tests/

# 4. Rode explicitamente
pytest tests/test_meu_arquivo.py -v
```

### Testes falhando sem motivo

**Solução:**
```python
# 1. Adicione prints de debug
def test_meu_codigo():
    print("DEBUG: Iniciando teste")
    resultado = minha_funcao()
    print(f"DEBUG: resultado={resultado}")
    assert resultado == esperado

# 2. Rode com -s para ver prints
pytest tests/test_arquivo.py -v -s

# 3. Verifique se teste é independente
# Não dependa de ordem de execução
```

### "Fixture not found"

**Solução:**
```python
# 1. Verifique se fixture está em conftest.py
# tests/conftest.py

@pytest.fixture
def minha_fixture():
    return dados

# 2. Ou importe no arquivo de teste
from tests.conftest import minha_fixture

# 3. Verifique escopo
@pytest.fixture(scope="module")  # Ou "function", "session"
```

### Cobertura baixa

**Solução:**
```bash
# 1. Veja o que não está coberto
pytest --cov=src --cov-report=term-missing

# 2. Escreva testes para linhas missing
# O relatório mostra números das linhas

# 3. Exclua código que não pode ser testado
# .coveragerc
[run]
omit =
    src/__init__.py
    */__pycache__/*
```

## 6. Problemas de Performance

### Climy lento

**Solução:**
```python
# 1. Use cache do Streamlit
@st.cache_data(ttl=300)
def buscar_previsao(cidade):
    return get_complete_forecast(cidade)

# 2. Reduza dados processados
# Em vez de processar 24h, processe só 12h

# 3. Profile para achar bottleneck
import cProfile
cProfile.run('buscar_previsao("São Paulo")')
```

### Memory leak

**Solução:**
```python
# 1. Verifique variáveis globais
# Evite acumular dados em listas globais

# 2. Limpe cache periodicamente
import streamlit as st
st.cache_data.clear()

# 3. Use generators em vez de listas
def ler_dados():
    for dado in dados_grandes:
        yield dado  # Em vez de return lista
```

## 7. Problemas com Git

### "Please tell me who you are"

**Solução:**
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Arquivos .pyc no Git

**Solução:**
```bash
# 1. Adicione ao .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".pytest_cache/" >> .gitignore

# 2. Remova arquivos já commitados
git rm -r --cached __pycache__/
git commit -m "Remove arquivos de cache"
```

### Conflito de merge

**Solução:**
```bash
# 1. Veja conflito
git status

# 2. Abra arquivo conflitante
# Procure por:
# <<<<<<< HEAD
# Seu código
# =======
# Código deles
# >>>>>>> branch

# 3. Resolva manualmente
# 4. Commit
git add arquivo_resolvido.py
git commit -m "Resolve merge conflict"
```

## 8. Problemas com VS Code

### IntelliSense não funciona

**Solução:**
1. Verifique extensão Python instalada
2. Ctrl+Shift+P → "Python: Select Interpreter"
3. Selecione interpretador correto
4. Recarregue janela: Ctrl+Shift+P → "Developer: Reload Window"

### Formatação não funciona

**Solução:**
```bash
# Instale formatador
pip install black

# Configure VS Code
# settings.json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### Terminal não ativa venv

**Solução:**
```json
# settings.json
{
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe"
}
```

### Debugger não funciona

**Solução:**
1. Verifique launch.json configurado
2. Instale extensão Python
3. Tente debug simples:
   ```python
   x = 5
   print(x)  # Breakpoint aqui
   ```
4. Se não funcionar, reinstale extensão Python

## 9. Problemas com Ollama

### "Connection refused"

**Solução:**
```powershell
# 1. Verifique se Ollama está rodando
ollama list

# 2. Se não, inicie
ollama serve

# 3. No Windows, verifique Services
# Services → Ollama → Start

# 4. Teste conexão
curl http://localhost:11434/api/tags
```

### Modelo muito lento

**Solução:**
```powershell
# 1. Use modelo menor
ollama pull phi3
ollama pull llama3.2:1b

# 2. Use modelo quantizado
ollama pull llama3.2:q4_0

# 3. Verifique se GPU está sendo usada
ollama run llama3.2
# Deve mostrar "Using GPU" se disponível
```

### "Model not found"

**Solução:**
```powershell
# Baixe modelo
ollama pull llama3.2

# Verifique instalados
ollama list

# Se não baixar, verifique internet
# Proxy pode estar bloqueando
```

## 10. Checklist Geral de Troubleshooting

Quando algo der errado:

### Ambiente
- [ ] Python instalado e no PATH?
- [ ] Ambiente virtual ativo? (`(venv)` no terminal)
- [ ] Dependências instaladas? (`pip list`)
- [ ] Interpretador VS Code correto?

### Código
- [ ] Sem erros de sintaxe?
- [ ] Imports corretos?
- [ ] Paths absolutos/relativos certos?

### Execução
- [ ] Internet funcionando?
- [ ] API no ar? (teste no navegador)
- [ ] Portas disponíveis?
- [ ] Permissões de arquivo?

### Testes
- [ ] Nomes de arquivos corretos?
- [ ] Fixtures definidas?
- [ ] Mocks configurados?

### Debug
- [ ] Logs verificados?
- [ ] Prints de debug?
- [ ] Debugger tentado?

## 11. Comandos de Debug Úteis

```powershell
# Verificar Python
python --version
python -c "import sys; print(sys.executable)"

# Verificar pacotes
pip list
pip show streamlit

# Verificar internet
ping google.com
curl https://api.open-meteo.com

# Verificar portas
netstat -ano | findstr :8501

# Limpar cache
Remove-Item -Recurse -Force .pytest_cache
Remove-Item -Recurse -Force __pycache__

# Reinstalar tudo
pip uninstall -y -r requirements.txt
pip install -r requirements.txt

# Verificar arquivo
Get-Content streamlit_app.py -Head 20
Test-Path requirements.txt
```

## 12. Quando Pedir Ajuda

### Antes de perguntar, tenha:

1. **Mensagem de erro completa**
   ```
   Não: "Não funciona"
   Sim: "ModuleNotFoundError: No module named 'streamlit'"
   ```

2. **O que tentou**
   ```
   - Reinstalei dependências
   - Verifiquei PATH
   - Testei em outro terminal
   ```

3. **Código relevante**
   ```python
   # Trecho mínimo que reproduz erro
   import streamlit as st
   st.title("Teste")
   ```

4. **Ambiente**
   ```
   - Windows 11
   - Python 3.12
   - VS Code 1.88
   ```

### Onde pedir ajuda:

- Stack Overflow
- GitHub Issues do projeto
- Discord/Fóruns de Python
- Chat com IA (Ollama, ChatGPT)

## 13. Prevenção de Problemas

### Boas Práticas

```python
# 1. Valide inputs
def processar_temperatura(temp):
    if not isinstance(temp, (int, float)):
        raise TypeError("Temp deve ser numérico")
    if temp < -100 or temp > 60:
        raise ValueError("Temp fora de faixa")
    return temp

# 2. Use logging
import logging
logger = logging.getLogger(__name__)
logger.info("Processando dados")

# 3. Trate erros
try:
    dados = api_call()
except APIError as e:
    logger.error(f"Erro na API: {e}")
    return fallback_data

# 4. Teste antes de commit
pytest
black --check .
flake8
```

## 14. Recursos Úteis

### Documentação

- Python: https://docs.python.org/3/
- Streamlit: https://docs.streamlit.io/
- Open-Meteo: https://open-meteo.com/en/docs
- Pytest: https://docs.pytest.org/

### Ferramentas

- Black (formatador): https://black.readthedocs.io/
- Flake8 (linter): https://flake8.pycqa.org/
- MyPy (type checker): https://mypy.readthedocs.io/

### Comunidades

- Stack Overflow
- r/learnpython
- Python Discord
- GitHub Discussions

## 15. Resumo

| Problema | Solução Rápida |
|----------|----------------|
| Module not found | `pip install -r requirements.txt` |
| python não reconhecido | Reinstale marcando PATH |
| Streamlit não abre | `streamlit run --server.port 8502` |
| Testes não rodam | Verifique nomes `test_*.py` |
| API timeout | Aumente `TIMEOUT` no config |
| Lento | Use `@st.cache_data` |

## Conclusão

Parabéns por chegar até aqui! 🎉

Você agora tem:
- ✅ Fundamentos sólidos de Python
- ✅ Conhecimento do projeto Climy
- ✅ Ferramentas de IA (Ollama)
- ✅ Boas práticas de desenvolvimento
- ✅ Técnicas de teste e debug
- ✅ Solução de problemas comuns

**Continue praticando!** A melhor forma de aprender é:
1. Codando todos os dias
2. Lendo código de outros
3. Contribuindo em projetos
4. Ensinando o que aprendeu

Boa jornada! 🚀

---

**Fim da documentação Climy**

Volte ao [00-index-geral.md](./00-index-geral.md) para navegar por todos os guias.
