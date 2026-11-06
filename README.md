# TESTE 1 — Plataforma local de análise fundamentalista

Aplicação de pesquisa fundamentalista de ações globais, executada localmente no Windows e apresentada no browser.

## Princípios
- **Local-first:** dados, documentos, base de dados e configuração ficam no PC.
- **Sem cloud:** os ficheiros de dados do utilizador não são enviados para serviços externos.
- **Simplicidade:** uma instalação inicial (`INSTALAR.bat`) e um arranque normal (`INICIAR.bat`).
- **Fontes verificáveis:** privilegiar fontes oficiais; nunca inventar ou preencher lacunas silenciosamente.
- **Rastreabilidade:** cada recolha deve preservar fonte, URL e data de recolha.
- **Qualidade:** nenhuma fase é concluída sem testes registados.

## Protótipo atual
O primeiro protótipo apresenta uma interface Streamlit local, permite obter o ficheiro Company Facts da SEC para Apple Inc. e guarda o JSON original numa base SQLite local. Também permite pesquisar as tags US-GAAP disponíveis e descarregar um backup da base SQLite.

- Empresa-piloto: Apple Inc.
- CIK SEC: `0000320193`
- Fonte: [SEC Company Facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json)
- Dados locais: pasta `data/` (ignorada pelo Git).

**Limitação importante:** a normalização cobre apenas um conjunto limitado de tags US-GAAP e ainda precisa de reconciliação com os 10-K oficiais. Não usar os resultados do protótipo como análise de investimento.

## Como preparar
1. Instalar Python 3.11 ou superior.
2. Executar `INSTALAR.bat`.
3. Executar `INICIAR.bat`.
4. Na aplicação, introduzir um User-Agent com nome e email de contacto para a SEC.
5. Carregar em «Atualizar dados oficiais».

## Estado
Consultar [PROJECT_STATUS.md](PROJECT_STATUS.md) e [ROADMAP.md](ROADMAP.md). Doze testes unitários passaram num ambiente local isolado. O workflow GitHub Actions, a instalação num PC Windows e a reconciliação com os 10-K continuam pendentes.

## Segurança e privacidade
A aplicação liga-se apenas a `127.0.0.1`. Os dados e a base SQLite ficam no computador. Não versionar a pasta `data/` nem credenciais.
