# 🐍 Guia 03: Estruturas de Controle - Condicionais e Loops

Agora que você sabe o básico de variáveis e operadores, vamos aprender a controlar o fluxo do programa!

## 1. Condicionais (if, elif, else)

Condicionais permitem que seu programa tome decisões.

### Estrutura Básica

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade!")
    print("Pode tirar carteira de motorista.")
```

**Importante:** Note os **dois pontos (:)** após a condição e a **indentação** (4 espaços) nas linhas seguintes.

### if com else

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### if, elif, else (Múltiplas condições)

```python
nota = 75

if nota >= 90:
    print("Conceito A")
elif nota >= 70:  # elif = else if
    print("Conceito B")
elif nota >= 50:
    print("Conceito C")
else:
    print("Conceito D - Reprovado")
```

**Como funciona:**
1. Verifica a primeira condição (`if`)
2. Se for falsa, verifica a próxima (`elif`)
3. Continua verificando até achar uma verdadeira
4. Se nenhuma for verdadeira, executa o `else`

### Condições Compostas

```python
# Usando AND (ambas devem ser verdadeiras)
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir!")

# Usando OR (pelo menos uma deve ser verdadeira)
dia = "Sábado"

if dia == "Sábado" or dia == "Domingo":
    print("Fim de semana!")

# Usando NOT (inverte a condição)
chovendo = False

if not chovendo:
    print("Não está chovendo, pode sair!")
```

### Exemplos Práticos

#### Exemplo 1: Verificando Triângulo

```python
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É um triângulo válido!")

    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo válido!")
```

#### Exemplo 2: Sistema de Login Simples

```python
usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido!")
elif usuario == usuario_correto:
    print("Senha incorreta!")
else:
    print("Usuário não encontrado!")
```

#### Exemplo 3: Classificação Climática (Baseado no Climy)

```python
temperatura = 28.5

if temperatura < 0:
    print("❄️ Congelante")
elif temperatura < 15:
    print("🥶 Frio")
elif temperatura < 25:
    print("😌 Agradável")
elif temperatura < 30:
    print("🌤️ Quente")
else:
    print("🥵 Muito quente")
```

## 2. Loops (Repetição)

Loops permitem repetir blocos de código várias vezes.

### Loop for (Para cada)

Use quando souber quantas vezes quer repetir.

```python
# Iterando sobre uma sequência de números
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Contagem: {i}")

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

# Iterando sobre uma string
nome = "Python"

for letra in nome:
    print(f"Letra: {letra}")
```

### range() - Gerador de Números

```python
range(5)       # 0, 1, 2, 3, 4
range(2, 6)    # 2, 3, 4, 5 (início, fim)
range(0, 10, 2)  # 0, 2, 4, 6, 8 (início, fim, passo)
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (contagem regressiva)
```

### Exemplos com for

#### Exemplo 1: Tabuada

```python
numero = int(input("Tabuada do: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

#### Exemplo 2: Soma de Números

```python
soma = 0

for i in range(1, 101):  # 1 até 100
    soma += i  # soma = soma + i

print(f"Soma de 1 a 100: {soma}")
```

#### Exemplo 3: Processando Temperaturas (Climy)

```python
temperaturas = [22.5, 24.0, 26.3, 28.1, 25.7, 23.9, 21.5]

print("Previsão semanal:")
print("-" * 30)

for i, temp in enumerate(temperaturas):
    dia = i + 1
    print(f"Dia {dia}: {temp:.1f}°C")

# Calculando média
media = sum(temperaturas) / len(temperaturas)
print("-" * 30)
print(f"Média: {media:.1f}°C")
```

### Loop while (Enquanto)

Use quando não souber quantas vezes vai repetir.

```python
# Contador simples
contador = 0

while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1  # Importante: incrementa para não loop infinito!

print("Fim!")
```

### Exemplos com while

#### Exemplo 1: Validação de Input

```python
senha = ""

while len(senha) < 6:
    senha = input("Digite uma senha (mínimo 6 caracteres): ")
    if len(senha) < 6:
        print("Senha muito curta!")

print("Senha válida!")
```

#### Exemplo 2: Menu Interativo

```python
opcao = 0

while opcao != 4:
    print("\n=== Menu ===")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Saldo: R$ 1000.00")
    elif opcao == 2:
        valor = float(input("Valor: "))
        print(f"Depositado R$ {valor:.2f}")
    elif opcao == 3:
        valor = float(input("Valor: "))
        print(f"Sacado R$ {valor:.2f}")
    elif opcao == 4:
        print("Saindo...")
    else:
        print("Opção inválida!")
```

#### Exemplo 3: Jogo de Adivinhação

```python
import random

numero_secreto = random.randint(1, 100)
palpites = 0
adivinhou = False

print("Adivinhe o número (1-100)")

while not adivinhou:
    palpite = int(input("Seu palpite: "))
    palpites += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Acertou em {palpites} tentativas!")
        adivinhou = True
    elif palpite < numero_secreto:
        print("Mais alto!")
    else:
        print("Mais baixo!")
```

## 3. Controle de Loops

### break (Interrompe o loop)

```python
for i in range(10):
    if i == 5:
        break  # Para o loop quando i for 5
    print(i)

# Saída: 0, 1, 2, 3, 4
```

### continue (Pula para próxima iteração)

```python
for i in range(10):
    if i % 2 == 0:  # Se for par
        continue  # Pula este número
    print(i)

# Saída: 1, 3, 5, 7, 9 (só ímpares)
```

### Exemplo Combinado

```python
numeros = [1, 3, -5, 7, -2, 9, 0, 11]

for num in numeros:
    if num < 0:
        print(f"Negativo encontrado: {num}, pulando...")
        continue

    if num == 0:
        print("Zero encontrado, parando!")
        break

    print(f"Número positivo: {num}")
```

## 4. Loops Aninhados

Loops dentro de loops.

### Tabuada Completa

```python
for i in range(1, 11):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j:2} = {resultado:3}")
```

### Padrões com Estrelas

```python
# Triângulo
for i in range(1, 6):
    print("*" * i)

# Saída:
# *
# **
# ***
# ****
# *****

# Triângulo invertido
for i in range(5, 0, -1):
    print("*" * i)
```

### Matriz/Grade

```python
# Imprimindo uma grade 3x3
for linha in range(3):
    for coluna in range(3):
        print(f"[{linha},{coluna}]", end=" ")
    print()  # Nova linha

# Saída:
# [0,0] [0,1] [0,2]
# [1,0] [1,1] [1,2]
# [2,0] [2,1] [2,2]
```

## 5. Exemplos Práticos Avançados

### Exemplo 1: Analisador de Temperaturas (Climy)

```python
temperaturas = []

print("Digite as temperaturas (ou 'fim' para encerrar):")

while True:
    entrada = input("Temperatura: ")

    if entrada.lower() == 'fim':
        break

    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Valor inválido!")

if temperaturas:
    print(f"\nTotal: {len(temperaturas)} temperaturas")
    print(f"Máxima: {max(temperaturas):.1f}°C")
    print(f"Mínima: {min(temperaturas):.1f}°C")
    print(f"Média: {sum(temperaturas)/len(temperaturas):.1f}°C")
else:
    print("Nenhuma temperatura registrada!")
```

### Exemplo 2: Validador de Dados de Cidade

```python
cidades_validas = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

print("=== Busca de Cidades ===")
print(f"Cidades disponíveis: {', '.join(cidades_validas)}\n")

while True:
    cidade = input("Digite o nome da cidade (ou 'sair'): ")

    if cidade.lower() == 'sair':
        print("Encerrando...")
        break

    # Normaliza o nome (primeira letra maiúscula)
    cidade_normalizada = cidade.strip().title()

    if cidade_normalizada in cidades_validas:
        print(f"✅ Cidade encontrada: {cidade_normalizada}")
        print("🌤️  Buscando previsão...")
        # Aqui entraria a chamada da API
    else:
        print(f"❌ Cidade '{cidade_normalizada}' não encontrada!")
        print("Dica: Verifique a ortografia")

    print("-" * 40)
```

### Exemplo 3: Processamento de Previsão Horária

```python
# Simulando dados da API
previsao_24h = {
    'horas': list(range(24)),
    'temperaturas': [20 + (i * 0.5) if i < 12 else 26 - (i * 0.3) for i in range(24)]
}

print("Previsão Horária (24h)")
print("=" * 50)

for hora, temp in zip(previsao_24h['horas'], previsao_24h['temperaturas']):
    if 6 <= hora < 12:
        periodo = "🌅 Manhã"
    elif 12 <= hora < 18:
        periodo = "☀️ Tarde"
    elif 18 <= hora < 24:
        periodo = "🌆 Noite"
    else:
        periodo = "🌙 Madrugada"

    print(f"{hora:02d}:00 - {temp:5.1f}°C - {periodo}")

print("=" * 50)
```

## 6. Erros Comuns

### Loop Infinito

❌ **ERRADO:**
```python
contador = 0
while contador < 5:
    print(contador)
    # Esqueci de incrementar! Loop infinito!
```

✅ **CERTO:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa
```

### Indentação Errada

❌ **ERRADO:**
```python
for i in range(5):
print(i)  # Falta indentação
```

✅ **CERTO:**
```python
for i in range(5):
    print(i)  # 4 espaços
```

### Usar variável de loop fora do escopo

```python
for i in range(5):
    valor = i * 2

print(valor)  # Funciona, mas valor será o último valor (8)
```

## 7. Exercícios Práticos

### Exercício 1: Números Pares
Imprima todos os números pares de 1 a 50.

<details>
<summary>Ver solução</summary>

```python
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Ou mais simples:
for i in range(2, 51, 2):
    print(i)
```
</details>

### Exercício 2: Contagem Regressiva
Faça uma contagem regressiva de 10 até 0 e mostre "Fogos!" no final.

<details>
<summary>Ver solução</summary>

```python
for i in range(10, -1, -1):
    print(i)

print("🎆 Fogos de artifício!")
```
</details>

### Exercício 3: Fatorial
Calcule o fatorial de um número.

<details>
<summary>Ver solução</summary>

```python
numero = int(input("Número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"{numero}! = {fatorial}")
```
</details>

### Exercício 4: Sequência de Fibonacci
Gere os primeiros 10 números da sequência Fibonacci.

<details>
<summary>Ver solução</summary>

```python
a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

# Saída: 0 1 1 2 3 5 8 13 21 34
```
</details>

## 8. Resumo

| Estrutura | Uso | Exemplo |
|-----------|-----|---------|
| `if` | Uma condição | `if x > 10:` |
| `elif` | Condição alternativa | `elif x == 10:` |
| `else` | Caso contrário | `else:` |
| `for` | Loop com quantidade conhecida | `for i in range(10):` |
| `while` | Loop com condição | `while x < 10:` |
| `break` | Interrompe loop | `if x == 5: break` |
| `continue` | Pula iteração | `if par: continue` |

## Próximos Passos

1. ✅ Pratique todos os exemplos
2. ✅ Modifique os códigos e teste
3. ✅ Resolva os exercícios
4. ✅ Avance para o **Guia 04** (Funções e Módulos)

---

**Próximo guia:** [04-funcoes-modulos.md](./04-funcoes-modulos.md) - Criando e organizando código
