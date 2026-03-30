<h1 align="center">🌤️ Climy — Dashboard Meteorológico Inteligente</h1>

<p align="center">
<b>Aplicação web de previsão do tempo, moderna, performática e didática.</b><br>
Desenvolvida com <strong>Python + Streamlit</strong> e integração com a API Open-Meteo.
</p>

---

## ✨ Funcionalidades

### 🔍 Busca Inteligente de Cidades
- Autocomplete dinâmico estilo Google
- Validação de cidades reais (evita estados, países ou entradas inválidas)
- Exibição de contexto geográfico (cidade, estado, país)

### 🌡️ Dashboard em Tempo Real
- Temperatura atual
- Sensação térmica
- Umidade relativa do ar
- Velocidade do vento
- Condição climática com ícones dinâmicos (WMO)

### 📅 Previsão Horária (24h)
- Gráfico interativo horizontal
- Evolução de temperatura ao longo do dia
- Indicadores visuais de mudança climática

### 🗓️ Previsão de 7 Dias
- Temperaturas mínimas e máximas
- Ícones representando o clima diário
- Ideal para planejamento semanal

### 🎨 Interface e Experiência (UX/UI)
- Customização via CSS externo
- Componentes HTML integrados ao Streamlit
- Layout responsivo e moderno

### ⚡ Performance e Cache
- Sistema de cache com TTL configurável
- Redução de chamadas à API
- Melhor tempo de resposta e escalabilidade

---
├── services/
│   └── weather_api.py      # Integração com APIs externas
│
├── src/
│   └── config.py           # Configurações globais (ex: CACHE_TTL)
│
## 🏗️ Arquitetura do Projeto

O projeto segue uma abordagem baseada em separação de responsabilidades, facilitando manutenção, testes e escalabilidade:

```text
climy/
│
├── streamlit_app.py        # Entry point (UI + estado da aplicação)
├── services/
│   └── weather_api.py      # Integração com APIs externas
├── src/
│   └── config.py           # Configurações globais (ex: CACHE_TTL)
├── assets/
│   └── style.css           # Customização visual
├── requirements.txt
└── README.md
```

### 🔹 Camadas

**Interface (`streamlit_app.py`)**
- Gerencia `st.session_state`, renderização de componentes e fluxo de interação do usuário

**Serviços (`services/`)**
- Requisições HTTP, tratamento de erros, normalização de dados

**Configuração (`src/`)**
- Constantes globais, parâmetros de cache, variáveis de ambiente

---
pip instalado
git clone https://github.com/seu-usuario/climy.git
## 🚀 Setup e Execução

### 1. Pré-requisitos
- Python 3.9+
- pip instalado

### 2. Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/climy.git

# Acesse o diretório
cd climy

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
```

### 3. Execução
```bash
streamlit run streamlit_app.py
```
Acesse no navegador: [http://localhost:8501](http://localhost:8501)

---
## ⚙️ Configuração e Customização

### ⏱️ Cache (Performance)
Definido em `src/config.py`:

```python
CACHE_TTL = 600  # segundos
```
- Controla o tempo de expiração dos dados
- Evita requisições desnecessárias
- Melhora performance geral

### 🌦️ Mapeamento WMO (Ícones Climáticos)
A aplicação utiliza códigos da Organização Meteorológica Mundial.

```python
WMO_EMOJIS: dict[int, str] = {
    0: "☀️",   # Céu limpo
    1: "🌤️",  # Parcialmente nublado
    2: "⛅",   # Nublado
    3: "☁️",   # Encoberto
}
```

---

## 🔐 Segurança e Boas Práticas

- Sanitização de inputs com `html.escape`
- Tratamento de exceções de API
- Logging estruturado (`logging.ERROR`)
- Separação clara de responsabilidades
- Código orientado a manutenção e escalabilidade

---

## 📈 Possíveis Evoluções

- 📍 Geolocalização automática do usuário
- 📊 Gráficos avançados com Plotly
- 🔔 Alertas meteorológicos em tempo real
- 🌎 Suporte multilíngue
- 📱 Versão mobile-first ou PWA
- ☁️ Deploy em cloud (AWS, GCP, Vercel)

---

## 📄 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## 👩‍💻 Autoria
Desenvolvido com ❤️ por Mariana Franco.
