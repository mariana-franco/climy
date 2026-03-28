# 🐍 Guia 06: Programação Orientada a Objetos (POO)

Programação Orientada a Objetos é um paradigma que organiza o código em "objetos" que representam coisas do mundo real.

## 1. Conceitos Fundamentais

### O Que é POO?

POO organiza o código em torno de **objetos** que combinam:
- **Dados** (atributos/propriedades)
- **Comportamentos** (métodos/funções)

### Os 4 Pilares da POO

1. **Classe** - Molde/modelo para criar objetos
2. **Objeto** - Instância de uma classe
3. **Herança** - Reutilizar código de classes pai
4. **Polimorfismo** - Mesma interface, diferentes implementações
5. **Encapsulamento** - Proteger dados internos

## 2. Classes e Objetos

### Criando uma Classe

```python
class Pessoa:
    """Classe que representa uma pessoa."""

    # Método construtor (inicializa o objeto)
    def __init__(self, nome, idade):
        self.nome = nome      # Atributo
        self.idade = idade    # Atributo

    # Método (função dentro da classe)
    def apresentar(self):
        """Apresenta a pessoa."""
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."

# Criando objetos (instâncias)
pessoa1 = Pessoa("Maria", 25)
pessoa2 = Pessoa("João", 30)

# Usando objetos
print(pessoa1.nome)        # "Maria"
print(pessoa1.apresentar())  # "Olá, sou Maria e tenho 25 anos."
print(pessoa2.apresentar())  # "Olá, sou João e tenho 30 anos."
```

### Entendendo `self`

- `self` é uma referência ao **próprio objeto**
- Permite acessar atributos e métodos do objeto
- É sempre o **primeiro parâmetro** de métodos
- Por convenção usamos `self`, mas poderia ser qualquer nome

```python
class Exemplo:
    def __init__(self, valor):
        self.valor = valor  # self.valor é atributo do objeto

    def mostrar(self):
        print(self.valor)  # Acessa o atributo do próprio objeto
```

### Atributos de Classe vs Instância

```python
class Cachorro:
    # Atributo de classe (compartilhado por todos)
    especie = "Canis lupus familiaris"

    def __init__(self, nome, idade):
        # Atributos de instância (único para cada objeto)
        self.nome = nome
        self.idade = idade

rex = Cachorro("Rex", 5)
bob = Cachorro("Bob", 3)

print(rex.especie)  # "Canis lupus familiaris" (mesmo para todos)
print(bob.nome)     # "Bob" (único para este objeto)
```

## 3. Métodos Especiais

Métodos com duplo underline (`__`) são chamados automaticamente.

### `__init__` - Construtor

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        print(f"Produto {self.nome} criado!")

p1 = Produto("Notebook", 5000)  # Imprime a mensagem
```

### `__str__` - Representação em String

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

p = Pessoa("Maria", 25)
print(p)  # "Maria (25 anos)" - chama __str__ automaticamente
```

### `__repr__` - Representação para Desenvolvedores

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

p = Ponto(10, 20)
print(repr(p))  # "Ponto(10, 20)"
```

### `__eq__` - Comparação de Igualdade

```python
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return self.cpf == other.cpf
        return False

p1 = Pessoa("Maria", "123.456.789-00")
p2 = Pessoa("Maria", "123.456.789-00")
p3 = Pessoa("João", "987.654.321-00")

print(p1 == p2)  # True (mesmo CPF)
print(p1 == p3)  # False (CPF diferente)
```

### Outros Métodos Especiais

```python
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Soma dois vetores (operador +)"""
        return Vetor(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Multiplica por escalar (operador *)"""
        return Vetor(self.x * scalar, self.y * scalar)

    def __len__(self):
        """Retorna magnitude (função len())"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

v1 = Vetor(3, 4)
v2 = Vetor(1, 2)

v3 = v1 + v2  # Usa __add__
print(v3.x, v3.y)  # 4, 6

v4 = v1 * 2  # Usa __mul__
print(v4.x, v4.y)  # 6, 8

print(len(v1))  # 5 (usa __len__)
```

## 4. Encapsulamento

Proteger atributos e métodos de acesso direto.

### Atributos Públicos vs Privados

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular      # Público (acesso livre)
        self.__saldo = saldo        # Privado (não acessar diretamente)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def get_saldo(self):  # Método getter
        return self.__saldo

    def set_saldo(self, valor):  # Método setter (com validação)
        if valor >= 0:
            self.__saldo = valor

conta = ContaBancaria("Maria", 1000)

# Acesso público (permitido)
print(conta.titular)  # "Maria"

# Acesso privado (NÃO fazer!)
# print(conta.__saldo)  # ERRO!

# Forma correta
print(conta.get_saldo())  # 1000
conta.depositar(500)
print(conta.get_saldo())  # 1500
```

### Properties (Forma Pythonica)

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco  # Usa o setter

    @property
    def preco(self):
        """Getter - acessa como atributo normal"""
        return self._preco

    @preco.setter
    def preco(self, valor):
        """Setter - valida antes de atribuir"""
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

    @property
    def preco_com_desconto(self):
        """Property só de leitura"""
        return self._preco * 0.9

p = Produto("Notebook", 5000)
print(p.preco)  # 5000 (chama getter)
p.preco = 4500  # Chama setter
print(p.preco_com_desconto)  # 4050
```

## 5. Herança

Reutilizar código de uma classe pai.

### Herança Simples

```python
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som genérico"

    def dormir(self):
        return f"{self.nome} está dormindo"

class Cachorro(Animal):  # Herda de Animal
    def falar(self):  # Sobrescreve método do pai
        return "Au au!"

    def buscar_bolinha(self):  # Método exclusivo
        return f"{self.nome} foi buscar a bolinha"

class Gato(Animal):  # Também herda de Animal
    def falar(self):
        return "Miau!"

    def arranhar_sofa(self):
        return f"{self.nome} está arranhando o sofá"

# Uso
rex = Cachorro("Rex", 5)
bob = Gato("Bob", 3)

print(rex.falar())  # "Au au!" (método do filho)
print(rex.dormir())  # "Rex está dormindo" (método do pai)
print(bob.falar())  # "Miau!"
print(bob.arranhar_sofa())  # Método exclusivo do gato
```

### Usando `super()`

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, cargo):
        super().__init__(nome, idade)  # Chama construtor do pai
        self.salario = salario
        self.cargo = cargo

    def apresentar(self):
        return f"{self.nome}, {self.cargo}, R$ {self.salario:.2f}"

f = Funcionario("Maria", 30, 5000, "Gerente")
print(f.apresentar())  # "Maria, Gerente, R$ 5000.00"
```

### Herança Múltipla

```python
class Terrestre:
    def andar(self):
        return "Andando no chão"

class Aquatico:
    def nadar(self):
        return "Nadando na água"

class Anfibio(Terrestre, Aquatico):
    pass

sapo = Anfibio()
print(sapo.andar())  # "Andando no chão"
print(sapo.nadar())  # "Nadando na água"
```

## 6. Polimorfismo

Mesma interface, diferentes implementações.

### Polimorfismo com Herança

```python
class Animal:
    def falar(self):
        pass  # Método abstrato

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Vaca(Animal):
    def falar(self):
        return "Muuu!"

# Polimorfismo em ação
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.falar())  # Cada um fala de um jeito
# Au au!
# Miau!
# Muuu!
```

### Polimorfismo sem Herança

```python
class Carro:
    def mover(self):
        return "Carro movendo na rua"

class Barco:
    def mover(self):
        return "Barco movendo no mar"

class Aviao:
    def mover(self):
        return "Avião voando no céu"

# Todos têm método mover()
veiculos = [Carro(), Barco(), Aviao()]

for veiculo in veiculos:
    print(veiculo.mover())
```

## 7. Classes Abstratas

Classes que não podem ser instanciadas, só herdadas.

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    """Classe abstrata - não pode ser instanciada"""

    @abstractmethod
    def area(self):
        """Calcula área (obrigatório implementar)"""
        pass

    @abstractmethod
    def perimetro(self):
        """Calcula perímetro (obrigatório implementar)"""
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raio

# Uso
ret = Retangulo(5, 10)
print(ret.area())  # 50

circ = Circulo(7)
print(circ.area())  # 153.86

# forma = FormaGeometrica()  # ERRO! Classe abstrata
```

## 8. Exemplos Práticos (Climy)

### Exemplo 1: Modelo de Dados Climáticos

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DadosClimaticos:
    """Classe de dados climáticos (dataclass é moderno e prático)."""
    temperatura: float
    umidade: float
    vento: float
    pressao: float
    timestamp: datetime

    @property
    def sensacao_termica(self) -> float:
        """Calcula sensação térmica."""
        if self.temperatura <= 10 and self.vento > 4.8:
            # Wind chill
            v = self.vento ** 0.16
            return round(
                13.12 + 0.6215 * self.temperatura
                - 11.37 * v + 0.3965 * self.temperatura * v,
                1
            )
        return self.temperatura

    def __str__(self) -> str:
        return (
            f"🌡️ {self.temperatura:.1f}°C | "
            f"💧 {self.umidade}% | "
            f"💨 {self.vento:.1f} km/h"
        )

# Uso
dados = DadosClimaticos(
    temperatura=28.5,
    umidade=65,
    vento=12.3,
    pressao=1013.25,
    timestamp=datetime.now()
)

print(dados)  # Usa __str__
print(f"Sensação: {dados.sensacao_termica:.1f}°C")
```

### Exemplo 2: API Client com POO

```python
import requests
from typing import Dict, Any

class APIClient:
    """Cliente genérico para APIs."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str, params: Dict = None) -> Dict[str, Any]:
        """Faz requisição GET."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise APIError(f"Erro na requisição: {e}")

    def post(self, endpoint: str, data: Dict = None) -> Dict[str, Any]:
        """Faz requisição POST."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise APIError(f"Erro na requisição: {e}")

class APIError(Exception):
    """Erro customizado para API."""
    pass

# Uso
client = APIClient("https://api.exemplo.com", timeout=5)
dados = client.get("/clima", {"cidade": "São Paulo"})
```

### Exemplo 3: Sistema de Cache

```python
from datetime import datetime, timedelta
from typing import Any, Optional

class Cache:
    """Sistema de cache com TTL (Time To Live)."""

    def __init__(self, ttl_segundos: int = 300):
        self._dados = {}
        self._tempos = {}
        self.ttl = ttl_segundos

    def set(self, chave: str, valor: Any):
        """Armazena valor no cache."""
        self._dados[chave] = valor
        self._tempos[chave] = datetime.now()

    def get(self, chave: str, default: Any = None) -> Optional[Any]:
        """Recupera valor do cache (se não expirou)."""
        if chave not in self._dados:
            return default

        # Verifica se expirou
        tempo_decorrido = datetime.now() - self._tempos[chave]
        if tempo_decorrido.total_seconds() > self.ttl:
            self.delete(chave)  # Remove se expirou
            return default

        return self._dados[chave]

    def delete(self, chave: str):
        """Remove do cache."""
        self._dados.pop(chave, None)
        self._tempos.pop(chave, None)

    def clear(self):
        """Limpa todo o cache."""
        self._dados.clear()
        self._tempos.clear()

    def __contains__(self, chave: str) -> bool:
        """Verifica se chave existe (operador in)."""
        return chave in self._dados and self.get(chave) is not None

# Uso no Climy
cache = Cache(ttl_segundos=300)  # 5 minutos

# Armazenar
cache.set("clima_sao_paulo", {"temp": 28.5})

# Recuperar
dados = cache.get("clima_sao_paulo")
if dados:
    print(f"Do cache: {dados}")
else:
    print("Cache expirou ou não existe")
```

## 9. Boas Práticas de POO

### Nomes de Classes

✅ **CERTO:**
```python
class Pessoa:
    pass

class ContaBancaria:
    pass

class GerenciadorDeCidades:
    pass
```

❌ **ERRADO:**
```python
class pessoa:  # Minúscula
    pass

class Conta_Bancaria:  # Snake case
    pass
```

### Princípio da Responsabilidade Única

Cada classe deve ter **uma única responsabilidade**.

✅ **CERTO:**
```python
class Usuario:
    """Só gerencia dados do usuário"""
    pass

class UsuarioRepositorio:
    """Só gerencia banco de dados de usuários"""
    pass

class UsuarioEmail:
    """Só envia emails para usuários"""
    pass
```

❌ **ERRADO:**
```python
class Usuario:
    # Faz tudo (não faça isso!)
    def salvar_no_banco(self): pass
    def enviar_email(self): pass
    def validar_dados(self): pass
```

### Composição vs Herança

Prefira **composição** (ter um) em vez de **herança** (ser um).

✅ **CERTO (Composição):**
```python
class Motor:
    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self):
        self.motor = Motor()  # Carro TEM um motor

    def ligar(self):
        return self.motor.ligar()
```

❌ **ERRADO (Herança forçada):**
```python
class Carro(Motor):  # Carro NÃO É UM motor
    pass
```

## 10. Exercícios Práticos

### Exercício 1: Classe Retângulo
Crie uma classe Retângulo com base, altura, métodos de área e perímetro.

<details>
<summary>Ver solução</summary>

```python
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Retângulo {self.base}x{self.altura}"

r = Retangulo(5, 10)
print(r.area())  # 50
print(r.perimetro())  # 30
```
</details>

### Exercício 2: Sistema Bancário
Crie classes Conta, ContaCorrente e ContaPoupanca com métodos de depósito e saque.

<details>
<summary>Ver solução</summary>

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def get_saldo(self):
        return self._saldo

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self._saldo + self.limite:
            self._saldo -= valor
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        self._saldo *= (1 + self.taxa_juros)
```
</details>

### Exercício 3: Modelo de Previsão (Climy)
Crie uma classe PrevisaoClimatica com dados e métodos de análise.

<details>
<summary>Ver solução</summary>

```python
class PrevisaoClimatica:
    def __init__(self, cidade, temperatura, umidade, vento):
        self.cidade = cidade
        self.temperatura = temperatura
        self.umidade = umidade
        self.vento = vento

    def classificar(self):
        if self.temperatura < 15:
            return "Frio"
        elif self.temperatura < 25:
            return "Agradável"
        else:
            return "Quente"

    def __str__(self):
        return (
            f"🌤️ {self.cidade}: {self.temperatura}°C - "
            f"{self.classificar()}"
        )

p = PrevisaoClimatica("São Paulo", 28.5, 65, 12.3)
print(p)  # 🌤️ São Paulo: 28.5°C - Quente
```
</details>

## 11. Resumo

| Conceito | Descrição | Exemplo |
|----------|-----------|---------|
| Classe | Molde de objeto | `class Pessoa:` |
| Objeto | Instância de classe | `p = Pessoa()` |
| Atributo | Dado do objeto | `self.nome` |
| Método | Função do objeto | `def falar():` |
| Herança | Reutilizar classe pai | `class Filho(Pai):` |
| Polimorfismo | Mesma interface | `animal.falar()` |
| Encapsulamento | Proteger dados | `__atributo` |
| Property | Getter/Setter | `@property` |

## Próximos Passos

1. ✅ Pratique criando classes
2. ✅ Use POO no Climy
3. ✅ Estude o **Guia 07** (Tratamento de Erros)

---

**Próximo guia:** [07-tratamento-erros.md](./07-tratamento-erros.md) - Exceções e debugging
