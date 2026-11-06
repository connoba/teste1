# Estado do projeto — TESTE 1

**Última atualização:** 2026-11-06  
**Repositório:** https://github.com/connoba/teste1  
**Branch:** main

## Resumo honesto
- [x] Acesso GitHub à conta connoba e permissões de escrita confirmados.
- [x] Documentação de âmbito, arquitetura, fontes, validação, segurança, testes e roadmap criada.
- [x] Aplicação local Streamlit criada.
- [x] Recolha de SEC Company Facts e Submissions para Apple implementada.
- [x] Payloads originais guardados em SQLite, com URL e data de recolha.
- [x] Extração inicial de observações anuais 10-K para nove métricas US-GAAP selecionadas.
- [x] Interface com tabela histórica, gráficos, indicadores derivados, histórico de filings SEC, dicionário de tags e exportação CSV criada.
- [x] Backup manual da base SQLite disponível na interface.
- [x] Instalador Windows com verificação Python 3.11+ e iniciador com browser automático configurado.
- [x] Treze testes unitários passaram num ambiente Python local isolado (cópia dos módulos e testes atuais); compilação Python também passou.
- [x] GitHub Actions configurado para executar testes em Windows.
- [ ] Workflow GitHub Actions confirmado como aprovado.
- [ ] Instalação e arranque verificados num PC Windows real.
- [ ] Séries reconciliadas com os 10-K originais da Apple.
- [ ] Restauro de backup testado.
- [ ] Relatórios financeiros exportáveis concluídos.
- [ ] Calendário futuro de resultados confirmado por fonte oficial implementado.

## Estado por fase
| Fase | Estado | Evidência |
|---|---|---|
| 0 — Auditoria e âmbito | Concluída | Requisitos e riscos documentados |
| 1 — Tecnologia | Em validação | Protótipo criado; execução Windows e CI pendentes |
| 2 — Fundação local | Em curso | SQLite, BATs e download de backup criados; instalação, arranque e restauro por testar |
| 3 — Dados oficiais | Protótipo | Company Facts e Submissions SEC preservados; séries anuais e filings extraídos; reconciliação pendente |
| 4 — Interface | Protótipo | Lista, gráficos, indicadores, calendário de filings, dicionário e CSV implementados |
| 5 — Análise | Protótipo | Crescimento da receita, margens, FCF aproximado, passivos/capital próprio e ROE aproximado implementados; validação financeira pendente |
| 6 — Relatórios | Protótipo | Relatório Markdown descarregável com séries, indicadores, filings e fontes; validação documental pendente |
| 7 — Calendário | Protótipo | Histórico SEC 10-K, 10-Q e 8-K; calendário futuro de earnings por implementar |
| 8 — Testes | Parcialmente testado | 13 testes locais passaram; CI e Windows real pendentes |
| 9 — Entrega | Por iniciar | Sem versão estável |

## Registo de verificações
| Data | Verificação | Resultado |
|---|---|---|
| 2026-11-06 | Acesso GitHub à conta connoba | Aprovado |
| 2026-11-06 | Permissões no repositório teste1 | Leitura e escrita confirmadas |
| 2026-11-06 | Testes unitários locais isolados | 13 aprovados; compilação Python também passou |
| 2026-11-06 | GitHub Actions | Workflow configurado; GitHub não devolveu status para o commit consultado |
| 2026-11-06 | Instalação Windows real | Pendente |
| 2026-11-06 | Reconciliação com 10-K Apple | Pendente |

## Próximas tarefas
1. Confirmar o resultado do workflow GitHub Actions e corrigir eventuais falhas.
2. Testar os dois BATs num Windows limpo.
3. Verificar tags e valores SEC contra os 10-K originais.
4. Implementar histórico de versões, amended filings e deteção de reformulações.
5. Completar restauro de backup e validar modo offline.
6. Criar relatório financeiro reproduzível com fontes e fórmulas.
7. Integrar datas futuras de resultados apenas com fonte oficial e identificação clara de confirmado versus estimado.

**Regra de controlo:** código criado não significa código testado; testes locais não significam CI aprovado; valores extraídos não significam validação contabilística.
