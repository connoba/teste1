# Estado do projeto — TESTE 1

**Última atualização:** 2026-11-06  
**Repositório:** https://github.com/connoba/teste1  
**Branch:** main

## Resumo honesto
- [x] Acesso GitHub à conta connoba e permissões de escrita confirmados.
- [x] Documentação inicial, arquitetura candidata, fontes, validação, segurança, plano de testes e roadmap criados.
- [x] Protótipo inicial da aplicação Streamlit criado.
- [x] Integração inicial com SEC Company Facts para Apple implementada.
- [x] Persistência do payload original em SQLite local implementada.
- [x] Scripts Windows de instalação e arranque criados.
- [x] Testes unitários iniciais criados.
- [x] GitHub Actions configurado para executar os testes em Windows.
- [ ] Testes automáticos executados e aprovados.
- [ ] Instalação e arranque verificados num PC Windows real.
- [ ] Dados SEC reconciliados com documentos oficiais e métricas normalizadas.

## Estado por fase
| Fase | Estado | Evidência |
|---|---|---|
| 0 — Auditoria e âmbito | Concluída | Repositório e requisitos iniciais auditados; documentação criada |
| 1 — Tecnologia | Em validação | Protótipo Python/Streamlit/SQLite criado; aguarda execução de CI e teste Windows |
| 2 — Fundação local | Em curso | SQLite e scripts .bat criados; instalação, arranque, backup e restauro por testar |
| 3 — Dados oficiais | Protótipo | Recolha Company Facts SEC e preservação do JSON implementadas; validação contabilística por fazer |
| 4 — Interface | Protótipo | Página local de exploração de tags US-GAAP criada; modos Lista/Gráficos finais por fazer |
| 5 — Análise | Por iniciar | Métricas financeiras ainda não calculadas |
| 6 — Relatórios | Por iniciar | Por implementar |
| 7 — Calendário | Por iniciar | Por implementar |
| 8 — Testes | Preparado, execução pendente | Testes pytest e workflow Windows criados; sem resultado de execução confirmado |
| 9 — Entrega | Por iniciar | Sem versão estável |

## Verificações registadas
| Data | Verificação | Resultado |
|---|---|---|
| 2026-11-06 | Acesso GitHub à conta connoba | Aprovado |
| 2026-11-06 | Permissões no repositório teste1 | Leitura e escrita confirmadas |
| 2026-11-06 | Documentação e ficheiros de aplicação | Criados no branch main |
| 2026-11-06 | Testes automáticos | Ainda não executados/confirmados |

## Próximos passos
1. Obter o resultado do workflow GitHub Actions em Windows.
2. Corrigir todos os erros reportados pelo CI.
3. Executar instalação e arranque no Windows.
4. Validar o payload SEC e construir a primeira tabela financeira com períodos e unidades corretos.
5. Só depois avançar para gráficos e métricas.

**Regra de controlo:** código criado não significa código testado; testes preparados não significam testes aprovados. Não promover fases sem evidência.
