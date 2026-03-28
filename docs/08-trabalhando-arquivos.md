# 🐍 Guia 08: Trabalhando com Arquivos e Dados

Aprenda a ler, escrever e manipular arquivos em Python.

## 1. Abrindo e Fechando Arquivos

### Método Tradicional

```python
# Abrir arquivo
arquivo = open("dados.txt", "r", encoding="utf-8")

# Ler conteúdo
conteudo = arquivo.read()
print(conteudo)

# Fechar arquivo (IMPORTANTE!)
arquivo.close()
```

### Método Recomendado (Context Manager)

```python
# with fecha o arquivo automaticamente
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Arquivo já foi fechado aqui
```

## 2. Modos de Abertura

| Modo | Descrição | Cria arquivo? |
|------|-----------|---------------|
| `'r'` | Leitura (default) | ❌ Erro se não existir |
| `'w'` | Escrita | ✅ Sim (sobrescreve!) |
| `'a'` | Append (adiciona) | ✅ Sim (se não existir) |
| `'x'` | Criação | ❌ Erro se existir |
| `'b'` | Binário | - |
| `'t'` | Texto (default) | - |
| `'+'` | Leitura e escrita | - |

### Exemplos

```python
# Leitura
with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Escrita (sobrescreve!)
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Conteúdo novo")

# Append (adiciona ao final)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\nNova linha de log")

# Leitura e escrita
with open("dados.txt", "r+", encoding="utf-8") as f:
    conteudo = f.read()
    f.write("\nMais conteúdo")

# Binário (imagens, etc)
with open("foto.jpg", "rb") as f:
    dados = f.read()
```

## 3. Lendo Arquivos

### read() - Lê Tudo

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()  # Lê arquivo inteiro
    print(conteudo)
```

### readline() - Lê Linha por Linha

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    linha1 = f.readline()  # Lê primeira linha
    linha2 = f.readline()  # Lê segunda linha

    # Ou iterar
    for linha in f:
        print(linha.strip())  # strip() remove \n
```

### readlines() - Lê Todas em Lista

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()  # Lista de strings

    for i, linha in enumerate(linhas):
        print(f"Linha {i}: {linha.strip()}")
```

### read() com Tamanho

```python
with open("dados.txt", "r", encoding="utf-8") as f:
    # Lê 100 caracteres
    parte = f.read(100)
    print(parte)

    # Lê mais 100
    outra_parte = f.read(100)
    print(outra_parte)
```

## 4. Escrevendo Arquivos

### write() - Escreve Texto

```python
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")
```

### writelines() - Escreve Lista

```python
linhas = [
    "Primeira linha\n",
    "Segunda linha\n",
    "Terceira linha\n"
]

with open("saida.txt", "w", encoding="utf-8") as f:
    f.writelines(linhas)
```

## 5. Trabalhando com Paths (pathlib)

### Importando pathlib

```python
from pathlib import Path

# Criar path
caminho = Path("dados/arquivo.txt")

# Path absoluto
absoluto = Path(__file__).resolve().parent

# Juntar paths
pasta = Path("dados")
arquivo = pasta / "subpasta" / "arquivo.txt"
print(arquivo)  # dados/subpasta/arquivo.txt
```

### Métodos Úteis de Path

```python
from pathlib import Path

caminho = Path("dados/arquivo.txt")

# Informações
caminho.exists()        # True/False
caminho.is_file()       # É arquivo?
caminho.is_dir()        # É diretório?
caminho.name            # 'arquivo.txt'
caminho.stem            # 'arquivo' (sem extensão)
caminho.suffix          # '.txt' (extensão)
caminho.parent          # Path('dados')

# Ler e escrever
caminho.read_text(encoding="utf-8")
caminho.write_text("conteúdo", encoding="utf-8")

# Listar diretório
pasta = Path("dados")
for arquivo in pasta.iterdir():
    print(arquivo.name)

# Criar diretórios
Path("nova/pasta").mkdir(parents=True, exist_ok=True)
```

## 6. Trabalhando com JSON

### Lendo JSON

```python
import json

# De arquivo
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)  # dict Python

# De string
json_string = '{"nome": "Maria", "idade": 25}'
dados = json.loads(json_string)

print(dados["nome"])  # "Maria"
```

### Escrevendo JSON

```python
import json

dados = {
    "nome": "Maria",
    "idade": 25,
    "cidades": ["São Paulo", "Rio"]
}

# Para arquivo
with open("saida.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

# Para string
json_string = json.dumps(dados, indent=2, ensure_ascii=False)
```

### Exemplo: Salvando Configurações

```python
import json
from pathlib import Path

CONFIG_FILE = Path("config.json")

def salvar_config(config):
    """Salva configurações em JSON."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def carregar_config():
    """Carrega configurações do JSON."""
    if not CONFIG_FILE.exists():
        return {}  # Retorna vazio se não existir

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Uso
config = {
    "cidade_padrao": "São Paulo",
    "temperatura_unit": "celsius",
    "cache_ttl": 300
}

salvar_config(config)
config_carregado = carregar_config()
```

## 7. Trabalhando com CSV

### Lendo CSV

```python
import csv

with open("dados.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)

    for linha in leitor:
        print(linha)  # Lista de valores
        # ['Nome', 'Idade', 'Cidade']
        # ['Maria', '25', 'São Paulo']
```

### Lendo CSV com DictReader

```python
import csv

with open("dados.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)

    for linha in leitor:
        print(linha)
        # {'Nome': 'Maria', 'Idade': '25', 'Cidade': 'São Paulo'}
        print(linha["Nome"])  # "Maria"
```

### Escrevendo CSV

```python
import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Maria", 25, "São Paulo"],
    ["João", 30, "Rio de Janeiro"]
]

with open("saida.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(dados)
```

### Escrevendo CSV com DictWriter

```python
import csv

dados = [
    {"Nome": "Maria", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "João", "Idade": 30, "Cidade": "Rio"}
]

with open("saida.csv", "w", encoding="utf-8", newline="") as f:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(f, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(dados)
```

## 8. Exemplos Práticos (Climy)

### Exemplo 1: Cache em Arquivo

```python
import json
from pathlib import Path
from datetime import datetime

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

def salvar_cache(cidade: str, dados: dict):
    """Salva dados de clima em cache."""
    arquivo = CACHE_DIR / f"{cidade.replace(' ', '_')}.json"

    cache_completo = {
        "timestamp": datetime.now().isoformat(),
        "dados": dados
    }

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(cache_completo, f, indent=2, ensure_ascii=False)

def carregar_cache(cidade: str, ttl_segundos: int = 300):
    """Carrega cache se não expirou."""
    arquivo = CACHE_DIR / f"{cidade.replace(' ', '_')}.json"

    if not arquivo.exists():
        return None

    with open(arquivo, "r", encoding="utf-8") as f:
        cache = json.load(f)

    # Verifica se expirou
    timestamp = datetime.fromisoformat(cache["timestamp"])
    decorrido = (datetime.now() - timestamp).total_seconds()

    if decorrido > ttl_segundos:
        arquivo.unlink()  # Remove arquivo expirado
        return None

    return cache["dados"]

# Uso
dados_clima = {"temperatura": 28.5, "umidade": 65}
salvar_cache("São Paulo", dados_clima)

cache = carregar_cache("São Paulo")
if cache:
    print(f"Do cache: {cache}")
```

### Exemplo 2: Exportar Previsão para CSV

```python
import csv
from pathlib import Path

def exportar_previsao_csv(previsao_horaria, cidade: str):
    """Exporta previsão horária para CSV."""

    arquivo = Path("exports") / f"previsao_{cidade.replace(' ', '_')}.csv"
    arquivo.parent.mkdir(exist_ok=True)

    with open(arquivo, "w", encoding="utf-8", newline="") as f:
        campos = ["hora", "temperatura", "umidade", "vento", "condicao"]
        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(previsao_horaria)

    print(f"Exportado para {arquivo}")

# Uso
previsao = [
    {"hora": "00:00", "temperatura": 22.5, "umidade": 65, "vento": 12.3, "condicao": "Limpo"},
    {"hora": "01:00", "temperatura": 21.8, "umidade": 68, "vento": 10.5, "condicao": "Nublado"},
    # ... mais horas
]

exportar_previsao_csv(previsao, "São Paulo")
```

### Exemplo 3: Log de Requisições

```python
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("logs") / "requisicoes.log"
LOG_FILE.parent.mkdir(exist_ok=True)

def log_requisicao(cidade: str, sucesso: bool, tempo_ms: float):
    """Registra requisição em arquivo de log."""

    timestamp = datetime.now().isoformat()
    status = "SUCESSO" if sucesso else "ERRO"

    linha = f"{timestamp} - {cidade} - {status} - {tempo_ms:.2f}ms\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha)

# Uso
log_requisicao("São Paulo", True, 234.5)
log_requisicao("Rio de Janeiro", False, 5000.0)
```

### Exemplo 4: Carregar Cidades de Arquivo

```python
import json
from pathlib import Path

def carregar_cidades_cadastradas():
    """Carrega lista de cidades válidas de JSON."""
    arquivo = Path("data") / "cidades.json"

    if not arquivo.exists():
        return []

    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_cidade_cadastrada(nome: str, estado: str, pais: str,
                              lat: float, lon: float):
    """Adiciona cidade ao cadastro."""
    arquivo = Path("data") / "cidades.json"

    # Carrega existentes
    cidades = carregar_cidades_cadastradas()

    # Adiciona nova
    nova_cidade = {
        "nome": nome,
        "estado": estado,
        "pais": pais,
        "latitude": lat,
        "longitude": lon
    }
    cidades.append(nova_cidade)

    # Salva tudo
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(cidades, f, indent=2, ensure_ascii=False)

# Uso
cidades = carregar_cidades_cadastradas()
print(f"{len(cidades)} cidades cadastradas")

salvar_cidade_cadastrada(
    "São Paulo", "SP", "Brasil",
    -23.5505, -46.6333
)
```

## 9. Arquivos Temporários

```python
import tempfile

# Criar arquivo temporário
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
    f.write("Dados temporários")
    temp_path = f.name

print(f"Arquivo temp: {temp_path}")

# Usar depois
with open(temp_path, "r") as f:
    print(f.read())

# Limpar
Path(temp_path).unlink()
```

## 10. Verificando e Manipulando Arquivos

```python
from pathlib import Path

arquivo = Path("dados.txt")

# Verificar existência
if arquivo.exists():
    print("Arquivo existe")

# Tamanho
tamanho = arquivo.stat().st_size
print(f"Tamanho: {tamanho} bytes")

# Renomear
arquivo.rename("novo_nome.txt")

# Mover
arquivo.rename("pasta/novo_nome.txt")

# Copiar
import shutil
shutil.copy("origem.txt", "destino.txt")

# Remover
arquivo.unlink()  # ou Path("arquivo.txt").unlink()

# Remover diretório inteiro
shutil.rmtree("pasta")
```

## 11. Exercícios Práticos

### Exercício 1: Leitor de Configurações
Leia um arquivo de configurações em JSON.

<details>
<summary>Ver solução</summary>

```python
import json
from pathlib import Path

def ler_config(arquivo="config.json"):
    caminho = Path(arquivo)

    if not caminho.exists():
        return {"erro": "Arquivo não existe"}

    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

config = ler_config()
print(config)
```
</details>

### Exercício 2: Contador de Linhas
Conte quantas linhas tem um arquivo.

<details>
<summary>Ver solução</summary>

```python
from pathlib import Path

def contar_linhas(arquivo):
    caminho = Path(arquivo)

    if not caminho.exists():
        return 0

    with open(caminho, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

total = contar_linhas("dados.txt")
print(f"Total: {total} linhas")
```
</details>

### Exercício 3: Backup Simples
Crie backup de um arquivo.

<details>
<summary>Ver solução</summary>

```python
import shutil
from pathlib import Path
from datetime import datetime

def criar_backup(origem):
    caminho_origem = Path(origem)

    if not caminho_origem.exists():
        print("Arquivo não existe")
        return

    # Gera nome com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = caminho_origem.parent / f"{caminho_origem.stem}_backup_{timestamp}{caminho_origem.suffix}"

    shutil.copy2(origem, destino)
    print(f"Backup criado: {destino}")

criar_backup("dados importantes.txt")
```
</details>

## 12. Resumo

| Operação | Código |
|----------|--------|
| Abrir arquivo | `with open("arq.txt", "r") as f:` |
| Ler tudo | `f.read()` |
| Ler linhas | `for linha in f:` |
| Escrever | `f.write("texto")` |
| JSON load | `json.load(f)` |
| JSON dump | `json.dump(dados, f)` |
| Path exists | `Path("arq").exists()` |
| Path join | `Path("pasta") / "arq.txt"` |

## Próximos Passos

1. ✅ Pratique leitura/escrita de arquivos
2. ✅ Use JSON para configurações do Climy
3. ✅ Implemente cache em arquivo
4. ✅ Estude o **Guia 09** (Entendendo o Climy)

---

**Próximo guia:** [09-entendendo-climy.md](./09-entendendo-climy.md) - Arquitetura do projeto
