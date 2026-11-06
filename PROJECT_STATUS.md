# Estado do projeto — TESTE 1

**Última atualização:** 2026-11-06  
**Repositório:** https://github.com/connoba/teste1  
**Branch:** main

## Resumo honesto
- [x] Acesso GitHub à conta connoba e permissões de escrita confirmados.
- [x] Documentação inicial, arquitetura, fontes, validação, segurança, testes e roadmap criados.
- [x] Aplicação local Streamlit criada.
- [x] Recolha de SEC Company Facts para Apple implementada.
- [x] Payload original guardado em SQLite, com URL e data de recolha.
- [x] Extração inicial de observações anuais 10-K para nove métricas US-GAAP selecionadas.
- [x] Interface com tabela histórica, gráficos, dicionário de tags e exportação CSV.
- [x] Instalador Windows com verificação Python 3.11+ e iniciador com browser automático configurado.
- [x] Seis testes unitários executados com sucesso num ambiente Python local isolado (cópia dos módulos e testes atuais).
- [x] GitHub Actions configurado para executar testes em Windows.
- [ ] Workflow GitHub Actions confirmado como aprovado.
- [ ] Instalação e arranque verificados num PC Windows real.
- [ ] Séries reconciliadas com os 10-K originais da Apple.
- [ ] Backup e restauro testados.
- [ ] Relatórios, calendário e análise fundamentalista concluídos.

## Estado por fase
| Fase | Estado | Evidência |
|---|---|---|
| 0 — Auditoria e âmbito | Concluída | Requisitos e riscos documentados |
| 1 — Tecnologia | Em validação | Protótipo criado; execução Windows e CI pendentes |
| 2 — Fundação local | Em curso | SQLite e scripts .bat criados; instalação, arranque e recuperação por testar |
| 3 — Dados oficiais | Protótipo | SEC Company Facts preservado; séries anuais iniciais extraídas; reconciliação pendente |
| 4 — Interface | Protótipo | Lista, gráficos, dicionário de tags e CSV implementados |
| 5 — Análise | Por iniciar | Rácios e diagnósticos por implementar |
| 6 — Relatórios | Por iniciar | Por implementar |
| 7 — Calendário | Por iniciar | Por implementar |
| 8 — Testes | Parcialmente testado | 6 testes locais passaram; CI e Windows real pendentes |
| 9 — Entrega | Por iniciar | Sem versão estável |

## Registo de verificações
| Data | Verificação | Resultado |
|---|---|---|
| 2026-11-06 | Acesso GitHub à conta connoba | Aprovado |
| 2026-11-06 | Permissões no repositório teste1 | Leitura e escrita confirmadas |
| 2026-11-06 | Testes unitários locais isolados | 6 aprovados |
| 2026-11-06 | Workflow GitHub Actions | Configurado; resultado ainda não confirmado |
| 2026-11-06 | Instalação Windows real | Pendente |
| 2026-11-06 | Reconciliação com 10-K Apple | Pendente |

## Próximas tarefas
1. Confirmar o resultado do workflow GitHub Actions e corrigir eventuais falhas.
2. Testar os dois BATs num Windows limpo.
3. Verificar as tags e valores SEC contra os 10-K Apple.
4. Adicionar histórico de filings e deteção de reformulações.
5. Criar backups/restauro e validar modo offline.
6. Só depois implementar rácios, relatórios e calendário.

**Regra de controlo:** código criado não significa código testado; testes locais não significam CI aprovado; valores extraídos não significam validação contabilística.
