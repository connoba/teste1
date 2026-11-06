@echo off
setlocal
cd /d "%~dp0"
echo.
echo ==========================================
echo   TESTE 1 - Instalacao
echo ==========================================
echo.

set "PY_EXE="
set "PY_ARGS="

where py >nul 2>nul
if not errorlevel 1 (
  set "PY_EXE=py"
  set "PY_ARGS=-3"
  goto verificar_python
)

where python >nul 2>nul
if not errorlevel 1 (
  set "PY_EXE=python"
  goto verificar_python
)

echo Python nao encontrado. A tentar instalar Python 3.11 automaticamente...
where winget >nul 2>nul
if errorlevel 1 (
  echo.
  echo ERRO: Este computador nao tem Python nem Windows Package Manager (winget).
  echo Instale Python 3.11 ou superior em https://www.python.org/downloads/windows/
  echo Depois volte a executar INSTALAR.bat.
  pause
  exit /b 1
)

winget install --id Python.Python.3.11 --exact --scope user --accept-source-agreements --accept-package-agreements
if errorlevel 1 (
  echo.
  echo A instalacao automatica nao foi concluida.
  echo Instale Python 3.11 ou superior em https://www.python.org/downloads/windows/
  pause
  exit /b 1
)

set "PY_HOME=%LocalAppData%\Programs\Python\Python311"
if exist "%PY_HOME%\python.exe" (
  set "PY_EXE=%PY_HOME%\python.exe"
  goto verificar_python
)

set "PY_LAUNCHER=%LocalAppData%\Programs\Python\Launcher\py.exe"
if exist "%PY_LAUNCHER%" (
  set "PY_EXE=%PY_LAUNCHER%"
  set "PY_ARGS=-3.11"
  goto verificar_python
)

echo.
echo Python foi instalado, mas o executavel nao foi localizado automaticamente.
echo Feche esta janela e execute INSTALAR.bat novamente.
pause
exit /b 1

:verificar_python
"%PY_EXE%" %PY_ARGS% -c "import sys; raise SystemExit(0 if sys.version_info >= (3,11) else 1)"
if errorlevel 1 (
  echo ERRO: E necessario Python 3.11 ou superior.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo A criar ambiente Python local...
  "%PY_EXE%" %PY_ARGS% -m venv .venv
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
