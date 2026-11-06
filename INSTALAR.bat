@echo off
setlocal
cd /d "%~dp0"
echo.
echo ==========================================
echo   TESTE 1 - Instalacao
echo ==========================================
echo.

where py >nul 2>nul
if errorlevel 1 (
  echo ERRO: Python 3.11 ou superior nao foi encontrado.
  echo Instale Python 3.11+ e ative "Add Python to PATH".
  pause
  exit /b 1
)

py -3 -c "import sys; raise SystemExit(0 if sys.version_info >= (3,11) else 1)"
if errorlevel 1 (
  echo ERRO: E necessario Python 3.11 ou superior.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo A criar ambiente Python local...
  py -3 -m venv .venv
  if errorlevel 1 goto erro
)

echo A instalar dependencias...
".venv\Scripts\python.exe" -m pip install --upgrade pip
if errorlevel 1 goto erro
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto erro

if not exist "data" mkdir data

echo.
echo Instalacao concluida.
echo Para abrir a aplicacao, execute INICIAR.bat.
pause
exit /b 0

:erro
echo.
echo ERRO durante a instalacao. Consulte a mensagem acima.
pause
exit /b 1
