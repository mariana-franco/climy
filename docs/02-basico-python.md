# 🐍 Guia 02: Básico do Python - Sintaxe e Primeiros Códigos

Bem-vindo ao mundo Python! Neste guia, você aprenderá os fundamentos da linguagem.

## 1. Primeiro Programa

### Hello World

```python
print("Olá, mundo!")
```

**O que acontece:**
- `print()` é uma função que exibe texto na tela
- O texto entre aspas é uma **string** (texto)
- Parênteses indicam que estamos **chamando** a função

### Executando no VS Code

1. Crie um arquivo `teste.py`
2. Digite o código acima
3. Clique com botão direito → "Run Python File in Terminal"
4. Ou pressione `Ctrl+F5`

## 2. Variáveis

Variáveis são como "caixas" onde guardamos informações.

```python
# Criando variáveis
nome = "Maria"      # Texto (string)
idade = 25          # Número inteiro (int)
altura = 1.68       # Número decimal (float)
estudante = True    # Verdadeiro/Falso (boolean)

# Usando variáveis
print(nome)         # Mostra: Maria
print(idade)        # Mostra: 25
```

### Regras para Nomes de Variáveis

✅ **VÁLIDO:**
```python
nome = "João"
idade_usuario = 30
_total = 100
nome2 = "Carlos"
```

❌ **INVÁLIDO:**
```python
2nome = "Carlos"    # Não pode começar com número
nome-usuario = "João"  # Não pode usar hífen
class = "Python"    # Não pode usar palavras reservadas
```

### Tipos de Dados

```python
# String (texto)
nome = "Ana"
cidade = 'São Paulo'  # Aspas simples também funciona

# Inteiro (números sem vírgula)
idade = 25
quantidade = -10  # Negativos também

# Float (números decimais)
altura = 1.75
preco = 19.99
temperatura = -3.5

# Boolean (verdadeiro ou falso)
ativo = True
inativo = False

# None (valor vazio/nulo)
valor = None
```

## 3. Operações Básicas

### Aritméticas

```python
a = 10
b = 3

soma = a + b           # 13
subtracao = a - b      # 7
multiplicacao = a * b  # 30
divisao = a / b        # 3.333... (sempre retorna float)
divisao_inteira = a // b  # 3 (só a parte inteira)
resto = a % b          # 1 (resto da divisão)
potencia = a ** b      # 1000 (10 elevado a 3)
```

### Comparação

```python
x = 10
y = 20

x == y   # False (igual)
x != y   # True (diferente)
x > y    # False (maior)
x < y    # True (menor)
x >= y   # False (maior ou igual)
x <= y   # True (menor ou igual)
```

### Lógicas

```python
ativo = True
logado = False

ativo and logado   # False (E lógico - ambos precisam ser True)
ativo or logado    # True (OU lógico - pelo menos um True)
not ativo          # False (NEGAÇÃO - inverte o valor)
```

## 4. Strings (Texto)

### Criando e Manipulando

```python
nome = "Python"

# Acessando caracteres
primeira_letra = nome[0]     # 'P'
segunda_letra = nome[1]      # 'y'
ultima_letra = nome[-1]      # 'n'

# Fatiamento (slicing)
parte = nome[0:3]    # 'Pyt' (índices 0, 1, 2)
parte = nome[:3]     # 'Pyt' (do início até 3)
parte = nome[2:]     # 'thon' (do 2 até o fim)
parte = nome[:]      # 'Python' (tudo)

# Tamanho
tamanho = len(nome)  # 6
```

### Métodos de String

```python
texto = "  Hello World  "

texto.lower()        # "  hello world  " (minúsculas)
texto.upper()        # "  HELLO WORLD  " (maiúsculas)
texto.strip()        # "Hello World" (remove espaços das pontas)
texto.replace("H", "J")  # "  Jello World  "
texto.split()        # ['Hello', 'World'] (transforma em lista)
texto.capitalize()   # "  hello world  " (primeira maiúscula)
texto.title()        # "  Hello World  " (cada palavra com maiúscula)
```

### Formatando Strings

```python
# f-strings (recomendado - Python 3.6+)
nome = "Maria"
idade = 25

print(f"Olá, {nome}!")                    # Olá, Maria!
print(f"Você tem {idade} anos")           # Você tem 25 anos
print(f"Próximo ano: {idade + 1}")        # Próximo ano: 26

# Format (antigo, mas ainda usado)
print("Olá, {}!".format(nome))
print("Olá, {0}! Você tem {1} anos".format(nome, idade))

# % (muito antigo, evite)
print("Olá, %s!" % nome)
```

### Exemplo Prático

```python
# Formatando números
preco = 19.99
print(f"Preço: R$ {preco:.2f}")  # Preço: R$ 19.99

# Formatando porcentagem
taxa = 0.15
print(f"Taxa: {taxa:.1%}")  # Taxa: 15.0%

# Alinhamento
nome = "Ana"
print(f"{nome:>10}")  # "       Ana" (direita, 10 caracteres)
print(f"{nome:<10}")  # "Ana       " (esquerda)
print(f"{nome:^10}")  # "   Ana    " (centro)
```

## 5. Input do Usuário

```python
# Pedindo dados ao usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Olá, {nome}! Você tem {idade} anos.")
```

**Importante:** `input()` sempre retorna **string**!

```python
# Para números, converta:
idade = int(input("Digite sua idade: "))      # inteiro
altura = float(input("Digite sua altura: "))  # decimal
```

## 6. Comentários

```python
# Comentário de uma linha

"""
Comentário de múltiplas linhas
(tecnicamente é uma string, mas funciona como comentário)
"""

def calcular_area():
    """Docstring: explica o que a função faz"""
    pass
```

## 7. Exemplos Práticos

### Exemplo 1: Calculadora Simples

```python
# Calculadora básica
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}")
```

### Exemplo 2: Conversor de Temperatura

```python
# Celsius para Fahrenheit
celsius = float(input("Temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Fahrenheit para Celsius
fahrenheit = float(input("Temperatura em °F: "))
celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F = {celsius:.1f}°C")
```

### Exemplo 3: Formatando Dados do Climy

```python
# Exemplo baseado no Climy
cidade = "São Paulo"
temperatura = 28.5
umidade = 65
vento = 12.3

print("=" * 40)
print(f"🌤️  Previsão para {cidade}")
print("=" * 40)
print(f"🌡️  Temperatura: {temperatura:.1f}°C")
print(f"💧 Umidade: {umidade}%")
print(f"💨 Vento: {vento:.1f} km/h")
print("=" * 40)
```

**Saída:**
```
========================================
🌤️  Previsão para São Paulo
========================================
🌡️  Temperatura: 28.5°C
💧 Umidade: 65%
💨 Vento: 12.3 km/h
========================================
```

## 8. Erros Comuns de Iniciantes

### Esquecer dois pontos (:)

❌ **ERRADO:**
```python
if idade > 18  # Falta :
    print("Maior")
```

✅ **CERTO:**
```python
if idade > 18:  # Tem :
    print("Maior")
```

### Confundir = com ==

❌ **ERRADO:**
```python
if x = 5:  # = é para atribuir
    print("É 5")
```

✅ **CERTO:**
```python
if x == 5:  # == é para comparar
    print("É 5")
```

### Indentação errada

❌ **ERRADO:**
```python
def saudacao():
print("Olá")  # Falta indentação
```

✅ **CERTO:**
```python
def saudacao():
    print("Olá")  # 4 espaços ou 1 tab
```

### Usar variável não definida

❌ **ERRADO:**
```python
print(nome)  # nome não existe
```

✅ **CERTO:**
```python
nome = "Maria"
print(nome)  # Agora funciona
```

## 9. Exercícios Práticos

### Exercício 1: Boas-vindas
Crie um programa que pede nome e idade, depois exibe uma mensagem de boas-vindas.

<details>
<summary>Ver solução</summary>

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"\nBem-vindo(a), {nome}!")
print(f"Que legal que você tem {idade} anos!")
```
</details>

### Exercício 2: Calculadora de IMC
Crie um programa que calcula o IMC (Índice de Massa Corporal).

<details>
<summary>Ver solução</summary>

```python
nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"\n{nome}, seu IMC é {imc:.2f}")
```
</details>

### Exercício 3: Conversor de Moedas
Crie um conversor de Real para Dólar (use cotação fixa, ex: 5.0).

<details>
<summary>Ver solução</summary>

```python
cotacao = 5.0
reais = float(input("Valor em R$: "))

dolares = reais / cotacao

print(f"R$ {reais:.2f} = US$ {dolares:.2f}")
```
</details>

## 10. Resumo

| Conceito | Exemplo |
|----------|---------|
| Variável | `nome = "Maria"` |
| Print | `print("Olá")` |
| Input | `idade = input("Idade: ")` |
| Type | `int()`, `float()`, `str()`, `bool()` |
| Operadores | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparação | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Lógicos | `and`, `or`, `not` |
| String | `len()`, `.upper()`, `.lower()`, `.split()` |
| f-string | `f"Olá, {nome}!"` |

## Próximos Passos

Agora que você conhece o básico:

1. ✅ Pratique os exercícios
2. ✅ Modifique os exemplos
3. ✅ Crie seus próprios programas
4. ✅ Avance para o **Guia 03** (Condicionais e Loops)

## 📝 Dica de Ouro

**Sempre teste seu código!** Não apenas leia, execute, modifique, quebre e conserte. É assim que se aprende programação.

---

**Próximo guia:** [03-estruturas-controle.md](./03-estruturas-controle.md) - if/else, for, while
