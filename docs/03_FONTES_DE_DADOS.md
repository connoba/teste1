# Fontes de dados — TESTE 1

## Fontes primárias do piloto Apple

| Fonte | Conteúdo | Utilização | URL |
|---|---|---|---|
| SEC Company Facts | Factos XBRL normalizados por conceito, unidade e período | Séries financeiras anuais e tags | https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json |
| SEC Submissions | Histórico de formulários e submissões | Calendário de filings, accession e datas | https://data.sec.gov/submissions/CIK0000320193.json |
| SEC EDGAR Archives | Documentos originais submetidos | Conferência de 10-K, 10-Q e 8-K | https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude |
| Apple Investor Relations | Relatórios anuais e documentos publicados pela empresa | Fonte oficial complementar para reconciliação | https://investor.apple.com/ |

## Regras de utilização
- A SEC é a fonte estruturada primária do protótipo.
- Os relatórios anuais da Apple são a fonte documental de controlo.
- Guardar URL, data de recolha, CIK, formulário, período, accession e tag sempre que disponíveis.
- Não substituir silenciosamente valores SEC por valores de fornecedores comerciais.
- Se duas fontes divergirem, manter ambos os valores com a respetiva proveniência e abrir uma exceção de validação.
- Respeitar as políticas de acesso e limites de utilização publicados pela SEC.
- Utilizar um User-Agent identificável com contacto válido.

## Âmbito atual
A aplicação recolhe Company Facts e Submissions da Apple. Ainda não descarrega nem arquiva automaticamente os PDFs/HTML completos dos relatórios anuais da Apple. A reconciliação documental continua pendente.
