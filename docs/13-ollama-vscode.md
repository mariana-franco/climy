# 🤖 Guia 13: Usando Ollama como Agente no VS Code

Guia completo para configurar e usar Ollama com IA no VS Code para potencializar seu desenvolvimento.

## 1. O Que é Ollama?

**Ollama** é uma ferramenta que permite rodar modelos de linguagem (LLMs) localmente no seu computador.

### Vantagens

✅ **Privacidade** - Tudo roda localmente, sem enviar dados para nuvem
✅ **Gratuito** - Sem custos de API
✅ **Offline** - Funciona sem internet
✅ **Customizável** - Escolha entre vários modelos
✅ **Rápido** - Sem latência de rede

### Modelos Disponíveis

| Modelo | Tamanho | Uso |
|--------|---------|-----|
| Llama 3.2 | 3B | Rápido, bom para código |
| Llama 3.1 | 8B | Equilibrado |
| Mistral | 7B | Bom para código |
| Codellama | 7B | Especializado em código |
| DeepSeek Coder | 6.7B | Excelente para programação |

## 2. Instalando Ollama

### Windows

1. **Baixe o instalador:**
   - Acesse https://ollama.com/download
   - Baixe para Windows
   - Execute instalador

2. **Verifique instalação:**
   ```powershell
   ollama --version
   ```

### macOS

```bash
# Com Homebrew
brew install ollama

# Ou baixe em https://ollama.com/download
```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 3. Baixando Modelos

### Comandos Básicos

```powershell
# Baixar modelo (ex: Llama 3.2)
ollama pull llama3.2

# Baixar modelo para código
ollama pull codellama

# Baixar DeepSeek Coder
ollama pull deepseek-coder

# Listar modelos instalados
ollama list

# Remover modelo
ollama rm llama3.2
```

### Modelos Recomendados para Programação

```powershell
# Melhor custo-benefício
ollama pull llama3.2

# Especializado em código
ollama pull codellama

# Alternativa excelente
ollama pull deepseek-coder

# Modelo pequeno e rápido
ollama pull phi3
```

## 4. Configurando Ollama no VS Code

### Extensão 1: Continue (Recomendado)

1. **Instale a extensão:**
   - VS Code → Extensions (Ctrl+Shift+X)
   - Busque "Continue"
   - Instale "Continue - Codestral, Llama, Claude..."

2. **Configure para Ollama:**
   - Abra `~/.continue/config.json`
   - Ou clique no ícone do Continue → ⚙️ Settings

```json
{
  "models": [
    {
      "title": "Ollama - Llama 3.2",
      "provider": "ollama",
      "model": "llama3.2",
      "apiBase": "http://localhost:11434"
    },
    {
      "title": "Ollama - CodeLlama",
      "provider": "ollama",
      "model": "codellama",
      "apiBase": "http://localhost:11434"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Ollama - Llama 3.2",
    "provider": "ollama",
    "model": "llama3.2",
    "apiBase": "http://localhost:11434"
  }
}
```

3. **Use o Continue:**
   - `Ctrl+L` - Chat com IA
   - `Ctrl+I` - Editar código com IA
   - `Tab` - Autocomplete

### Extensão 2: Cline (Agente Autônomo)

1. **Instale:**
   - Busque "Cline" nas extensões
   - Instale

2. **Configure:**
   - Abra Cline (ícone na barra lateral)
   - Settings → Provider: Ollama
   - Model: `llama3.2` ou `codellama`
   - Base URL: `http://localhost:11434`

3. **Use:**
   - Digite tarefas em linguagem natural
   - Cline executa ações no VS Code

### Extensão 3: Twinny

1. **Instale:**
   - Busque "Twinny" nas extensões

2. **Configure:**
   ```json
   {
     "twinny.ollamaUrl": "http://localhost:11434",
     "twinny.model": "codellama"
   }
   ```

3. **Use:**
   - Autocomplete estilo GitHub Copilot
   - `Ctrl+Enter` para gerar código

## 5. Usando Ollama via Terminal

### Chat Interativo

```powershell
# Iniciar chat
ollama run llama3.2

# Digite sua pergunta
>>> "Como faço uma função em Python?"
```

### Prompt Único

```powershell
# Execute e saia
ollama run llama3.2 "Explique list comprehension em Python"
```

### Com Contexto de Arquivo

```powershell
# Pipe de arquivo
cat meu_arquivo.py | ollama run llama3.2 "Explique este código"

# Ou no Windows PowerShell
Get-Content meu_arquivo.py | ollama run llama3.2 "Explique este código"
```

## 6. API do Ollama

### Endpoint Principal

```
http://localhost:11434/api/generate
```

### Exemplo com Python

```python
import requests
import json

def perguntar_ollama(pergunta: str, modelo: str = "llama3.2"):
    """Envia pergunta para Ollama local."""

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": modelo,
        "prompt": pergunta,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]

# Uso
resposta = perguntar_ollama(
    "Como criar uma lista em Python?"
)
print(resposta)
```

### Com Histórico (Contexto)

```python
def chat_ollama(mensagens: list, modelo: str = "llama3.2"):
    """Chat com histórico de mensagens."""

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": modelo,
        "messages": mensagens,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["message"]["content"]

# Uso
mensagens = [
    {"role": "user", "content": "O que é Python?"},
    {"role": "assistant", "content": "Python é uma linguagem..."},
    {"role": "user", "content": "Mostre um exemplo"}
]

resposta = chat_ollama(mensagens)
```

## 7. Casos de Uso no Desenvolvimento

### 1. Explicar Código

**Prompt:**
```
Explique este código linha por linha:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
```

### 2. Gerar Código

**Prompt:**
```
Crie uma função Python que:
- Recebe uma lista de temperaturas
- Retorna média, máxima e mínima
- Inclua docstring e type hints
```

### 3. Debuggar Erros

**Prompt:**
```
Este código está dando erro. O que está errado?

```python
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

print(calcular_media([]))
```

Erro: ZeroDivisionError: division by zero
```

### 4. Refatorar Código

**Prompt:**
```
Refatore este código para seguir PEP 8:

```python
def calc(x,y):
    z=x+y
    return z
```
```

### 5. Gerar Testes

**Prompt:**
```
Crie testes pytest para esta função:

```python
def validar_email(email):
    return '@' in email and '.' in email
```
```

### 6. Documentar Código

**Prompt:**
```
Adicione docstrings completas:

```python
class Calculadora:
    def soma(self, a, b):
        return a + b

    def divisao(self, a, b):
        return a / b
```
```

## 8. Integração com Climy

### Exemplo: Gerar Explicação do Código

```python
import requests

def gerar_explicacao_codigo(arquivo: str):
    """Gera explicação de arquivo Python usando Ollama."""

    # Lê arquivo
    with open(arquivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    prompt = f"""
Explique este código de forma didática para iniciantes:

```python
{codigo}
```

Inclua:
1. O que o código faz
2. Principais funções/classes
3. Exemplos de uso
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

# Uso
explicacao = gerar_explicacao_codigo("services/weather_api.py")
print(explicacao)
```

### Exemplo: Gerar Testes Automaticamente

```python
def gerar_testes(arquivo: str, funcao: str):
    """Gera testes pytest para uma função específica."""

    with open(arquivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    prompt = f"""
Crie testes pytest completos para a função '{funcao}':

```python
{codigo}
```

Inclua:
- Casos normais
- Casos de erro
- Edge cases
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "codellama",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

# Uso
testes = gerar_testes("src/utils.py", "validar_email")
print(testes)
```

## 9. Dicas de Performance

### Otimizar Modelo

```powershell
# Usar modelo quantizado (menor, mais rápido)
ollama pull llama3.2:3b

# Aumentar contexto se tiver RAM
ollama run llama3.2 --num_ctx 4096
```

### Configurar GPU (se disponível)

```powershell
# Ollama usa GPU automaticamente se disponível
# Verifique:
ollama run llama3.2
# Deve mostrar "Using GPU" se disponível
```

### Reduzir Uso de Memória

```json
// ~/.ollama/config.json
{
  "num_ctx": 2048,
  "num_batch": 256
}
```

## 10. Solução de Problemas

### Problema: "Connection refused"

**Solução:**
```powershell
# Verifique se Ollama está rodando
ollama list

# Se não estiver, inicie
ollama serve

# No Windows, verifique se serviço está rodando
# Services → Ollama
```

### Problema: Modelo muito lento

**Solução:**
```powershell
# Use modelo menor
ollama pull phi3
ollama pull llama3.2:1b

# Ou modelo quantizado
ollama pull llama3.2:q4_0
```

### Problema: "Model not found"

**Solução:**
```powershell
# Baixe o modelo
ollama pull llama3.2

# Verifique modelos instalados
ollama list
```

### Problema: VS Code não conecta

**Solução:**
```powershell
# Verifique se Ollama está acessível
curl http://localhost:11434/api/tags

# Deve retornar lista de modelos

# Reinicie Ollama
ollama serve
```

## 11. Comandos Úteis

```powershell
# Iniciar servidor Ollama
ollama serve

# Listar modelos
ollama list

# Baixar modelo
ollama pull <nome>

# Rodar modelo
ollama run <nome>

# Remover modelo
ollama rm <nome>

# Copiar modelo
ollama cp <origem> <destino>

# Ver logs
Get-Content ~/.ollama/logs/server.log -Tail 50
```

## 12. Melhores Práticas

### 1. Escolha Modelo Certo

- **Código:** `codellama`, `deepseek-coder`
- **Geral:** `llama3.2`, `mistral`
- **Rápido:** `phi3`, `llama3.2:1b`

### 2. Prompts Claros

❌ **Vago:**
```
"Faça uma função"
```

✅ **Específico:**
```
"Crie uma função Python que valida email,
retorna True se tiver @ e ., False caso contrário.
Inclua type hints e docstring."
```

### 3. Revise Código Gerado

- IA pode errar
- Sempre teste o código
- Verifique segurança

### 4. Use Contexto

```
"Considere este código existente:
[código]

Agora adicione uma função que..."
```

## 13. Próximos Passos

1. ✅ Instale Ollama
2. ✅ Baixe `llama3.2` ou `codellama`
3. ✅ Instale extensão Continue no VS Code
4. ✅ Configure para usar Ollama local
5. ✅ Pratique com os exemplos do **Guia 14** (Prompt Engineering)

---

**Próximo guia:** [14-prompt-engineering.md](./14-prompt-engineering.md) - Como escrever prompts eficazes
