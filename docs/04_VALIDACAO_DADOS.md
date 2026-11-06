# Validação e qualidade dos dados

## Princípios
1. Nenhum valor é inventado ou estimado para preencher lacunas.
2. Preservar o payload original da fonte.
3. Separar recolha, normalização, cálculo e apresentação.
4. Cada observação deve manter tag, período, unidade, formulário e data de submissão.
5. Valores em falta não são equivalentes a zero.
6. Não misturar moedas, unidades ou períodos.

## Validação já implementada
- Apenas formulários 10-K para a primeira série anual.
- Separação entre factos de duração (fluxos) e factos instantâneos (balanço).
- Unidade monetária USD exigida para as métricas atualmente suportadas.
- Duração entre 330 e 380 dias para observações anuais de fluxo.
- Seleção da submissão mais recente para o mesmo ano fiscal e período.
- Crescimento anual e ROE aproximado não calculados quando existe uma lacuna temporal superior ao intervalo anual esperado.

## Validação ainda necessária
- Reconciliar cada métrica e período com o 10-K correspondente.
- Verificar extensões XBRL específicas da Apple e alterações de tags ao longo do tempo.
- Identificar reapresentações, amended filings e mudanças de classificação.
- Rever períodos fiscais de 52/53 semanas e mudanças no calendário fiscal.
- Verificar sinais e convenções de CapEx e fluxo de caixa.
- Confirmar se o valor corresponde ao consolidado e não a segmentos.
- Guardar resultado e evidência de cada reconciliação.

## Critério de aprovação de uma série
Uma série só pode ser considerada validada depois de:
- tag e unidade documentadas;
- períodos confirmados;
- amostra histórica reconciliada com documentos oficiais;
- divergências explicadas;
- testes de regressão aprovados.
