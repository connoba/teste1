# TESTE 1 — Plataforma local de análise fundamentalista

Aplicação de pesquisa fundamentalista de ações globais, executada localmente no Windows e apresentada no browser.

## Princípios
- **Local-first:** dados, documentos, base de dados e configuração ficam no PC.
- **Sem cloud:** não enviar ficheiros do utilizador para serviços externos.
- **Simplicidade:** uma instalação inicial (`INSTALAR.bat`) e um arranque normal (`INICIAR.bat`).
- **Fontes verificáveis:** privilegiar fontes oficiais; nunca inventar ou preencher lacunas silenciosamente.
- **Rastreabilidade:** cada valor deve conservar fonte, URL, data de recolha, período fiscal, unidade e moeda.
- **Qualidade:** nenhuma fase é concluída sem testes registados.

## Caso-piloto
Apple Inc. — CIK SEC `0000320193`. O piloto valida recolha, normalização, histórico, proveniência e apresentação antes de alargar a cobertura.

## Execução pretendida
- Windows 10/11 e browser local.
- SQLite e documentos guardados localmente.
- `INSTALAR.bat` uma única vez; `INICIAR.bat` para utilização diária.
- Sem Docker, PostgreSQL ou serviços cloud.

## Estado
Consultar [PROJECT_STATUS.md](PROJECT_STATUS.md) e [ROADMAP.md](ROADMAP.md).

> Estado inicial: documentação e planeamento. A aplicação ainda não está implementada nem testada.
