# 🔀 Guia 12: Git e GitHub - Controle de Versão

Aprenda a versionar seu código, trabalhar com branches e contribuir em projetos.

## 1. O Que é Git?

**Git** é um sistema de controle de versão distribuído.

### Por Que Usar?

✅ **Histórico** - Veja todas as mudanças do projeto
✅ **Backup** - Código na nuvem (GitHub)
✅ **Colaboração** - Múltiplas pessoas no mesmo projeto
✅ **Experimentos** - Branches para testar sem quebrar
✅ **Revert** - Desfaça mudanças se algo der errado

## 2. Instalação

### Windows

1. **Baixe:** https://git-scm.com/download/win
2. **Instale:** Próximo, Próximo... (configurações padrão)
3. **Verifique:**
   ```powershell
   git --version
   # git version 2.44.0
   ```

### macOS

```bash
# Com Homebrew
brew install git

# Ou instale Xcode Command Line Tools
xcode-select --install
```

### Linux

```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git
```

## 3. Configuração Inicial

### Configure Seu Nome e Email

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Verifique Configurações

```bash
git config --list
```

### Editor Padrão

```bash
# VS Code
git config --global core.editor "code --wait"

# Ou Vim (padrão)
git config --global core.editor vim
```

## 4. Conceitos Fundamentais

### Repositório (Repo)

Pasta do projeto com histórico Git.

### Working Directory

Sua pasta atual com arquivos.

### Staging Area

Área onde você prepara commits.

### Commit

Snapshot das mudanças no repositório.

### Branch

Linha de desenvolvimento independente.

### Remote

Repositório na nuvem (GitHub, GitLab).

## 5. Comandos Básicos

### Inicializar Repositório

```bash
# Na pasta do projeto
cd climy
git init

# Cria pasta .git (oculta)
# Agora é um repositório Git
```

### Verificar Status

```bash
git status

# Saída:
# On branch main
# Untracked files:
#   streamlit_app.py
# Changes not staged for commit:
#   modified:   src/config.py
```

### Adicionar Arquivos

```bash
# Adiciona um arquivo
git add streamlit_app.py

# Adiciona todos os arquivos
git add .

# Adiciona todos .py
git add *.py

# Remove arquivo do staging
git reset HEAD arquivo.py
```

### Commitar Mudanças

```bash
git commit -m "feat: adiciona busca de cidades"

# Mensagens comuns:
# feat: nova funcionalidade
# fix: correção de bug
# docs: atualização de documentação
# style: formatação, PEP 8
# refactor: refatoração de código
# test: adiciona testes
# chore: configuração, dependências
```

### Ver Histórico

```bash
# Lista commits
git log

# Resumido
git log --oneline

# Com gráfico
git log --oneline --graph --all

# Últimos 5
git log -5
```

## 6. Branches

### Criar Branch

```bash
# Cria nova branch
git branch feature/nova-funcionalidade

# Ou cria e já muda
git checkout -b feature/nova-funcionalidade

# Moderno (Git 2.23+)
git switch -c feature/nova-funcionalidade
```

### Listar Branches

```bash
# Branches locais
git branch

# Branches remotas
git branch -r

# Todas
git branch -a

# Branch atual
git branch --show-current
```

### Mudar de Branch

```bash
# Muda para branch
git checkout main

# Moderno
git switch main
```

### Mesclar Branch (Merge)

```bash
# Volte para main
git checkout main

# Merge da branch feature
git merge feature/nova-funcionalidade

# Resolve conflitos se houver
# Commit automático se sem conflitos
```

### Deletar Branch

```bash
# Deleta branch local
git branch -d feature/nova-funcionalidade

# Força deletar (mesmo não merged)
git branch -D feature/nova-funcionalidade

# Deleta branch remota
git push origin --delete feature/nova-funcionalidade
```

## 7. GitHub

### Clonar Repositório

```bash
# Do GitHub
git clone https://github.com/usuario/climy.git

# Clona para pasta climy/
cd climy
```

### Adicionar Remote

```bash
# Ver remotes
git remote -v

# Adicionar remote
git remote add origin https://github.com/usuario/climy.git

# Renomear
git remote rename origin upstream
```

### Push (Enviar)

```bash
# Envia branch para GitHub
git push -u origin main

# Depois, só
git push

# Força push (cuidado!)
git push --force
```

### Pull (Baixar)

```bash
# Baixa mudanças do GitHub
git pull origin main

# Ou fetch + merge
git fetch origin
git merge origin/main
```

### Fork e Contribuir

1. **Fork no GitHub:**
   - Botão "Fork" no repo
   - Cria cópia na sua conta

2. **Clone seu fork:**
   ```bash
   git clone https://github.com/SEU_USUARIO/climy.git
   ```

3. **Crie branch:**
   ```bash
   git checkout -b feature/minha-contribuicao
   ```

4. **Faça mudanças e commit:**
   ```bash
   git add .
   git commit -m "feat: adiciona nova feature"
   git push origin feature/minha-contribuicao
   ```

5. **Pull Request:**
   - No GitHub, vá para seu fork
   - Clique "Compare & pull request"
   - Descreva mudanças
   - Aguarde review

## 8. Resolvendo Conflitos

### Quando Acontece

- Duas pessoas mudam mesma linha
- Merge não consegue decidir automaticamente

### Como Resolver

1. **Git avisa:**
   ```
   CONFLICT (content): Merge conflict in streamlit_app.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```

2. **Abra arquivo:**
   ```python
   <<<<<<< HEAD
   st.title("Climy v2")
   =======
   st.title("Climy Atualizado")
   >>>>>>> feature/nova-funcionalidade
   ```

3. **Edite manualmente:**
   ```python
   # Escolha uma versão ou combine
   st.title("Climy v2 Atualizado")
   ```

4. **Marque como resolvido:**
   ```bash
   git add streamlit_app.py
   git commit -m "Resolve merge conflict"
   ```

## 9. .gitignore

Arquivo que diz o que Git deve ignorar.

### Crie .gitignore

```bash
# .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testes
.pytest_cache/
.coverage
htmlcov/
*.cover

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

### Regras

```bash
# Ignora pasta
__pycache__/

# Ignora extensão
*.log

# Ignora arquivo específico
secret.key

# Mas não ignore este
!important.log

# Ignora recursivo
**/temp/
```

## 10. Comandos Úteis

### Desfazer Mudanças

```bash
# Desfaz mudanças em arquivo (antes do add)
git checkout -- arquivo.py

# Ou moderno
git restore arquivo.py

# Remove do staging (antes do commit)
git reset HEAD arquivo.py

# Ou moderno
git restore --staged arquivo.py
```

### Stash (Guardar Mudanças)

```bash
# Guarda mudanças temporariamente
git stash

# Lista stashes
git stash list

# Aplica último stash
git stash apply

# Aplica e remove da lista
git stash pop

# Remove stash
git stash drop
```

### Tag (Versões)

```bash
# Cria tag
git tag v1.0.0

# Tag com mensagem
git tag -a v1.0.0 -m "Versão 1.0.0"

# Envia tags
git push origin --tags

# Lista tags
git tag
```

### Blame (Quem Mudou)

```bash
# Mostra quem modificou cada linha
git blame streamlit_app.py

# Com histórico
git blame -L 10,20 streamlit_app.py
```

### Diff (Diferenças)

```bash
# Mudanças não commitadas
git diff

# Entre branches
git diff main..feature

# Entre commits
git diff abc123..def456
```

## 11. Fluxo de Trabalho (Workflow)

### Git Flow (Simplificado)

```
main (produção)
  ↑
  merge
  ↑
develop (desenvolvimento)
  ↑
  merge
  ↑
feature/nova-feature (sua branch)
```

### Passos

1. **Atualize develop:**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Crie feature:**
   ```bash
   git checkout -b feature/minha-feature
   ```

3. **Desenvolva:**
   ```bash
   git add .
   git commit -m "feat: adiciona X"
   ```

4. **Atualize develop:**
   ```bash
   git checkout develop
   git pull origin develop
   ```

5. **Merge:**
   ```bash
   git checkout develop
   git merge feature/minha-feature
   git push origin develop
   ```

6. **Deploy para main:**
   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```

## 12. Boas Práticas

### Commits

✅ **CERTO:**
```bash
git commit -m "feat: adiciona busca de cidades"
git commit -m "fix: corrige erro de validação"
git commit -m "docs: atualiza README"
```

❌ **ERRADO:**
```bash
git commit -m "mudanças"
git commit -m "arrumando coisas"
git commit -m "teste"
git commit -m "aaaaaaa"
```

### Branches

✅ **CERTO:**
```bash
feature/busca-cidades
fix/erro-validacao
docs/atualiza-readme
hotfix/corrige-bug-critico
```

❌ **ERRADO:**
```bash
nova-branch
teste
branch1
minha-branch-muito-longa-que-nao-tem-sentido
```

### Mensagens de Commit

Use padrão Conventional Commits:

```
<tipo>(<escopo>): <descrição>

[corpo opcional]

[rodapé opcional]
```

**Tipos:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Configuração

**Exemplo:**
```
feat(weather): adiciona cache de 5 minutos

- Implementa cache com TTL configurável
- Reduz chamadas à API em 80%
- Adiciona testes de cache

Closes #123
```

## 13. GitHub Actions (CI/CD)

### Crie Workflow

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: pytest -v --cov
```

### O Que Acontece

1. Push para GitHub
2. GitHub Actions roda automaticamente
3. Instala dependências
4. Roda testes
5. Mostra resultado

## 14. Comandos para o Dia a Dia

```bash
# Começar dia
git checkout main
git pull origin main

# Trabalhar
git checkout -b feature/nova
# ... codar ...
git add .
git commit -m "feat: adiciona X"

# Antes de push
git fetch origin
git rebase origin/main

# Enviar
git push -u origin feature/nova

# Fim do dia
git checkout main
git pull origin main
```

## 15. Troubleshooting

### "Please tell me who you are"

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### "Already up to date"

Significa que já está sincronizado.

### "Changes not staged for commit"

```bash
# Ver diferenças
git diff

# Adiciona e commita
git add .
git commit -m "mensagem"
```

### Commit errado

```bash
# Desfaz último commit (mantém mudanças)
git reset --soft HEAD~1

# Desfaz tudo
git reset --hard HEAD~1
```

### Push errado

```bash
# Se foi último commit
git reset --hard HEAD~1
git push --force
```

## 16. Resumo

| Comando | O Que Faz |
|---------|-----------|
| `git init` | Inicia repo |
| `git clone` | Baixa repo |
| `git status` | Mostra estado |
| `git add` | Adiciona ao staging |
| `git commit` | Commita mudanças |
| `git push` | Envia para remote |
| `git pull` | Baixa do remote |
| `git branch` | Gerencia branches |
| `git merge` | Mescla branches |
| `git log` | Histórico |

## Próximos Passos

1. ✅ Crie conta no GitHub
2. ✅ Clone o Climy
3. ✅ Crie uma branch e faça mudanças
4. ✅ Estude o **Guia 13** (Ollama no VS Code)

---

**Próximo guia:** [13-ollama-vscode.md](./13-ollama-vscode.md) - IA local no VS Code
