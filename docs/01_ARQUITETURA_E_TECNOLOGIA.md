# Arquitetura e seleção tecnológica

## Objetivo
Aplicação web local, simples de instalar e manter, sem infraestrutura cloud e sem exigir ao utilizador gerir vários serviços.

## Candidatos iniciais (a validar)
| Componente | Candidato | Motivo | Risco a testar |
|---|---|---|---|
| Linguagem | Python | Ecossistema de dados e bibliotecas maduras | Versões e dependências no Windows |
| Interface | Streamlit | Interface browser com pouca infraestrutura | Navegação, estado e desempenho |
| Gráficos | Plotly | Gráficos interativos | Legibilidade e tamanho |
| Base de dados | SQLite | Ficheiro local, sem servidor separado | Escritas, migrações e cópias |
| Testes | pytest | Testes automatizados | Integração com instalação |

A combinação é uma **hipótese**, não decisão final. Aprovação apenas após protótipo mínimo no Windows.

## Arquitetura pretendida
1. Interface browser local.
2. Camada de aplicação e regras financeiras.
3. Camada de ingestão de dados oficiais.
4. Validação e normalização independentes da interface.
5. SQLite para dados estruturados.
6. Ficheiros originais e documentos numa pasta local.
7. Logs e backups locais.

## Restrições
- Browser liga apenas ao serviço local.
- Não expor o serviço à rede por defeito.
- Não exigir Docker, PostgreSQL ou conta cloud.
- Explicar falhas de Internet e indisponibilidade das fontes.
- Atualizações externas apenas quando solicitadas ou configuradas explicitamente.
- Encerramento sem perda de dados.

## Decisão pendente
Testar instalação e arranque em Windows limpo, abertura automática do browser, encerramento, persistência SQLite, atualização e recuperação. Só depois fixar a stack.
