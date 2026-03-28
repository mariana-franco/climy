# 🐍 Guia 07: Tratamento de Erros e Exceções

Erros acontecem! Aprenda a lidar com eles de forma elegante e profissional.

## 1. Tipos de Erros

### Erros de Sintaxe

Ocorre quando você escreve código inválido.

```python
# Faltou dois pontos
if True
    print("Olá")  # SyntaxError

# Parênteses não fechados
print("Olá"  # SyntaxError

# Indentação errada
def func():
print("Olá")  # IndentationError
```

**Solução:** Corrija a sintaxe antes de executar.

### Erros de Execução (Exceções)

O código é sintaticamente correto, mas falha durante execução.

```python
# Divisão por zero
resultado = 10 / 0  # ZeroDivisionError

# Acessar índice inexistente
lista = [1, 2, 3]
print(lista[10])  # IndexError

# Chave não existe em dict
dicionario = {"a": 1}
print(dicionario["b"])  # KeyError

# Converter texto inválido
numero = int("abc")  # ValueError

# Arquivo não existe
arquivo = open("inexistente.txt")  # FileNotFoundError

# Importar módulo inexistente
import modulo_que_nao_existe  # ModuleNotFoundError
```

## 2. Try/Except - Capturando Exceções

### Estrutura Básica

```python
try:
    # Código que pode gerar erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    # Executa se houver divisão por zero
    print("Não é possível dividir por zero!")
except ValueError:
    # Executa se a conversão falhar
    print("Por favor, digite um número válido!")
except:
    # Captura QUALQUER erro (evite usar assim)
    print("Ocorreu um erro inesperado!")
```

### Múltiplas Exceções

```python
try:
    valor = int(input("Valor: "))
    resultado = 100 / valor
except (ValueError, ZeroDivisionError):
    print("Erro: Valor inválido ou divisão por zero!")
```

### Usando `else` (Se Não Houver Erro)

```python
try:
    numero = int(input("Número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print("Ocorreu um erro!")
else:
    # Executa só se NÃO houver exceção
    print(f"Resultado: {resultado}")
    print("Operação realizada com sucesso!")
```

### Usando `finally` (Sempre Executa)

```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print(conteudo)
finally:
    # Sempre executa, com erro ou não
    print("Operação finalizada!")
    if 'arquivo' in locals():
        arquivo.close()  # Garante que fecha o arquivo
```

## 3. Capturando a Exceção

```python
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Tipo do erro: {type(e).__name__}")  # ZeroDivisionError
    print(f"Mensagem: {e}")  # division by zero
    print(f"Detalhes: {e.args}")  # ('division by zero',)
```

### Hierarquia de Exceções

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- ValueError
      +-- TypeError
      +-- FileNotFoundError
      +-- KeyError
      +-- IndexError
      +-- ... e muitas outras
```

**Dica:** Capture exceções específicas primeiro, genéricas depois.

```python
try:
    # Código
except ZeroDivisionError:  # Específica primeiro
    print("Divisão por zero")
except ArithmeticError:  # Genérica depois
    print("Erro aritmético")
except Exception:  # Mais genérica ainda
    print("Qualquer erro")
```

## 4. Levantando Exceções (raise)

### Criando Exceções Manualmente

```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("Valor deve ser positivo")
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(100, 150)
except ValueError as e:
    print(f"Erro: {e}")
```

### Criando Exceções Customizadas

```python
class SaldoInsuficienteError(Exception):
    """Exceção customizada para saldo insuficiente."""
    def __init__(self, saldo, valor_saque):
        self.saldo = saldo
        self.valor_saque = valor_saque
        super().__init__(
            f"Saldo {saldo} insuficiente para saque de {valor_saque}"
        )

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    return saldo - valor

try:
    sacar(100, 150)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
    print(f"Saldo: {e.saldo}, Saque: {e.valor_saque}")
```

## 5. Boas Práticas

### ✅ CERTO

```python
# Capture exceções específicas
try:
    resultado = int(valor) / divisor
except ValueError:
    print("Valor inválido")
except ZeroDivisionError:
    print("Divisão por zero")

# Use finally para limpeza
try:
    arquivo = open("dados.txt")
    processar(arquivo)
finally:
    arquivo.close()

# Documente exceções customizadas
class APIError(Exception):
    """Erro na comunicação com API externa."""
    pass
```

### ❌ ERRADO

```python
# Não capture tudo sem necessidade
try:
    # código
except:  # MUITO genérico!
    pass  # Silenciar erros é perigoso!

# Não ignore exceções
try:
    perigoso()
except:
    pass  # Nunca faça isso!

# Não use try/except para fluxo normal
# ERRADO:
try:
    valor = dicionario[chave]
except KeyError:
    valor = None

# CERTO:
valor = dicionario.get(chave, None)
```

## 6. Exemplos Práticos (Climy)

### Exemplo 1: API com Tratamento de Erros

```python
import requests
from typing import Dict, Any

class WeatherAPIError(Exception):
    """Erro na API de clima."""
    pass

class WeatherAPITimeoutError(WeatherAPIError):
    """Timeout na API."""
    pass

class WeatherAPIConnectionError(WeatherAPIError):
    """Erro de conexão."""
    pass

def buscar_temperatura(cidade: str, timeout: int = 5) -> Dict[str, Any]:
    """Busca temperatura na API com tratamento robusto de erros."""

    url = f"https://api.open-meteo.com/v1/forecast"
    params = {"q": cidade}

    try:
        response = requests.get(url, params=params, timeout=timeout)

        # Verifica status HTTP
        response.raise_for_status()

        return response.json()

    except requests.Timeout:
        raise WeatherAPITimeoutError(
            f"Timeout após {timeout}s ao buscar {cidade}"
        )

    except requests.ConnectionError:
        raise WeatherAPIConnectionError(
            f"Erro de conexão ao buscar {cidade}"
        )

    except requests.HTTPError as e:
        if e.response.status_code == 404:
            raise WeatherAPIError(f"Cidade '{cidade}' não encontrada")
        raise WeatherAPIError(f"Erro HTTP {e.response.status_code}")

    except requests.RequestException as e:
        raise WeatherAPIError(f"Erro inesperado: {e}")

# Uso
try:
    dados = buscar_temperatura("São Paulo", timeout=5)
    print(f"Temperatura: {dados['current_weather']['temperature']}°C")
except WeatherAPITimeoutError as e:
    print(f"⏱️  {e}")
except WeatherAPIConnectionError as e:
    print(f"🔌 {e}")
except WeatherAPIError as e:
    print(f"❌ {e}")
```

### Exemplo 2: Validação com Exceções

```python
class ValidacaoError(Exception):
    """Erro de validação de dados."""
    pass

def validar_temperatura(temp: float) -> float:
    """Valida faixa de temperatura razoável."""
    if not isinstance(temp, (int, float)):
        raise ValidacaoError(f"Temperatura deve ser numérica, got {type(temp)}")

    if temp < -100 or temp > 60:
        raise ValidacaoError(
            f"Temperatura {temp}°C fora de faixa razoável (-100 a 60)"
        )

    return temp

def validar_cidade(cidade: str) -> str:
    """Valida nome de cidade."""
    if not isinstance(cidade, str):
        raise ValidacaoError("Cidade deve ser string")

    cidade = cidade.strip()

    if len(cidade) < 2:
        raise ValidacaoError("Nome de cidade muito curto")

    if len(cidade) > 100:
        raise ValidacaoError("Nome de cidade muito longo")

    return cidade

# Uso
try:
    cidade = validar_cidade("  SP  ")
    temp = validar_temperatura(28.5)
    print(f"{cidade}: {temp}°C")
except ValidacaoError as e:
    print(f"❌ Validação falhou: {e}")
```

### Exemplo 3: Context Manager para Recursos

```python
from contextlib import contextmanager

@contextmanager
def abrir_arquivo_seguro(arquivo, modo='r'):
    """Context manager que trata erros de arquivo automaticamente."""
    f = None
    try:
        f = open(arquivo, modo, encoding='utf-8')
        yield f
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado")
        yield None
    except PermissionError:
        print(f"Sem permissão para '{arquivo}'")
        yield None
    except UnicodeDecodeError:
        print(f"Erro de codificação em '{arquivo}'")
        yield None
    finally:
        if f:
            f.close()
            print(f"Arquivo '{arquivo}' fechado")

# Uso
with abrir_arquivo_seguro("dados.txt") as f:
    if f:
        conteudo = f.read()
        print(conteudo)
```

## 7. Logging (Registrando Erros)

Em vez de só printar erros, use logging profissional.

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',  # Salva em arquivo
    filemode='a'
)

logger = logging.getLogger(__name__)

def processar_dados(dados):
    try:
        resultado = perigoso(dados)
        logger.info(f"Processamento bem-sucedido: {resultado}")
        return resultado
    except ValueError as e:
        logger.error(f"Erro de valor: {e}", exc_info=True)
        raise
    except Exception as e:
        logger.critical(f"Erro crítico: {e}", exc_info=True)
        raise

# Níveis de logging
logger.debug("Detalhes para debug")
logger.info("Informação geral")
logger.warning("Aviso importante")
logger.error("Erro ocorreu")
logger.critical("Erro crítico")
```

## 8. Debugging com Traceback

### Capturando Traceback Completo

```python
import traceback

try:
    1 / 0
except Exception:
    print("Ocorreu um erro:")
    traceback.print_exc()  # Imprime traceback completo

    # Ou capturar como string
    erro_completo = traceback.format_exc()
    print(erro_completo)
```

### Logging com Traceback

```python
import logging
import traceback

logger = logging.getLogger(__name__)

try:
    codigo_perigoso()
except Exception as e:
    logger.error(
        f"Erro em {__name__}:\n{traceback.format_exc()}"
    )
```

## 9. Assert (Depuração)

Assert verifica condições durante desenvolvimento.

```python
def calcular_media(numeros):
    assert len(numeros) > 0, "Lista não pode ser vazia"
    assert all(isinstance(n, (int, float)) for n in numeros), \
        "Todos devem ser números"

    return sum(numeros) / len(numeros)

# Em produção, assertions podem ser desativadas com -O
# python -O script.py
```

**Não use assert para validação em produção!**

❌ **ERRADO:**
```python
def sacar(saldo, valor):
    assert valor > 0  # Pode ser desativado!
    return saldo - valor
```

✅ **CERTO:**
```python
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("Valor deve ser positivo")
    return saldo - valor
```

## 10. Exercícios Práticos

### Exercício 1: Calculadora Segura
Crie uma calculadora que trata divisão por zero e input inválido.

<details>
<summary>Ver solução</summary>

```python
def calculadora():
    try:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        operacao = input("Operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, digite números válidos!")
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")

calculadora()
```
</details>

### Exercício 2: Leitor de Arquivo Seguro
Leia um arquivo tratando todos os erros possíveis.

<details>
<summary>Ver solução</summary>

```python
def ler_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' não encontrado")
        return None
    except PermissionError:
        print(f"Sem permissão para ler '{caminho}'")
        return None
    except UnicodeDecodeError:
        print(f"Erro de codificação em '{caminho}'")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# Uso
conteudo = ler_arquivo("dados.txt")
```
</details>

### Exercício 3: Validador de Idade com Exceção Customizada
Crie exceção customizada para idade inválida.

<details>
<summary>Ver solução</summary>

```python
class IdadeInvalidaError(Exception):
    """Idade fora de faixa válida."""
    pass

def validar_idade(idade):
    if not isinstance(idade, int):
        raise IdadeInvalidaError("Idade deve ser inteiro")
    if idade < 0 or idade > 150:
        raise IdadeInvalidaError(f"Idade {idade} inválida")
    return idade

try:
    validar_idade(200)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
```
</details>

## 11. Resumo

| Conceito | Sintaxe | Quando Usar |
|----------|---------|-------------|
| try/except | `try: ... except Erro:` | Capturar erros |
| else | `else: ...` | Se não houve erro |
| finally | `finally: ...` | Sempre executa |
| raise | `raise Erro("msg")` | Levantar erro |
| assert | `assert condicao` | Debug (não produção) |
| logging | `logger.error()` | Registrar erros |

## Próximos Passos

1. ✅ Pratique try/except em todos os scripts
2. ✅ Crie exceções customizadas para Climy
3. ✅ Use logging em vez de print
4. ✅ Estude o **Guia 08** (Trabalhando com Arquivos)

---

**Próximo guia:** [08-trabalhando-arquivos.md](./08-trabalhando-arquivos.md) - Leitura e escrita de arquivos
