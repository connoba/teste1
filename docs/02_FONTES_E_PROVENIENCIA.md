# Fontes de dados e proveniência

## Política
Usar dados oficiais sempre que disponíveis. Agregadores podem ajudar na descoberta, mas não substituem a fonte primária sem indicação explícita.

## Apple — piloto
- SEC EDGAR submissions: https://data.sec.gov/submissions/CIK0000320193.json
- SEC company facts: https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json
- SEC filing history: https://www.sec.gov/edgar/browse/?CIK=320193
- Apple Investor Relations: https://investor.apple.com/

CIK do piloto: `0000320193`.

## Metadados obrigatórios por observação
Empresa e identificador; tag original e métrica normalizada; valor bruto e normalizado; unidade e moeda; período fiscal e tipo de período; data de publicação/submissão; URL e ID do documento; data/hora da recolha; indicação de correção ou reformulação quando detetável.

## Cuidados
- Tags XBRL semelhantes não são necessariamente equivalentes.
- Não misturar trimestres, exercícios e valores acumulados.
- Uma métrica pode ter unidades ou contextos diferentes.
- Submissões posteriores podem reformular períodos anteriores.
- Não interpolar valores em falta sem os identificar como estimativas.
- Respeitar termos e limites da SEC; implementar User-Agent identificável e tratamento de HTTP 429/5xx.

## Expansão global
A cobertura internacional será faseada por jurisdição. Não assumir que a SEC cobre empresas fora dos EUA. Cada jurisdição exige auditoria própria de fontes, formatos, licenças, idioma e calendário fiscal.
