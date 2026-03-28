# ✍️ Guia 14: Prompt Engineering - Guia Completo

Aprenda a escrever prompts eficazes para obter melhores respostas de IAs como Ollama, ChatGPT, etc.

## 1. O Que é Prompt Engineering?

**Prompt engineering** é a arte de escrever instruções claras e eficazes para modelos de IA, obtendo respostas mais precisas e úteis.

### Por Que Importa?

Um bom prompt pode fazer a diferença entre:

❌ **Prompt ruim:**
```
"Faça uma função"
```
→ Resposta genérica, pode não servir

✅ **Prompt bom:**
```
"Crie uma função Python que valida CPF,
retornando True se válido, False se inválido.
Inclua docstring, type hints e testes pytest."
```
→ Resposta completa e útil

## 2. Estrutura de um Prompt Eficaz

### Fórmula C.R.I.S.P.E.

**C**ontexto - Situação/background
**R**ole - Papel que IA deve assumir
**I**nstruções - O que fazer exatamente
**S**tyle - Estilo/tom/formato
**P**arametros - Limitações/requisitos
**E**xemplos - Exemplos do que você quer

### Exemplo Aplicado

```
# Contexto
Estou aprendendo Python e criando um app de previsão do tempo.

# Role
Você é um professor de Python didático e paciente.

# Instruções
Crie uma função que calcula sensação térmica.

# Style
- Use português claro
- Explique cada passo
- Inclua comentários no código

# Parametros
- Função deve ter type hints
- Máximo 30 linhas
- Sem bibliotecas externas

# Exemplos
Exemplo de uso:
>>> calcula_sensacao(30, 70)  # temp=30, umidade=70
35.5  # sensação térmica
```

## 3. Técnicas de Prompting

### 1. Few-Shot Prompting (Dar Exemplos)

```
Converta estas funções para usar type hints:

Exemplo 1:
Entrada: def soma(a, b): return a + b
Saída: def soma(a: int, b: int) -> int: return a + b

Exemplo 2:
Entrada: def saudacao(nome): return f"Olá, {nome}"
Saída: def saudacao(nome: str) -> str: return f"Olá, {nome}"

Agora converta:
def calcular_media(numeros):
    return sum(numeros) / len(numeros)
```

### 2. Chain of Thought (Pensamento Passo a Passo)

```
Resolva este problema passo a passo:

Problema: Calcular média de temperaturas

1. Primeiro, some todas as temperaturas
2. Conte quantas temperaturas temos
3. Divida soma pela quantidade
4. Retorne o resultado

Código:
```

### 3. Role Prompting (Atribuir Papel)

```
Você é um desenvolvedor Python sênior especializado em:
- Clean Code
- PEP 8
- Testes unitários
- Performance

Revise este código e sugira melhorias:

[código]
```

### 4. Template Prompting

```
Use este template para responder:

## Resumo
[1-2 frases sobre o que faz]

## Código
```python
[código aqui]
```

## Explicação
[Como funciona]

## Exemplo de Uso
```python
[exemplo aqui]
```

## Testes
```python
[testes aqui]
```

Agora crie uma função que [sua solicitação]
```

## 4. Prompts para Programação

### 1. Gerar Código

```
Crie uma função Python [NOME_FUNCAO] que:

**Objetivo:**
[O que a função deve fazer]

**Parâmetros:**
- param1 (tipo): descrição
- param2 (tipo): descrição

**Retorno:**
(tipo): descrição do retorno

**Requisitos:**
- [ ] Type hints
- [ ] Docstring completa
- [ ] Tratamento de erros
- [ ] Seguir PEP 8

**Exemplo de uso:**
```python
[exemplo aqui]
```
```

### 2. Explicar Código

```
Explique este código para um iniciante em Python:

```python
[código]
```

Inclua:
1. Visão geral do que o código faz
2. Explicação linha por linha das partes importantes
3. Conceitos Python utilizados
4. Exemplo prático de uso
5. Possíveis melhorias

Use analogias do mundo real para facilitar entendimento.
```

### 3. Debuggar Erros

```
Estou recebendo este erro:

**Erro:**
```
[mensagem de erro completa]
```

**Código:**
```python
[código]
```

**O que eu esperava:**
[comportamento esperado]

**O que aconteceu:**
[comportamento atual]

**Já tentei:**
- [o que você já tentou]

Por favor:
1. Explique a causa do erro
2. Mostre como corrigir
3. Previna erros similares no futuro
```

### 4. Refatorar Código

```
Refatore este código seguindo estas diretrizes:

**Código atual:**
```python
[código]
```

**Diretrizes:**
- [ ] Seguir PEP 8
- [ ] Melhorar nomes de variáveis
- [ ] Reduzir complexidade
- [ ] Adicionar type hints
- [ ] Melhorar legibilidade
- [ ] Manter mesma funcionalidade

**Prioridades:**
1. Legibilidade
2. Performance
3. Manutenibilidade

Explique cada mudança feita.
```

### 5. Gerar Testes

```
Crie testes pytest completos para:

**Função:**
```python
[código da função]
```

**Cubra:**
- [ ] Casos normais (happy path)
- [ ] Casos de erro
- [ ] Edge cases (valores limites)
- [ ] Valores nulos/vazios
- [ ] Tipos inválidos

**Formato:**
- Use pytest fixtures se apropriado
- Nomeie testes claramente (test_[func]_[caso])
- Inclua asserts descritivos
- Adicione docstrings

**Exemplo de estrutura:**
```python
def test_[funcao]_[caso_normal]():
    # Arrange
    # Act
    # Assert
```
```

### 6. Documentar Código

```
Adicione documentação completa:

**Código:**
```python
[código]
```

**Inclua:**
- Module docstring no topo
- Class docstring para cada classe
- Method docstring para cada método
- Type hints em todos os parâmetros e retornos
- Exemplos em docstrings (doctest format)

**Siga:**
- Google style docstrings
- PEP 257
- PEP 484 (type hints)
```

## 5. Prompts Específicos para Climy

### 1. Entender Módulo

```
Estou estudando o projeto Climy (app de previsão do tempo).

**Arquivo:** services/weather_api.py

**Objetivo:**
Explique este módulo para um desenvolvedor júnior que vai:
- Manter o código
- Adicionar features
- Corrigir bugs

Inclua:
1. Responsabilidade do módulo
2. Principais funções e o que fazem
3. Dependências externas (APIs)
4. Estrutura de dados de entrada/saída
5. Possíveis pontos de falha
6. Como testar

**Código:**
```python
[código completo ou trecho]
```
```

### 2. Adicionar Feature

```
Quero adicionar uma feature ao Climy:

**Feature:**
Previsão de chuva em formato visual (ícones)

**Contexto:**
- Climy já tem previsão horária
- API Open-Meteo fornece precipitation probability
- Streamlit já está configurado

**Requisitos:**
- Adicionar campo `precipitation_probability` no modelo
- Criar função que converte % em ícones
- Exibir no dashboard horário
- Manter performance (usar cache)

**Onde modificar:**
1. src/models/weather.py - adicionar campo
2. services/weather_api.py - buscar dado da API
3. streamlit_app.py - exibir na UI

Crie o código para cada arquivo.
```

### 3. Otimizar Performance

```
Analise a performance deste código:

**Código:**
```python
[código]
```

**Problema:**
- Lento quando processa muitas cidades
- Muitas chamadas à API
- Memory leaks possíveis

**Objetivo:**
- Reduzir tempo de execução em 50%
- Diminuir chamadas à API
- Otimizar uso de memória

**Sugira:**
1. Identifique bottlenecks
2. Sugira otimizações específicas
3. Mostre código otimizado
4. Explique ganho de performance de cada mudança
```

## 6. Anti-Patterns (O Que Não Fazer)

### ❌ Prompt Muito Vago

```
"Faça algo com Python"
```

✅ **Melhor:**
```
"Crie um script Python que lê temperaturas de um arquivo CSV
e gera um gráfico de linha com matplotlib"
```

### ❌ Múltiplas Tarefas de Uma Vez

```
"Crie uma função, escreva testes, documente, otimize,
explique, refatore e adicione logging"
```

✅ **Melhor:**
```
"Primeiro, crie a função [especificação]
Depois, escreva testes para ela
Então, adicione documentação"
```

### ❌ Sem Contexto

```
"Não funciona, conserte"
```

✅ **Melhor:**
```
"Esta função deveria retornar média de temperaturas,
mas está retornando 0.
Código: [código]
Erro: [mensagem]
Input de teste: [dados]"
```

### ❌ Esperar Leitura de Mente

```
"Faz igual aquele outro mas melhor"
```

✅ **Melhor:**
```
"Refatore esta função para:
- Ser 2x mais rápida
- Usar menos memória
- Manter mesma interface
Código: [código]"
```

### ❌ Prompts Gigantes

```
[2000 caracteres de contexto confuso]
```

✅ **Melhor:**
```
"Contexto principal: [2-3 frases]
Objetivo: [1 frase]
Requisitos: [lista com bullets]
Código: [trecho relevante]"
```

## 7. Templates Prontos

### Template 1: Criar Função

```markdown
# Tarefa: Criar função Python

## Objetivo
[O que a função deve fazer]

## Assinatura
def [nome]([parametros]) -> [retorno]:
    pass

## Requisitos
- [ ] Type hints completos
- [ ] Docstring no padrão Google
- [ ] Tratamento de erros
- [ ] [outros requisitos]

## Exemplos
```python
# Input
[exemplo de input]

# Output esperado
[exemplo de output]
```

## Restrições
- Não usar bibliotecas externas
- Máximo [X] linhas
- [outras restrições]
```

### Template 2: Explicar Conceito

```markdown
# Tarefa: Explicar conceito Python

## Conceito
[nome do conceito]

## Público-alvo
[nível: iniciante/intermediário/avançado]

## Incluir
- [ ] Definição simples
- [ ] Analogia do mundo real
- [ ] Exemplo de código
- [ ] Quando usar
- [ ] Quando não usar
- [ ] Erros comuns

## Formato
- Use português claro
- Evite jargões desnecessários
- Máximo 500 palavras
```

### Template 3: Code Review

```markdown
# Tarefa: Code Review

## Código
```python
[código]
```

## Foco da Review
- [ ] Bugs potenciais
- [ ] Performance
- [ ] Legibilidade
- [ ] PEP 8
- [ ] Testabilidade
- [ ] Segurança

## Formato da Resposta
1. Resumo geral
2. Pontos positivos
3. Problemas encontrados (prioridade: alta/média/baixa)
4. Sugestões de melhoria com código
5. Conclusão
```

## 8. Dicas Avançadas

### 1. Iteração

Não espere perfeição na primeira tentativa:

```
# Prompt 1
"Crie uma função de validação de email"

# Prompt 2 (refinando)
"Adicione verificação de domínio válido"

# Prompt 3 (refinando)
"Agora adicione suporte a emails internacionais"
```

### 2. Especificar Formato de Saída

```
"Responda em formato JSON:
{
  \"explicacao\": \"...\",
  \"codigo\": \"...\",
  \"exemplos\": [...]
}"
```

### 3. Pedir para IA Perguntar

```
"Antes de responder, me faça perguntas
se precisar de mais informações para
dar a melhor resposta possível."
```

### 4. Usar Delimitadores Claros

```
Analise este código:

```python
[código aqui]
```

Especifique:
1. [item 1]
2. [item 2]
3. [item 3]
```

### 5. Referenciar Conhecimento Prévio

```
"Considerando que já temos:
- Classe Weather com temperatura e umidade
- Função get_weather() que chama API
- Cache com TTL de 5 minutos

Crie uma função que..."
```

## 9. Exercícios Práticos

### Exercício 1: Melhore este Prompt

❌ **Original:**
```
"Faça uma calculadora"
```

<details>
<summary>Ver solução sugerida</summary>

```
"Crie uma calculadora em Python com:
- 4 operações básicas (+, -, *, /)
- Interface de linha de comando
- Menu interativo
- Tratamento de divisão por zero
- Loop até usuário digitar 'sair'

Inclua:
- Funções separadas para cada operação
- Docstrings
- Type hints
- Exemplo de uso no final
```
</details>

### Exercício 2: Crie Prompt para Testes

Crie um prompt para gerar testes pytest da função:

```python
def validar_cpf(cpf: str) -> bool:
    """Valida CPF brasileiro."""
    pass
```

<details>
<summary>Ver solução sugerida</summary>

```
"Crie testes pytest completos para validar_cpf():

Requisitos:
- Testar CPFs válidos (use exemplos reais)
- Testar CPFs inválidos (dígitos errados)
- Testar CPF com formato (123.456.789-00)
- Testar CPF apenas números (12345678900)
- Testar input vazio
- Testar CPF com letras
- Testar CPF com menos de 11 dígitos
- Testar CPF com mais de 11 dígitos
- Testar CPFs conhecidos inválidos (111.111.111-11, etc.)

Use pytest fixtures para dados de teste.
Nomeie testes claramente: test_validar_cpf_[caso]
```
</details>

## 10. Checklist de Prompt Perfeito

Antes de enviar, verifique:

- [ ] **Objetivo claro:** IA sabe o que fazer?
- [ ] **Contexto suficiente:** Tem informação necessária?
- [ ] **Requisitos explícitos:** Formato, estilo, limitações?
- [ ] **Exemplos:** Mostrou o que espera?
- [ ] **Específico:** Evitou vagueza?
- [ ] **Tamanho razoável:** Nem muito curto, nem muito longo?
- [ ] **Formato:** Usou markdown, code blocks?

## 11. Resumo

| Técnica | Quando Usar | Exemplo |
|---------|-------------|---------|
| Few-Shot | Padrões específicos | "Faça como nestes exemplos..." |
| Chain of Thought | Problemas complexos | "Pense passo a passo..." |
| Role | Especialidade | "Você é um especialista em..." |
| Template | Tarefas repetitivas | "Use este formato..." |
| Iteração | Refinar resultados | "Agora melhore X..." |

## Próximos Passos

1. ✅ Pratique com os templates
2. ✅ Use no Ollama (Guia 13)
3. ✅ Crie sua biblioteca de prompts
4. ✅ Avance para o **Guia 15** (Boas Práticas)

---

**Próximo guia:** [15-boas-praticas.md](./15-boas-praticas.md) - PEP 8 e Clean Code
