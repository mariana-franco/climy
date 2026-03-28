# 🐍 Guia 04: Funções e Módulos - Organizando seu Código

Funções e módulos são essenciais para escrever código limpo, reutilizável e organizado.

## 1. O Que São Funções?

Uma função é um bloco de código que realiza uma tarefa específica. Pense como uma "máquina" que:
- Recebe entrada (parâmetros)
- Processa
- Retorna saída (retorno)

### Por Que Usar Funções?

✅ **Reutilização:** Escreva uma vez, use várias vezes
✅ **Organização:** Divide código complexo em partes menores
✅ **Manutenção:** Fácil de corrigir e melhorar
✅ **Testabilidade:** Fácil de testar isoladamente

## 2. Criando Funções

### Sintaxe Básica

```python
def saudacao():
    """Mostra uma mensagem de saudação."""
    print("Olá! Bem-vindo ao Python!")

# Chamando a função
saudacao()
saudacao()  # Pode chamar quantas vezes quiser
```

**Partes da função:**
- `def` - Palavra-chave que define uma função
- `saudacao` - Nome da função
- `()` - Parênteses (podem ter parâmetros)
- `:` - Dois pontos (obrigatório!)
- `"""..."""` - Docstring (documentação)
- `print(...)` - Corpo da função (indentado!)

### Funções com Parâmetros

```python
def saudacao_personalizada(nome):
    """Sauda uma pessoa pelo nome."""
    print(f"Olá, {nome}!")

saudacao_personalizada("Maria")  # Olá, Maria!
saudacao_personalizada("João")   # Olá, João!
```

### Múltiplos Parâmetros

```python
def apresentar(nome, idade, cidade):
    """Apresenta uma pessoa."""
    print(f"{nome}, {idade} anos, de {cidade}")

apresentar("Ana", 25, "São Paulo")
apresentar("Carlos", 30, "Rio de Janeiro")
```

### Parâmetros com Valor Padrão

```python
def saudacao(nome, mensagem="Olá"):
    """Sauda com mensagem padrão ou personalizada."""
    print(f"{mensagem}, {nome}!")

saudacao("Maria")              # Olá, Maria!
saudacao("João", "Bom dia")    # Bom dia, João!
```

**Importante:** Parâmetros com valor padrão devem vir **depois** dos sem valor padrão.

✅ **CERTO:**
```python
def func(a, b, c=10):  # c tem valor padrão
    pass
```

❌ **ERRADO:**
```python
def func(a=10, b, c):  # Erro! a não pode ter padrão se b e c não têm
    pass
```

## 3. Retorno de Valores

### Usando return

```python
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

resultado = soma(5, 3)
print(resultado)  # 8

# Ou usar diretamente
print(soma(10, 20))  # 30
```

### Múltiplos Retornos

```python
def calcular(num1, num2):
    """Retorna várias operações."""
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2

    return soma, subtracao, multiplicacao, divisao

# Recebendo todos os valores
resultados = calcular(10, 2)
print(resultados)  # (12, 8, 20, 5.0) - uma tupla!

# Desempacotando
s, sub, mult, div = calcular(10, 2)
print(f"Soma: {s}, Divisão: {div}")
```

### Retorno Antecipado

```python
def verificar_idade(idade):
    """Verifica se é maior de idade."""
    if idade < 0:
        return "Idade inválida!"

    if idade < 18:
        return "Menor de idade"

    return "Maior de idade"

print(verificar_idade(-5))   # Idade inválida!
print(verificar_idade(15))   # Menor de idade
print(verificar_idade(25))   # Maior de idade
```

## 4. Escopo de Variáveis

### Variáveis Locais vs Globais

```python
# Variável global
mensagem_global = "Sou global"

def minha_funcao():
    # Variável local
    mensagem_local = "Sou local"
    print(mensagem_global)  # Funciona!
    print(mensagem_local)   # Funciona!

minha_funcao()
print(mensagem_global)  # Funciona!
print(mensagem_local)   # ERRO! Não existe fora da função
```

### Modificando Variáveis Globais

```python
contador = 0

def incrementar():
    global contador  # Declara que vai usar a global
    contador += 1

incrementar()
print(contador)  # 1
```

**Dica:** Evite usar `global`. Prefira retornar valores e reatribuir.

## 5. Tipos de Parâmetros

### *args (Argumentos Posicionais Variáveis)

```python
def soma_todos(*args):
    """Soma quantos números forem passados."""
    return sum(args)

print(soma_todos(1, 2, 3))        # 6
print(soma_todos(1, 2, 3, 4, 5))  # 15
```

### **kwargs (Argumentos Nomeados Variáveis)

```python
def mostrar_info(**kwargs):
    """Mostra informações nomeadas."""
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Maria", idade=25, cidade="SP")
# nome: Maria
# idade: 25
# cidade: SP
```

### Combinando Tudo

```python
def func_completa(a, b, *args, c=10, **kwargs):
    """Função com todos os tipos de parâmetros."""
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}")
    print(f"kwargs={kwargs}")

func_completa(1, 2, 3, 4, 5, c=20, nome="Ana")
# a=1, b=2
# args=(3, 4, 5)
# c=20
# kwargs={'nome': 'Ana'}
```

## 6. Funções Lambda

Funções anônimas (sem nome) de uma linha.

```python
# Forma normal
def quadrado(x):
    return x ** 2

# Com lambda
quadrado = lambda x: x ** 2

print(quadrado(5))  # 25

# Lambda com múltiplos parâmetros
soma = lambda a, b: a + b
print(soma(3, 4))  # 7

# Lambda em listas
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25]
```

**Quando usar:** Para funções simples e rápidas. Para lógica complexa, use `def`.

## 7. Módulos e Imports

### O Que São Módulos?

Módulos são arquivos Python (`.py`) que contêm código reutilizável.

### Criando Seu Primeiro Módulo

**Arquivo: `matematica.py`**
```python
"""Módulo com funções matemáticas."""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    return "Divisão por zero!"

PI = 3.14159
```

**Arquivo: `main.py`**
```python
# Importando o módulo
import matematica

print(matematica.soma(5, 3))      # 8
print(matematica.PI)              # 3.14159
```

### Formas de Importar

```python
# 1. Importa o módulo inteiro
import matematica
matematica.soma(5, 3)

# 2. Importa funções específicas
from matematica import soma, divisao
soma(5, 3)  # Não precisa do prefixo
divisao(10, 2)

# 3. Importa tudo (não recomendado)
from matematica import *
soma(5, 3)

# 4. Importa com apelido (alias)
import matematica as mat
mat.soma(5, 3)

from matematica import soma as s
s(5, 3)
```

### Módulos da Biblioteca Padrão

Python já vem com muitos módulos úteis:

```python
# math - Matemática
import math
print(math.sqrt(25))      # 5.0
print(math.pi)            # 3.14159...
print(math.ceil(4.3))     # 5 (arredonda pra cima)

# random - Números aleatórios
import random
print(random.randint(1, 100))  # Número aleatório entre 1 e 100
print(random.choice(['a', 'b', 'c']))  # Escolhe um da lista

# datetime - Datas e horas
from datetime import datetime
agora = datetime.now()
print(agora)  # 2026-03-28 10:30:45.123456
print(agora.year)  # 2026

# os - Sistema operacional
import os
print(os.getcwd())  # Diretório atual
print(os.listdir())  # Lista arquivos da pasta

# sys - Sistema
import sys
print(sys.version)  # Versão do Python
print(sys.path)     # Caminhos de busca de módulos
```

## 8. Pacotes

Pacotes são pastas com módulos Python.

### Estrutura de Pacote

```
meu_pacote/
    __init__.py  # Torna a pasta um pacote
    modulo1.py
    modulo2.py
    subpacote/
        __init__.py
        modulo3.py
```

**`__init__.py`** pode ser vazio ou conter código de inicialização.

### Importando de Pacotes

```python
# Importa do pacote
import meu_pacote.modulo1
meu_pacote.modulo1.funcao()

# Importa específico
from meu_pacote import modulo1
modulo1.funcao()

# Do subpacote
from meu_pacote.subpacote import modulo3
modulo3.funcao()
```

## 9. Exemplos Práticos

### Exemplo 1: Módulo de Utilidades (Climy)

**Arquivo: `src/utils.py`**
```python
"""Utilitários para o Climy."""

def formatar_temperatura(temp: float, unidade: str = "C") -> str:
    """Formata temperatura com símbolo."""
    simbolo = "°C" if unidade == "C" else "°F"
    return f"{temp:.1f}{simbolo}"

def formatar_vento(velocidade: float) -> str:
    """Formata velocidade do vento com ícone."""
    if velocidade < 5:
        return f"🍃 {velocidade:.1f} km/h"
    elif velocidade < 15:
        return f"💨 {velocidade:.1f} km/h"
    else:
        return f"🌪️ {velocidade:.1f} km/h"

def classificar_temperatura(temp: float) -> str:
    """Classifica temperatura em categorias."""
    if temp < 0:
        return "Congelante ❄️"
    elif temp < 15:
        return "Frio 🥶"
    elif temp < 25:
        return "Agradável 😌"
    elif temp < 30:
        return "Quente 🌤️"
    else:
        return "Muito quente 🥵"
```

**Uso:**
```python
from src.utils import formatar_temperatura, classificar_temperatura

temp = 28.5
print(f"Temperatura: {formatar_temperatura(temp)}")
print(f"Classificação: {classificar_temperatura(temp)}")
```

### Exemplo 2: Módulo de Validação

**Arquivo: `validators.py`**
```python
"""Validadores de dados."""

def validar_email(email: str) -> bool:
    """Valida se é um email válido."""
    return '@' in email and '.' in email

def validar_idade(idade: int) -> bool:
    """Valida faixa etária razoável."""
    return 0 <= idade <= 150

def validar_cidade(cidade: str) -> bool:
    """Valida se cidade tem nome válido."""
    return len(cidade.strip()) >= 2 and cidade.isalpha() or ' ' in cidade
```

### Exemplo 3: Calculadora Modular

**Arquivo: `calculadora/__init__.py`**
```python
"""Pacote calculadora."""

from .operacoes import soma, subtracao, multiplicacao, divisao
from .estatisticas import media, mediana, desvio_padrao

__all__ = ['soma', 'subtracao', 'multiplicacao', 'divisao',
           'media', 'mediana', 'desvio_padrao']
```

**Arquivo: `calculadora/operacoes.py`**
```python
"""Operações básicas."""

def soma(*args):
    return sum(args)

def subtracao(a, b):
    return a - b

def multiplicacao(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b
```

**Arquivo: `calculadora/estatisticas.py`**
```python
"""Funções estatísticas."""

def media(numeros):
    return sum(numeros) / len(numeros)

def mediana(numeros):
    ordenados = sorted(numeros)
    meio = len(ordenados) // 2
    return ordenados[meio]
```

## 10. Decoradores (Bônus)

Decoradores modificam o comportamento de funções.

```python
def meu_decorador(func):
    """Decorador simples."""
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def saudacao():
    print("Olá!")

saudacao()
# Antes da função
# Olá!
# Depois da função
```

### Decorador com Logging (Útil para Climy)

```python
import logging
from functools import wraps

def log_chamada(func):
    """Registra chamadas de função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Chamando {func.__name__}")
        resultado = func(*args, **kwargs)
        logging.info(f"{func.__name__} retornou {resultado}")
        return resultado
    return wrapper

@log_chamada
def buscar_temperatura(cidade):
    # Simula busca na API
    return 25.5

buscar_temperatura("São Paulo")
```

## 11. Boas Práticas

### Nomes de Funções

✅ **CERTO:**
```python
def calcular_media():
    pass

def buscar_usuario():
    pass

def validar_dados():
    pass
```

❌ **ERRADO:**
```python
def calc():  # Muito vago
    pass

def funcao1():  # Sem significado
    pass
```

### Docstrings

Sempre documente suas funções:

```python
def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso: Peso em quilogramas
        altura: Altura em metros

    Returns:
        float: Valor do IMC

    Example:
        >>> calcular_imc(70, 1.75)
        22.86
    """
    return peso / (altura ** 2)
```

### Funções Devem Fazer UMA Coisa

❌ **ERRADO:**
```python
def processar_dados():
    # Lê arquivo
    # Valida dados
    # Salva no banco
    # Envia email
    # Gera relatório
    pass  # Faz demais coisas!
```

✅ **CERTO:**
```python
def ler_arquivo():
    pass

def validar_dados(dados):
    pass

def salvar_no_banco(dados):
    pass

def enviar_email(destinatario):
    pass

def gerar_relatorio():
    pass
```

## 12. Exercícios Práticos

### Exercício 1: Calculadora de IMC
Crie uma função que calcula IMC e retorna a classificação.

<details>
<summary>Ver solução</summary>

```python
def calcular_imc(peso, altura):
    """Calcula IMC e retorna valor e classificação."""
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return imc, classificacao

# Uso
imc, classif = calcular_imc(70, 1.75)
print(f"IMC: {imc:.2f} - {classif}")
```
</details>

### Exercício 2: Formatador de Moeda
Crie um módulo que formata valores em Real.

<details>
<summary>Ver solução</summary>

```python
# modulo_moeda.py

def formatar_real(valor):
    """Formata valor como Real Brasileiro."""
    return f"R$ {valor:.2f}".replace('.', ',')

def formatar_porcentagem(valor):
    """Formata como porcentagem."""
    return f"{valor:.1f}%"

# Uso
from modulo_moeda import formatar_real
print(formatar_real(19.99))  # R$ 19,99
```
</details>

### Exercício 3: Processador de Temperaturas
Crie funções para analisar lista de temperaturas.

<details>
<summary>Ver solução</summary>

```python
def analisar_temperaturas(temps):
    """Analisa lista de temperaturas."""
    if not temps:
        return None

    return {
        'maxima': max(temps),
        'minima': min(temps),
        'media': sum(temps) / len(temps),
        'total': len(temps)
    }

# Uso
temps = [22.5, 24.0, 26.3, 28.1, 25.7]
analise = analisar_temperaturas(temps)
print(f"Média: {analise['media']:.1f}°C")
```
</details>

## 13. Resumo

| Conceito | Sintaxe | Exemplo |
|----------|---------|---------|
| Definir função | `def nome():` | `def saudar():` |
| Parâmetro | `def f(param):` | `def f(nome):` |
| Retorno | `return valor` | `return x + y` |
| Importar módulo | `import modulo` | `import math` |
| Importar função | `from mod import func` | `from math import sqrt` |
| Lambda | `lambda x: expr` | `lambda x: x*2` |

## Próximos Passos

1. ✅ Crie seu próprio módulo
2. ✅ Pratique com funções do Climy
3. ✅ Estude o **Guia 05** (Estruturas de Dados)

---

**Próximo guia:** [05-estruturas-dados.md](./05-estruturas-dados.md) - Listas, dicionários e mais
