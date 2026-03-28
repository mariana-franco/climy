# 🐍 Guia 01: Instalação e Configuração do Ambiente

Neste guia, você vai aprender a configurar todo o ambiente necessário para trabalhar com Python e o projeto Climy.

## 📋 Pré-requisitos

- Computador com Windows, macOS ou Linux
- Acesso à internet para downloads
- Espaço em disco: ~500MB (Python + dependências)

## 1. Instalando o Python

### Windows

1. **Baixe o Python:**
   - Acesse https://www.python.org/downloads/
   - Clique em "Download Python 3.12.x" (versão mais recente)

2. **Execute o instalador:**
   - ⚠️ **IMPORTANTE:** Marque a opção **"Add Python to PATH"** antes de instalar!
   - Clique em "Install Now"
   - Aguarde a instalação completar

3. **Verifique a instalação:**
   ```powershell
   python --version
   # Deve mostrar: Python 3.12.x
   ```

### macOS

1. **Instale via Homebrew (recomendado):**
   ```bash
   # Instale o Homebrew primeiro se não tiver
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Instale o Python
   brew install python
   ```

2. **Verifique a instalação:**
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

## 2. Instalando o VS Code

1. **Baixe o VS Code:**
   - Acesse https://code.visualstudio.com/
   - Baixe a versão para seu sistema operacional
   - Instale com as configurações padrão

2. **Instale as extensões recomendadas:**
   - Abra o VS Code
   - Vá para Extensions (Ctrl+Shift+X)
   - Instale:
     - **Python** (Microsoft)
     - **Pylance** (Microsoft)
     - **Python Indent** (Kevin Rose)
     - **GitLens** (GitKraken)

## 3. Criando um Ambiente Virtual

Ambientes virtuais isolam as dependências de cada projeto.

### No Windows (PowerShell):

```powershell
# Navegue até a pasta do projeto
cd C:\Users\55119\OneDrive\Documentos\GitHub\climy

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
.\venv\Scripts\Activate.ps1
```

### No macOS/Linux:

```bash
cd ~/Documentos/GitHub/climy
python3 -m venv venv
source venv/bin/activate
```

**Como saber se funcionou?**
- Você verá `(venv)` no início da linha do terminal
- Exemplo: `(venv) C:\Users\55119\...>`

## 4. Instalando as Dependências do Climy

Com o ambiente virtual ativado:

```powershell
# Instale todas as dependências
pip install -r requirements.txt
```

**O que será instalado:**
- `streamlit==1.28.0` - Framework para aplicação web
- `requests==2.31.0` - Cliente HTTP para APIs
- `python-dotenv==1.0.0` - Gerenciamento de variáveis de ambiente
- `pandas==2.0.3` - Manipulação de dados
- `pytest==7.4.3` - Framework de testes
- `pytest-cov==4.1.0` - Cobertura de testes

## 5. Configurando o VS Code para o Projeto

### 5.1 Selecionando o Interpretador Python

1. No VS Code, pressione `Ctrl+Shift+P`
2. Digite: "Python: Select Interpreter"
3. Escolha o interpretador do ambiente virtual:
   - Windows: `.\venv\Scripts\python.exe`
   - macOS/Linux: `./venv/bin/python`

### 5.2 Configurando o Terminal

1. Abra as configurações (Ctrl+,)
2. Pesquise por "terminal integrated default profile"
3. Selecione PowerShell (Windows) ou bash/zsh (macOS/Linux)

### 5.3 Configurações Recomendadas

Crie o arquivo `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "files.insertFinalNewline": true,
    "files.trimTrailingWhitespace": true
}
```

## 6. Criando Arquivo .env (Opcional)

O Climy usa variáveis de ambiente para configurações:

```bash
# Crie um arquivo .env na raiz do projeto
CLIMY_TIMEOUT=5
CLIMY_CACHE_TTL=300
CLIMY_MAX_CITIES=10
CLIMY_FORECAST_DAYS=7
CLIMY_HOURLY_HOURS=24
CLIMY_LANGUAGE=pt
```

## 7. Verificando a Instalação

### Teste 1: Verificar Python

```powershell
python --version
# Esperado: Python 3.12.x
```

### Teste 2: Verificar pip

```powershell
pip --version
# Esperado: pip 24.x
```

### Teste 3: Listar pacotes instalados

```powershell
pip list
# Deve mostrar streamlit, requests, pandas, pytest, etc.
```

### Teste 4: Executar o Climy

```powershell
# Com o ambiente virtual ativado
streamlit run streamlit_app.py
```

Se abrir uma aba no navegador com o Climy, **parabéns!** 🎉

## 8. Solução de Problemas Comuns

### Problema: "python não é reconhecido"

**Solução Windows:**
1. Reinstale o Python marcando "Add to PATH"
2. Ou adicione manualmente:
   - Painel de Controle → Sistema → Variáveis de Ambiente
   - Em "Path", adicione: `C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python312\`

### Problema: "Activate.ps1 não pode ser carregado"

**Solução Windows:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: "ModuleNotFoundError"

**Solução:**
```powershell
# Verifique se o ambiente virtual está ativo
# Deve aparecer (venv) no terminal

# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### Problema: VS Code não reconhece o ambiente

**Solução:**
1. Feche e reabra o VS Code
2. Pressione Ctrl+Shift+P → "Python: Select Interpreter"
3. Selecione manualmente o python do venv

## 9. Comandos Úteis do Dia a Dia

```powershell
# Ativar ambiente virtual (Windows)
.\venv\Scripts\Activate.ps1

# Desativar ambiente virtual
deactivate

# Instalar novo pacote
pip install nome-do-pacote

# Atualizar pacotes
pip install --upgrade pip

# Ver pacotes instalados
pip list

# Gerar lista de dependências
pip freeze > requirements.txt
```

## 10. Próximos Passos

Agora que seu ambiente está configurado:

1. ✅ Leia o **Guia 02** para aprender Python básico
2. ✅ Explore a estrutura do Climy no VS Code
3. ✅ Execute o Climy e teste as funcionalidades

## 📝 Resumo

| Etapa | Comando/Arquivo |
|-------|-----------------|
| Instalar Python | python.org/downloads |
| Instalar VS Code | code.visualstudio.com |
| Criar ambiente virtual | `python -m venv venv` |
| Ativar ambiente (Windows) | `.\venv\Scripts\Activate.ps1` |
| Instalar dependências | `pip install -r requirements.txt` |
| Executar Climy | `streamlit run streamlit_app.py` |

---

**Dica:** Mantenha o ambiente virtual sempre ativado quando trabalhar no projeto!

**Próximo guia:** [02-basico-python.md](./02-basico-python.md) - Sintaxe básica e primeiros códigos
