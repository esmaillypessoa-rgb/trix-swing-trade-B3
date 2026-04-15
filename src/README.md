# 💻 Código da Aplicação

Esta pasta contém o código do **Agente de Swing Trade com IA (TRIX AI Trader)**.

O agente é responsável por:

- 📊 Coletar dados de mercado (B3)
- 🧮 Calcular indicadores técnicos (TRIX)
- 🚦 Gerar sinais de compra e venda
- 🧠 Integrar análise com IA
- 📉 Executar backtest da estratégia
- 📊 Gerar ranking de ativos

---

## 📁 Estrutura da Aplicação

src/
├── app.py # Execução principal do agente
├── data_fetch.py # Coleta de dados históricos (Yahoo/B3)
├── indicators.py # Cálculo do TRIX
├── signal_engine.py # Geração de sinais (compra/venda)
├── backtest.py # Backtest da estratégia
├── ranking.py # Cálculo do score final
├── macro.py # Análise macroeconômica (placeholder)
├── fundamental.py # Análise fundamentalista (placeholder)
├── ai_engine.py # Integração com IA (LLM)
└── requirements.txt # Dependências

---

## ⚙️ Principais Componentes

### 📊 `data_fetch.py`
Responsável por baixar dados históricos dos ativos da B3.

---

### 🧮 `indicators.py`
Implementa o cálculo do indicador TRIX (Triple Exponential Average).

---

### 🚦 `signal_engine.py`
Define regras de entrada e saída:

- TRIX > média → COMPRA  
- TRIX < média → VENDA  

---

### 📉 `backtest.py`
Executa simulações históricas da estratégia:

- Avalia performance
- Calcula métricas
- Valida consistência

---

### 🧠 `ai_engine.py`
Responsável por:

- Interpretar dados
- Gerar análises textuais
- Priorizar ativos

---

### 📊 `ranking.py`
Calcula o score final dos ativos:
Score = (Técnico * 0.4) + (Fundamental * 0.3) + (Macro * 0.3)

---

## 📦 Exemplo de requirements.txt

pandas
yfinance
numpy

---

## 🚀 Como Rodar

### 1. Instalar dependências

```bash
pip install -r requirements.txt

2. Baixar dados históricos
python data_fetch.py
3. Executar o agente
python app.py
📊 Saída Esperada
ticker   signal   score
PETR4    COMPRA   8.2
VALE3    COMPRA   7.9
BBDC4    VENDA    6.8
🧪 Execução de Backtest
python backtest.py
🔐 Boas Práticas
Dados devem ser atualizados regularmente
Evitar uso de dados incompletos
Validar sinais antes de execução real
Utilizar gerenciamento de risco
🚀 Evolução Futura
Interface com Streamlit
Integração com API da B3
Machine Learning para previsão
Execução automatizada de ordens
📌 Observação

Este código é voltado para fins educacionais e não deve ser utilizado diretamente para operações financeiras sem validação adicional.
