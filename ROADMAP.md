# Roadmap — TESTE 1

As fases são sequenciais. Uma fase só passa a **Concluída** quando os critérios de aceitação forem verificados e registados em `PROJECT_STATUS.md`.

| Fase | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| 0 | Auditoria e âmbito | Repositório auditado; requisitos e riscos documentados | Concluída |
| 1 | Seleção tecnológica | Protótipo mínimo, dependências e execução Windows validados | Em validação |
| 2 | Fundação local | Arranque, configuração, SQLite, logs e backup/restauro testados | Em curso |
| 3 | Dados oficiais | Importação SEC/Apple, proveniência, versões e validação contabilística | Protótipo |
| 4 | Interface | Navegação, modo Lista, modo Gráficos e exportação | Protótipo |
| 5 | Análise fundamentalista | Métricas, rácios, fórmulas e períodos consistentes | Por iniciar |
| 6 | Relatórios | Relatórios reproduzíveis e exportáveis, com fontes | Por iniciar |
| 7 | Calendário | Eventos financeiros com origem e datas verificáveis | Por iniciar |
| 8 | Qualidade e recuperação | Testes funcionais, offline, atualização, backup e restauro aprovados | Em preparação |
| 9 | Entrega TESTE 1 | Instalação limpa e utilização diária validadas | Por iniciar |

## Trabalho implementado no protótipo
- Interface local em Streamlit.
- Recolha do SEC Company Facts para Apple Inc. (CIK 0000320193).
- Preservação do payload original em SQLite, com URL e data de recolha.
- Extração inicial de observações 10-K anuais para um conjunto limitado de tags US-GAAP.
- Separação entre factos de duração (fluxos) e factos instantâneos (balanço).
- Filtros de unidade e duração anual; exclusão de formulários trimestrais.
- Tabela histórica, gráfico de série temporal e exportação CSV.
- Scripts Windows para instalação e arranque.
- Testes unitários para persistência, filtragem anual e unidades.

## Próximos passos técnicos
1. Confirmar o workflow no GitHub Actions.
2. Testar instalação e arranque num Windows limpo.
3. Comparar cada série anual com os 10-K originais da Apple; documentar divergências.
4. Adicionar submissions SEC, accession number e deteção de alterações/reapresentações.
5. Completar backups/restauro e modo offline.
6. Implementar rácios e diagnósticos apenas depois da validação das séries base.

## Regras
1. Não construir métricas derivadas antes de validar as séries de origem.
2. Não introduzir Docker, PostgreSQL ou serviços permanentes sem justificação.
3. Preferir bibliotecas open-source maduras e reduzir dependências.
4. Não apagar nem substituir dados sem auditoria e backup.
5. Distinguir implementado, testado localmente, testado no CI e validado contra documentos oficiais.
6. Registar bloqueios e decisões no Git.
7. Não assumir comparabilidade entre conceitos contabilísticos de empresas, setores ou jurisdições diferentes.
