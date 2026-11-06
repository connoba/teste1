# Segurança, privacidade e backups

## Local-first
- Base de dados e documentos numa pasta local fora do controlo de versões.
- Git contém apenas código, documentação e exemplos sem dados privados.
- Não enviar documentos locais para cloud.
- Não guardar tokens, palavras-passe ou chaves no repositório.

## Rede
- Serviço ligado a localhost/127.0.0.1 por defeito.
- Não abrir portas externas nem configurar acesso remoto por defeito.
- Ligações externas apenas para fontes públicas e atualizações solicitadas.

## Backups
- Cópias locais datadas da base de dados e documentos originais.
- Política de retenção configurável.
- Validar backups através de restauro real.
- Nunca sobrescrever a única cópia.
- Backup simples, preferencialmente integrado na aplicação.

## Instalação
- Ambiente Python isolado.
- `INSTALAR.bat` prepara dependências e valida pré-requisitos.
- `INICIAR.bat` inicia a aplicação e abre o browser.
- Scripts com erros compreensíveis e sem apagar dados.
