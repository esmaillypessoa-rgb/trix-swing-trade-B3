🤖 Agente de Swing Trade com IA Generativa (B3)
📌 Visão Geral

Este projeto implementa um Agente Inteligente de Swing Trade para a B3, capaz de:

📊 Identificar sinais técnicos com TRIX(8)
🧾 Validar com análise fundamentalista
🌎 Incorporar contexto macroeconômico global
🧠 Utilizar IA Generativa para decisão assistida
📉 Avaliar performance via backtest
🎯 Objetivo

Gerar diariamente uma lista de ativos com potencial de operação (compra/venda) com base em:

Cruzamento do indicador TRIX
Confirmação por média móvel
Filtros quantitativos e qualitativos
⚙️ Estratégia Técnica
📈 Sinal de Compra
TRIX(8) > 0
TRIX cruza acima da média móvel (8)
📉 Sinal de Venda
TRIX(8) < 0
TRIX cruza abaixo da média móvel (8)
🧠 Modelo de Decisão

Score final:

Score = (Técnico * 0.4) + (Fundamentalista * 0.3) + (Macro * 0.3)
🔬 Melhorias Avançadas

✔ Filtro de liquidez
✔ Backtest com dados reais
✔ IA com controle de alucinação
✔ Integração com notícias confiáveis
✔ Arquitetura modular escalável

📁 Estrutura do Projeto
lab-agente-financeiro/
│
├── README.md
│
├── data/
│   ├── raw/                # Dados históricos (CSV reais)
│   ├── processed/          # Dados tratados
│   └── signals.csv         # Sinais gerados
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── src/
│   ├── app.py              # Execução principal
│   ├── data_fetch.py       # Coleta de dados
│   ├── indicators.py       # Indicadores técnicos
│   ├── signal_engine.py    # Geração de sinais
│   ├── backtest.py         # Backtest
│   ├── ranking.py          # Score final
│   ├── macro.py            # Análise macro
│   ├── fundamental.py      # Análise fundamentalista
│   └── ai_engine.py        # IA Generativa
│
├── assets/
│   └── diagramas.png
│
└── examples/
    └── README.md
🚀 Setup do Projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/lab-agente-financeiro.git
cd lab-agente-financeiro
2️⃣ Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3️⃣ Instalar dependências
pip install pandas yfinance
📡 Coleta de Dados (B3)

Baixe os últimos 2 anos de dados:

python src/data_fetch.py

✔ Os arquivos serão salvos em:

data/raw/
▶️ Execução do Agente
python src/app.py
📊 Saída Esperada
ticker   signal   score
PETR4    COMPRA   8.2
VALE3    COMPRA   7.9
📉 Backtest

Execute:

python src/backtest.py

Métricas:

Win Rate
Retorno médio
Retorno acumulado
🌎 Fontes de Dados
Mercado
Dados da B3
Yahoo Finance (fallback)
Notícias
BBC
CNN
Investing.com
🔐 Segurança
IA baseada apenas em dados fornecidos
Sem geração de informações fictícias
Restrições via prompt engineering
📊 Métricas Avaliadas
Assertividade dos sinais
Consistência do ranking
Drawdown
Retorno acumulado
🧠 IA Generativa

O agente utiliza IA para:

Interpretar cenário macroeconômico
Cruzar dados técnicos e fundamentalistas
Priorizar oportunidades
🛠️ Roadmap
 Integração com API da B3
 Dashboard com Streamlit
 Machine Learning para previsão
 Integração com MetaTrader
 Sistema de alertas (Telegram)
🎯 Diferencial

Este projeto vai além de um simples scanner técnico:

👉 Atua como um analista quantitativo automatizado com contexto macroeconômico

⚠️ Disclaimer

Este projeto é educacional e não constitui recomendação de investimento.
