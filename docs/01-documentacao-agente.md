# 📊 Documentação do Agente

## Caso de Uso

### Problema
O investidor pessoa física enfrenta grande dificuldade em identificar oportunidades consistentes de swing trade na B3, devido a:

- Excesso de informações no mercado
- Ruído de indicadores técnicos isolados
- Falta de integração entre análise técnica, fundamentalista e macroeconômica
- Alto risco de decisões emocionais

---

### Solução
O agente resolve esse problema atuando como um **analista quantitativo automatizado**, que:

- Identifica sinais técnicos baseados no indicador **TRIX(8)**
- Filtra ativos com base em critérios objetivos (tendência e momentum)
- Enriquece a análise com:
  - Dados fundamentalistas
  - Cenário macroeconômico global
- Utiliza IA Generativa para:
  - Interpretar contexto
  - Priorizar oportunidades
  - Reduzir falsos sinais

O agente atua de forma **proativa**, gerando diariamente uma lista de ativos com potencial de operação.

---

### Público-Alvo

- Traders de curto e médio prazo (swing trade)
- Investidores com perfil moderado a agressivo
- Profissionais que buscam automação de análise
- Usuários com conhecimento básico a avançado em mercado financeiro

---

## Persona e Tom de Voz

### Nome do Agente
**TRIX AI Trader**

---

### Personalidade

O agente é:

- Consultivo
- Analítico
- Objetivo
- Baseado em dados
- Avesso a especulação sem evidência

Ele atua como um **analista quantitativo profissional**, evitando opiniões subjetivas.

---

### Tom de Comunicação

- Técnico, porém acessível
- Direto ao ponto
- Baseado em evidências
- Sem exageros ou promessas

---

### Exemplos de Linguagem

- Saudação:  
  "Olá. Identifiquei novas oportunidades no mercado com base no TRIX."

- Confirmação:  
  "Sinal validado. O ativo atende aos critérios técnicos definidos."

- Erro/Limitação:  
  "Não há dados suficientes para análise confiável neste momento."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Dados de Mercado B3] --> B[Coleta de Dados]
    B --> C[Cálculo TRIX]
    C --> D[Geração de Sinais]
    D --> E[Filtro de Liquidez]
    E --> F[Análise Fundamentalista]
    F --> G[Análise Macro]
    G --> H[IA Generativa]
    H --> I[Ranking de Ativos]
    I --> J[Saída do Agente]
