# Arquitetura e seleção tecnológica

## Decisão provisória
O protótipo usa Python + Streamlit + Plotly + SQLite. É a combinação mais simples para uma aplicação no browser local, com um instalador e um iniciador, sem Docker, PostgreSQL ou serviços cloud.

A decisão só será definitiva depois de validar num Windows limpo e obter CI aprovado.

## Componentes
| Componente | Tecnologia | Responsabilidade |
|---|---|---|
| Linguagem | Python 3.11+ | Ingestão, regras e interface |
| Interface | Streamlit | Aplicação no browser local |
| Gráficos | Plotly | Séries históricas |
| Dados estruturados | SQLite | Histórico e metadados |
| HTTP | Requests | Acesso a fontes oficiais |
| Tabelas | Pandas | Apresentação e exportação |
| Testes | pytest | Testes automatizados |

## Arquitetura
1. O utilizador executa `INICIAR.bat`.
2. Streamlit escuta apenas em `127.0.0.1:8501`.
3. A interface chama módulos Python separados para recolha e normalização.
4. A ingestão obtém dados oficiais apenas quando solicitada.
5. O payload original é preservado em SQLite local.
6. A normalização extrai observações com período, unidade, formulário e data de submissão.
7. A interface apresenta tabelas, gráficos e CSV.

## Dados locais e privacidade
- A pasta `data/` é ignorada pelo Git.
- A base SQLite e os documentos ficam no computador.
- A SEC só é contactada quando o utilizador pede atualização.
- A aplicação não deve expor o serviço à rede local.
- Não guardar credenciais no repositório.

## Limitações conhecidas
- O protótipo cobre apenas Apple e um conjunto limitado de tags US-GAAP.
- As séries ainda não foram reconciliadas sistematicamente com os 10-K originais.
- Extensões XBRL específicas da empresa ainda não estão tratadas.
- A seleção da submissão mais recente por período não substitui uma gestão completa do histórico de reformulações.
- A extração anual não é, por si só, uma política contabilística validada.

## Critérios de aprovação
- Instalação num Windows limpo.
- Arranque e abertura do browser sem comandos manuais.
- Persistência após fechar e reabrir.
- Atualização sem perda dos dados anteriores.
- Backup e restauro demonstrados.
- Testes automáticos aprovados.
