@echo off
setlocal
cd /d "%~dp0"
echo.
echo ==========================================
echo   TESTE 1 - Instalacao
echo ==========================================
echo.

rem Preferir Python 3.11+ atraves do launcher do Windows.
where py >nul 2>nul
if not errorlevel 1 (
  py -3 -c "import sys; raise SystemExit(0 if sys.version_info >= (3,11) else 1)" >nul 2>nul
  if not errorlevel 1 (
    set "PY_EXE=py"
    set "PY_ARGS=-3"
    goto preparar
  )
)

rem Tentar Python no PATH se o launcher nao encontrar versao adequada.
where python >nul 2>nul
if not errorlevel 1 (
  python -c "import sys; raise SystemExit(0 if sys.version_info >= (3,11) else 1)" >nul 2>nul
  if not errorlevel 1 (
    set "PY_EXE=python"
    set "PY_ARGS="
    goto preparar
  )
)

echo Python 3.11+ nao encontrado. A tentar instalar Python 3.11 via winget...
where winget >nul 2>nul
if errorlevel 1 (
  echo.
  echo ERRO: Nao foi encontrado Python 3.11+ nem Windows Package Manager (winget).
  echo Instale Python 3.11 ou superior em https://www.python.org/downloads/windows/
  echo Depois volte a executar INSTALAR.bat.
  pause
  exit /b 1
)

winget install --id Python.Python.3.11 --exact --scope user --accept-source-agreements --accept-package-agreements
if errorlevel 1 (
  echo.
  echo ERRO: A instalacao automatica de Python nao foi concluida.
  echo Instale Python 3.11 ou superior em https://www.python.org/downloads/windows/
  pause
  exit /b 1
)

rem O launcher pode precisar de uma nova pesquisa apos a instalacao.
where py >nul 2>nul
if not errorlevel 1 (
  py -3.11 -c "import sys; raise SystemExit(0 if sys.version_info >= (3,11) else 1)" >nul 2>nul
  if not errorlevel 1 (
    set "PY_EXE=py"
    set "PY_ARGS=-3.11"
    goto preparar
  )
)

set "PY_HOME=%LocalAppData%\Programs\Python\Python311"
if exist "%PY_HOME%\python.exe" (
  set "PY_EXE=%PY_HOME%\python.exe"
  set "PY_ARGS="
  goto preparar
)

echo.
echo Python foi instalado, mas o executavel nao foi localizado.
echo Feche esta janela e execute INSTALAR.bat novamente.
pause
exit /b 1

:preparar
echo A preparar ambiente Python local...
if not exist ".venv\Scripts\python.exe" (
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
