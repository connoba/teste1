# Plano de testes

## Antes de cada versão
- Instalação em Windows sem Python previamente preparado.
- Reexecução segura do instalador.
- Arranque e abertura automática do browser.
- Serviço acessível apenas em localhost.
- Encerramento sem corrupção.
- Persistência após reinício.
- Base de dados vazia e com histórico.
- Falhas de Internet, timeout, HTTP 429 e HTTP 5xx.
- Dados malformados, duplicados, ausentes e reformulados.
- Backup e restauro completos.
- Verificação de que dados locais não são enviados para Git.

## Testes financeiros
- Fórmulas verificadas com exemplos manuais.
- Comparação com documentos oficiais.
- Separação de períodos trimestrais e anuais.
- Tratamento de unidades, moedas e escalas.
- Valores negativos, zero e indisponíveis.
- Testes de regressão das fontes.

## Evidência
Cada teste regista identificador, data, ambiente, passos, resultado esperado, resultado observado e estado (Aprovado/Falhou/Bloqueado). Nenhum teste é aprovado sem execução.
