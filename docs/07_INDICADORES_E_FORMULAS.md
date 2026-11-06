# Indicadores — definição e cautelas

Os indicadores abaixo são cálculos auxiliares do protótipo Apple. Não são uma classificação de qualidade nem uma recomendação de investimento.

| Indicador | Fórmula implementada | Cautela |
|---|---|---|
| Crescimento da receita | Receita do período / receita anterior - 1 | Só compara períodos anuais presentes na mesma série |
| Margem operacional | Resultado operacional / receita | Depende da classificação da tag e de itens não recorrentes |
| Margem líquida | Resultado líquido / receita | Pode ser afetada por impostos e itens extraordinários |
| Fluxo de caixa livre (aprox.) | Fluxo de caixa operacional - valor absoluto do CapEx | Definição simplificada; não substitui reconciliação da demonstração de fluxos |
| Passivos / capital próprio | Passivos / capital próprio | Pode ser pouco informativo quando capital próprio é negativo ou muito reduzido |
| ROE aproximado | Resultado líquido / média do capital próprio inicial e final | Usa o período anterior disponível; não calcula se faltar saldo comparável |

## Regras de integridade
- Não preencher observações em falta com zero.
- Não misturar unidades monetárias.
- Distinguir valores de duração (fluxos) de valores instantâneos (balanço).
- Não calcular rácios quando faltam inputs ou o denominador é zero.
- Preservar tag, período e submissão de origem na tabela base.
- Antes de usar numa decisão, reconciliar os dados com o relatório anual oficial e rever eventuais reapresentações.

## Limite atual
As métricas usam tags US-GAAP padronizadas. A aplicação ainda não trata integralmente extensões XBRL específicas da Apple nem mapeia automaticamente alterações de classificação ao longo do tempo.
