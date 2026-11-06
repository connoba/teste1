# Roadmap — TESTE 1

As fases são sequenciais. Uma fase só passa a **Concluída** quando os critérios de aceitação forem verificados e registados em `PROJECT_STATUS.md`.

| Fase | Objetivo | Critério de saída | Estado |
|---|---|---|---|
| 0 | Auditoria e âmbito | Repositório auditado; requisitos e riscos documentados | Em curso |
| 1 | Seleção tecnológica | Comparação e protótipo mínimo testado em Windows | Por iniciar |
| 2 | Fundação local | Arranque, configuração, SQLite, logs e backup testados | Por iniciar |
| 3 | Dados oficiais | Importação SEC/Apple, proveniência e validação automatizadas | Por iniciar |
| 4 | Interface | Navegação, modo Lista e modo Gráficos funcionais | Por iniciar |
| 5 | Análise fundamentalista | Métricas calculadas com fórmulas e períodos consistentes | Por iniciar |
| 6 | Relatórios | Relatórios reproduzíveis e exportáveis, com fontes | Por iniciar |
| 7 | Calendário | Eventos financeiros com origem e datas verificáveis | Por iniciar |
| 8 | Qualidade e recuperação | Testes funcionais, offline, atualização, backup e restauro aprovados | Por iniciar |
| 9 | Entrega TESTE 1 | Instalação limpa e utilização diária validadas | Por iniciar |

## Regras
1. Não construir funcionalidades antes de validar a arquitetura mínima.
2. Não introduzir Docker, PostgreSQL ou serviços permanentes sem justificação.
3. Preferir bibliotecas open-source maduras e reduzir dependências.
4. Não apagar nem substituir dados sem auditoria e backup.
5. Distinguir implementado, testado e validado.
6. Registar bloqueios e decisões no Git.

## Primeiro piloto — Apple Financial History
- Identificação da empresa e CIK.
- Recolha de submissions e company facts da SEC.
- Relatórios oficiais Apple Investor Relations.
- Histórico anual/trimestral com período fiscal, unidade, moeda e fonte.
- Deteção de ausências, duplicados, alterações e reformulações.
- Modos Lista e Gráficos.

Não assumir que todos os conceitos contabilísticos são comparáveis entre empresas ou jurisdições.
