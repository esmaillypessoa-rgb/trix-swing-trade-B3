# 📊 Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Histórico de decisões do agente (sinais e resultados) |
| `perfil_investidor.json` | JSON | Definição de perfil de risco e parâmetros de trading |
| `produtos_financeiros.json` | JSON | Contextualização dos instrumentos utilizados (ações, ETFs, derivativos) |
| `transacoes.csv` | CSV | Histórico de operações realizadas (backtest e performance) |

---

## Adaptações nos Dados

Os dados foram adaptados do modelo original do desafio para refletir um cenário real de **trading quantitativo**, incluindo:

- Substituição do contexto bancário por **operações de swing trade**
- Inclusão de:
  - Ativos da B3 (PETR4, VALE3, ITUB4, etc.)
  - Resultados de operações (win/loss)
  - Percentual de retorno
  - Tempo de holding
- Estruturação dos dados para permitir:
  - Backtesting
  - Avaliação de performance
  - Uso em modelos de machine learning (futuro)

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são carregados localmente a partir da pasta `data/` utilizando a biblioteca `pandas` (CSV) e `json`.

- CSV → carregados como DataFrame
- JSON → carregados como dicionários Python

Exemplo:

```python
import pandas as pd
import json

transacoes = pd.read_csv("data/transacoes.csv")

with open("data/perfil_investidor.json") as f:
    perfil = json.load(f)

### Exemplo de Contexto Montado
Perfil do Trader:
- Nome: Esmailly Pessoa
- Perfil: Moderado-agressivo
- Capital para trade: R$ 20.000
- Risco por operação: 2%

Ativos monitorados:
- PETR4
- VALE3
- ITUB4

Últimas operações:
- PETR4: +5.23% (5 dias)
- VALE3: +3.67% (4 dias)
- ITUB4: -2.75% (3 dias)

Contexto atual:
- Mercado com tendência de alta em commodities
- Fluxo estrangeiro positivo
