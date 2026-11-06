@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Execute primeiro INSTALAR.bat.
  pause
  exit /b 1
)
if not exist "data" mkdir data
".venv\Scripts\python.exe" -m streamlit run app\app.py --server.address 127.0.0.1 --server.port 8501 --server.headless false --browser.gatherUsageStats false
