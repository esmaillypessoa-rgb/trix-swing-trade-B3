# 📊 Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do agente de swing trade deve considerar duas dimensões:

1. **Testes estruturados:** Validação dos sinais técnicos e coerência das análises;
2. **Avaliação prática:** Teste com usuários e comparação com resultados reais de mercado.

---

## 📈 Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade Técnica** | O sinal gerado foi correto? | Sinal de compra seguido de movimento de alta |
| **Segurança (Anti-Alucinação)** | O agente evitou inventar dados? | Pergunta fora do dataset retorna resposta neutra |
| **Coerência com Estratégia** | O agente respeita regras do TRIX? | Não gerar compra com TRIX negativo |
| **Consistência** | O agente mantém padrão de decisão? | Mesmo cenário gera decisões semelhantes |
| **Aderência ao Perfil** | Respeita gestão de risco do perfil? | Não sugerir operações fora do risco definido |

---

> [!TIP]
> Peça para 3-5 pessoas com conhecimento básico em mercado testarem o agente e avaliarem as respostas.  
> Para maior precisão, utilize também comparação com dados históricos (backtest).

---

## 🧪 Exemplos de Cenários de Teste

### Teste 1: Sinal de Compra

- **Entrada:** Dados com TRIX positivo e cruzando média
- **Resposta esperada:** Sinal de COMPRA
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 2: Sinal de Venda

- **Entrada:** TRIX negativo abaixo da média
- **Resposta esperada:** Sinal de VENDA
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo

- **Pergunta:** "Qual o preço do dólar amanhã?"
- **Resposta esperada:**  
  O agente informa que não realiza previsões futuras específicas
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 4: Dados insuficientes

- **Entrada:** Ativo sem histórico suficiente
- **Resposta esperada:**  
  "Dados insuficientes para análise confiável"
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 5: Validação de risco

- **Entrada:** Operação com risco acima do permitido
- **Resposta esperada:**  
  O agente rejeita ou alerta sobre o risco
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## 📉 Métricas Quantitativas (Backtest)

| Métrica | Descrição |
|--------|----------|
| **Win Rate** | Percentual de operações vencedoras |
| **Retorno Médio** | Média de retorno por trade |
| **Drawdown Máximo** | Maior perda acumulada |
| **Sharpe Ratio** | Retorno ajustado ao risco |
| **Expectativa Matemática** | Valor esperado por operação |

---

## 📊 Exemplo de Resultado
Total de Trades: 50
Win Rate: 62%
Retorno Médio: 2.8%
Drawdown Máximo: -8%
Expectativa: positiva


---

## 🧠 Avaliação Qualitativa

### O que funcionou bem:

- Sinais técnicos consistentes com o TRIX
- Baixa incidência de falsos positivos
- Respostas objetivas e sem alucinação
- Boa integração entre análise técnica e contexto

---

### O que pode melhorar:

- Integração com dados fundamentalistas reais
- Maior sensibilidade em mercados laterais
- Inclusão de stop loss dinâmico
- Ajuste fino do período do TRIX

---

## 🔬 Métricas Avançadas (Opcional)

Para evolução do projeto:

- 📊 **Precision / Recall** para sinais de compra/venda  
- 📈 **Curva de Equity**  
- ⚡ **Latência da IA**  
- 💰 **Custo por inferência (tokens)**  
- 🤖 **Acurácia de modelos de Machine Learning (futuro)**  

Ferramentas recomendadas:

- Pandas / NumPy (análise)
- Matplotlib (visualização)
- LangFuse / LangWatch (monitoramento de LLM)

---

## 📌 Considerações Finais

A avaliação deste agente vai além de respostas corretas.

Ela envolve:

- 📊 Performance real no mercado
- 🧠 Consistência da lógica quantitativa
- 🔐 Segurança contra alucinação

O objetivo é garantir que o agente seja confiável, consistente e útil como ferramenta de apoio à decisão em swing trade.
