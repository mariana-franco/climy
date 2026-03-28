# 🐍 Guia 05: Estruturas de Dados - Listas, Dicionários e Mais

Python tem estruturas de dados poderosas e flexíveis. Vamos dominá-las!

## 1. Listas

Listas são coleções ordenadas e mutáveis de itens.

### Criando Listas

```python
# Lista vazia
lista = []

# Lista com elementos
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", 3.14, True]

# Usando list()
lista = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

### Acessando Elementos

```python
frutas = ["maçã", "banana", "laranja", "uva"]

# Índice positivo (começa em 0)
print(frutas[0])  # "maçã"
print(frutas[2])  # "laranja"

# Índice negativo (conta do fim)
print(frutas[-1])  # "uva"
print(frutas[-2])  # "laranja"

# Fatiamento (slicing)
print(frutas[0:2])   # ["maçã", "banana"]
print(frutas[:3])    # ["maçã", "banana", "laranja"]
print(frutas[2:])    # ["laranja", "uva"]
print(frutas[:])     # ["maçã", "banana", "laranja", "uva"] (cópia)
```

### Modificando Listas

```python
frutas = ["maçã", "banana", "laranja"]

# Adicionar elementos
frutas.append("uva")           # Adiciona no final
frutas.insert(1, "morango")    # Adiciona na posição 1

# Remover elementos
frutas.remove("banana")        # Remove pelo valor
ultimo = frutas.pop()          # Remove e retorna o último
del frutas[0]                  # Remove pelo índice

# Modificar elemento
frutas[0] = "pera"

print(frutas)  # ["pera", "morango", "laranja"]
```

### Métodos de Lista

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

numeros.append(7)        # Adiciona 7 no final
numeros.insert(0, 0)     # Insere 0 na posição 0
numeros.remove(1)        # Remove primeira ocorrência de 1
numeros.pop()            # Remove e retorna último
numeros.count(1)         # Quantas vezes 1 aparece?
numeros.index(4)         # Índice da primeira ocorrência de 4
numeros.sort()           # Ordena crescente
numeros.reverse()        # Inverte a ordem
numeros.copy()           # Cria cópia da lista
numeros.clear()          # Remove todos os elementos

# Tamanho
len(numeros)             # Quantidade de elementos
```

### List Comprehensions (MUITO IMPORTANTE!)

Forma concisa de criar listas.

```python
# Forma tradicional
quadrados = []
for i in range(10):
    quadrados.append(i ** 2)

# Com list comprehension (recomendado)
quadrados = [i ** 2 for i in range(10)]

# Com condição
pares = [i for i in range(20) if i % 2 == 0]

# Transformando elementos
frutas = ["maçã", "banana", "laranja"]
upper = [fruta.upper() for fruta in frutas]
# ['MAÇÃ', 'BANANA', 'LARANJA']

# Aninhada
matriz = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### Exemplos Práticos

```python
# Processando temperaturas (Climy)
temperaturas = [22.5, 24.0, 26.3, 28.1, 25.7, 23.9, 21.5]

# Filtrar temperaturas acima de 25
quentes = [t for t in temperaturas if t > 25]

# Arredondar todas
arredondadas = [round(t) for t in temperaturas]

# Converter para Fahrenheit
fahrenheit = [(t * 9/5) + 32 for t in temperaturas]

# Média das temperaturas
media = sum(temperaturas) / len(temperaturas)

# Temperatura máxima e mínima
maxima = max(temperaturas)
minima = min(temperaturas)
```

## 2. Tuplas

Tuplas são como listas, mas **imutáveis** (não podem ser alteradas).

### Criando Tuplas

```python
# Com parênteses
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")

# Sem parênteses (tuple packing)
ponto = 10, 20, 30

# Tupla vazia
vazia = ()

# Tupla com um elemento (precisa da vírgula!)
singleton = (42,)  # Não esqueça a vírgula!
```

### Acessando Elementos

```python
coordenadas = (10, 20, 30)

print(coordenadas[0])  # 10
print(coordenadas[-1])  # 30
print(coordenadas[1:3])  # (20, 30)

# Não pode modificar!
# coordenadas[0] = 5  # ERRO!
```

### Desempacotamento (Unpacking)

```python
# Desempacotando tupla
coordenadas = (10, 20, 30)
x, y, z = coordenadas

print(x)  # 10
print(y)  # 20
print(z)  # 30

# Ignorando valores
_, y, _ = coordenadas  # Só importa o y

# Múltipla atribuição
a, b = 1, 2
a, b = b, a  # Troca valores! a=2, b=1
```

### Quando Usar Tuplas

- Dados que não devem mudar (coordenadas, cores RGB, configurações)
- Retornar múltiplos valores de funções
- Chaves de dicionário (listas não podem!)

```python
def retornar_dados():
    return (10, 20, 30)  # Tupla é mais eficiente

x, y, z = retornar_dados()
```

## 3. Dicionários

Dicionários armazenam pares **chave-valor**. São como listas, mas você acessa por uma chave, não por índice.

### Criando Dicionários

```python
# Dicionário vazio
dicionario = {}

# Com elementos
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo"
}

# Usando dict()
dicionario = dict(nome="João", idade=30)
```

### Acessando Valores

```python
pessoa = {"nome": "Maria", "idade": 25, "cidade": "SP"}

# Pela chave
print(pessoa["nome"])  # "Maria"

# Com get (não gera erro se não existir)
print(pessoa.get("nome"))     # "Maria"
print(pessoa.get("email"))    # None
print(pessoa.get("email", "N/A"))  # "N/A" (valor padrão)
```

### Modificando Dicionários

```python
pessoa = {"nome": "Maria", "idade": 25}

# Adicionar/Modificar
pessoa["idade"] = 26           # Modifica
pessoa["email"] = "maria@email.com"  # Adiciona

# Remover
del pessoa["cidade"]           # Remove pela chave
idade = pessoa.pop("idade")    # Remove e retorna valor

# Verificar se existe
"nome" in pessoa  # True
"email" in pessoa  # False
```

### Métodos de Dicionário

```python
pessoa = {"nome": "Maria", "idade": 25, "cidade": "SP"}

pessoa.keys()    # dict_keys(['nome', 'idade', 'cidade'])
pessoa.values()  # dict_values(['Maria', 25, 'SP'])
pessoa.items()   # dict_items([('nome', 'Maria'), ('idade', 25), ('cidade', 'SP')])

# Iterando
for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Outros métodos
pessoa.get("nome", "Padrão")  # Retorna valor ou padrão
pessoa.update({"email": "m@email.com"})  # Atualiza com outro dict
pessoa.copy()  # Cria cópia
pessoa.clear()  # Remove tudo
```

### Dictionary Comprehensions

```python
# Criar dicionário rapidamente
quadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Transformar listas em dict
chaves = ["a", "b", "c"]
valores = [1, 2, 3]
dicionario = {k: v for k, v in zip(chaves, valores)}
# {'a': 1, 'b': 2, 'c': 3}

# Filtrar
pares = {x: x for x in range(10) if x % 2 == 0}
# {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}
```

### Exemplos Práticos (Climy)

```python
# Dados de previsão do tempo
previsao = {
    "cidade": "São Paulo",
    "temperatura": 28.5,
    "umidade": 65,
    "vento": 12.3,
    "condicao": "Parcialmente nublado"
}

# Acessando dados
print(f"{previsao['cidade']}: {previsao['temperatura']}°C")

# Iterando
for chave, valor in previsao.items():
    print(f"{chave}: {valor}")

# Dados horários (lista de dicts)
previsao_horaria = [
    {"hora": 0, "temp": 22.5, "condicao": "Limpo"},
    {"hora": 6, "temp": 20.1, "condicao": "Nublado"},
    {"hora": 12, "temp": 28.3, "condicao": "Sol"},
    {"hora": 18, "temp": 25.7, "condicao": "Parcial"},
]

# Filtrar horas com temperatura > 25
horas_quentes = [p for p in previsao_horaria if p["temp"] > 25]

# Extrair só temperaturas
temperaturas = [p["temp"] for p in previsao_horaria]
```

## 4. Sets (Conjuntos)

Sets são coleções **não ordenadas** e **sem elementos duplicados**.

### Criando Sets

```python
# Com chaves
frutas = {"maçã", "banana", "laranja"}

# Com set()
numeros = set([1, 2, 3, 2, 1])  # {1, 2, 3} (remove duplicatas)

# Vazio (cuidado!)
vazio = set()  # {} é dicionário vazio!
```

### Operações de Set

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# União
A | B  # {1, 2, 3, 4, 5, 6, 7, 8}
A.union(B)

# Interseção
A & B  # {4, 5}
A.intersection(B)

# Diferença
A - B  # {1, 2, 3} (está em A mas não em B)
A.difference(B)

# Diferença simétrica
A ^ B  # {1, 2, 3, 6, 7, 8} (está em um ou outro, mas não em ambos)
A.symmetric_difference(B)

# Subconjunto
{1, 2} <= A  # True (está contido)

# Superconjunto
A >= {1, 2}  # True (contém)
```

### Métodos de Set

```python
frutas = {"maçã", "banana"}

frutas.add("laranja")      # Adiciona
frutas.remove("maçã")      # Remove (erro se não existir)
frutas.discard("uva")      # Remove (sem erro)
frutas.pop()               # Remove e retorna um aleatório
frutas.clear()             # Limpa

# Verificar pertinência
"maçã" in frutas  # True
```

### Quando Usar Sets

- Remover duplicatas de lista
- Testar pertinência rapidamente
- Operações matemáticas de conjuntos

```python
# Remover duplicatas
lista = [1, 2, 2, 3, 3, 3]
unicos = list(set(lista))  # [1, 2, 3]

# Verificar se cidade já foi processada
cidades_processadas = set()

def processar_cidade(cidade):
    if cidade in cidades_processadas:
        return  # Já processada
    cidades_processadas.add(cidade)
    # Processa cidade...
```

## 5. Estruturas Aninhadas

Combinando listas, dicts e tuplas.

### Exemplo 1: Dados Complexos (Climy)

```python
dados_climy = {
    "cidade": {
        "nome": "São Paulo",
        "estado": "SP",
        "pais": "Brasil",
        "coordenadas": (-23.5505, -46.6333)
    },
    "previsao": {
        "atual": {
            "temperatura": 28.5,
            "sensacao_termica": 30.2,
            "umidade": 65,
            "vento": 12.3
        },
        "horaria": [
            {"hora": 0, "temp": 22.5},
            {"hora": 1, "temp": 21.8},
            # ... mais 22 horas
        ],
        "diaria": [
            {"dia": "Seg", "min": 18, "max": 28},
            {"dia": "Ter", "min": 19, "max": 30},
            # ... mais 5 dias
        ]
    }
}

# Acessando dados profundos
temp_atual = dados_climy["previsao"]["atual"]["temperatura"]
lat, lon = dados_climy["cidade"]["coordenadas"]
primeira_hora = dados_climy["previsao"]["horaria"][0]["temp"]
```

### Exemplo 2: Matriz (Lista de Listas)

```python
# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][0])  # 1 (linha 0, coluna 0)
print(matriz[1][2])  # 6 (linha 1, coluna 2)

# Iterando
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
```

## 6. Collections (Módulo Avançado)

Python tem estruturas de dados adicionais no módulo `collections`.

### Counter

```python
from collections import Counter

temperaturas = [22, 25, 25, 28, 28, 28, 30]
contador = Counter(temperaturas)

print(contador)  # Counter({28: 3, 25: 2, 22: 1, 30: 1})
print(contador[28])  # 3 (quantas vezes apareceu)

# Mais comum
print(contador.most_common(1))  # [(28, 3)]
```

### defaultdict

```python
from collections import defaultdict

# Dicionário com valor padrão
dicionario = defaultdict(int)  # int() retorna 0

dicionario["a"] += 1
dicionario["b"] += 2
print(dicionario["c"])  # 0 (não existe, retorna padrão)

# Útil para contagens
contagem = defaultdict(int)
for letra in "banana":
    contagem[letra] += 1
# {'b': 1, 'a': 3, 'n': 2}
```

### deque

```python
from collections import deque

# Fila eficiente (dupla extremidade)
fila = deque([1, 2, 3])

fila.append(4)      # Adiciona no final
fila.appendleft(0)  # Adiciona no início
fila.pop()          # Remove do final
fila.popleft()      # Remove do início
```

## 7. Exemplos Práticos Completos

### Exemplo 1: Gerenciador de Cidades (Climy)

```python
class GerenciadorCidades:
    def __init__(self):
        self.cidades = {}
        self.historico = []

    def adicionar_cidade(self, nome, dados):
        """Adiciona cidade com seus dados."""
        self.cidades[nome] = dados
        self.historico.append({
            "acao": "adicionar",
            "cidade": nome,
            "dados": dados
        })

    def buscar_cidade(self, nome):
        """Busca cidade por nome."""
        return self.cidades.get(nome)

    def listar_cidades(self):
        """Lista todas as cidades."""
        return list(self.cidades.keys())

    def temperaturas_acima_de(self, valor):
        """Retorna cidades com temperatura acima do valor."""
        return [
            nome for nome, dados in self.cidades.items()
            if dados.get("temperatura", 0) > valor
        ]

# Uso
gerenciador = GerenciadorCidades()
gerenciador.adicionar_cidade("São Paulo", {
    "temperatura": 28.5,
    "umidade": 65
})
gerenciador.adicionar_cidade("Rio de Janeiro", {
    "temperatura": 32.1,
    "umidade": 70
})

print(gerenciador.listar_cidades())
# ['São Paulo', 'Rio de Janeiro']

print(gerenciador.temperaturas_acima_de(30))
# ['Rio de Janeiro']
```

### Exemplo 2: Processador de Dados Horários

```python
def processar_previsao_horaria(dados):
    """Processa dados horários da API."""

    # Estrutura de entrada (exemplo)
    # dados = {
    #     'time': ['2026-03-28T00:00', '2026-03-28T01:00', ...],
    #     'temperature_2m': [22.5, 21.8, ...],
    #     'relative_humidity_2m': [65, 68, ...],
    #     'wind_speed_10m': [12.3, 10.5, ...]
    # }

    # Extrair dados em lista de dicts
    previsao = [
        {
            'hora': time.split('T')[1][:5],  # '00:00'
            'temperatura': temp,
            'umidade': umidade,
            'vento': vento
        }
        for time, temp, umidade, vento in zip(
            dados['time'],
            dados['temperature_2m'],
            dados['relative_humidity_2m'],
            dados['wind_speed_10m']
        )
    ]

    # Estatísticas
    temperaturas = [p['temperatura'] for p in previsao]

    return {
        'previsao': previsao,
        'maxima': max(temperaturas),
        'minima': min(temperaturas),
        'media': sum(temperaturas) / len(temperaturas),
        'total_horas': len(previsao)
    }
```

## 8. Exercícios Práticos

### Exercício 1: Manipulação de Lista
Crie uma lista de 10 números e:
- Adicione mais 3 números
- Remova o primeiro e último
- Ordene em ordem crescente
- Calcule a média

<details>
<summary>Ver solução</summary>

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Adicionar
numeros.extend([11, 12, 13])

# Remover
numeros.pop(0)  # Primeiro
numeros.pop()   # Último

# Ordenar
numeros.sort()

# Média
media = sum(numeros) / len(numeros)
print(f"Média: {media:.2f}")
```
</details>

### Exercício 2: Dicionário de Produtos
Crie um dicionário com produtos e preços, depois:
- Aumente 10% dos preços
- Filtre produtos acima de R$ 50
- Calcule o valor total do estoque

<details>
<summary>Ver solução</summary>

```python
produtos = {
    "Produto A": 45.00,
    "Produto B": 60.00,
    "Produto C": 30.00,
    "Produto D": 75.00
}

# Aumentar 10%
produtos = {k: v * 1.10 for k, v in produtos.items()}

# Filtrar acima de 50
caros = {k: v for k, v in produtos.items() if v > 50}

# Total
total = sum(produtos.values())
print(f"Total: R$ {total:.2f}")
```
</details>

### Exercício 3: Analisador de Temperaturas
Dada uma lista de temperaturas, use Counter para encontrar a temperatura mais frequente.

<details>
<summary>Ver solução</summary>

```python
from collections import Counter

temps = [22, 25, 25, 28, 28, 28, 30, 25, 28]
contador = Counter(temps)

mais_frequente, vezes = contador.most_common(1)[0]
print(f"{mais_frequente}°C apareceu {vezes} vezes")
```
</details>

## 9. Resumo

| Estrutura | Mutável | Ordenada | Índice | Sintaxe |
|-----------|---------|----------|--------|---------|
| Lista | ✅ | ✅ | Numérico | `[]` |
| Tupla | ❌ | ✅ | Numérico | `()` |
| Dicionário | ✅ | ❌* | Chave | `{}` |
| Set | ✅ | ❌ | Nenhum | `{}` |

*Python 3.7+ mantém ordem de inserção em dicts

## Próximos Passos

1. ✅ Pratique list/dict comprehensions
2. ✅ Use sets para remover duplicatas
3. ✅ Explore estruturas aninhadas
4. ✅ Avance para o **Guia 06** (Programação Orientada a Objetos)

---

**Próximo guia:** [06-programacao-orientada-objetos.md](./06-programacao-orientada-objetos.md) - Classes e objetos
