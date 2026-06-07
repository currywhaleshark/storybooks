@echo off
setlocal

cd /d "%~dp0"

set "PYTHON_EXE=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if not exist "%PYTHON_EXE%" (
  echo Bundled Codex Python was not found:
  echo %PYTHON_EXE%
  echo.
  echo Falling back to python on PATH.
  set "PYTHON_EXE=python"
)

echo Starting storybook TTS video web app...
echo.
echo Open this URL in your browser:
echo http://localhost:4174
echo.
echo Keep this window open while using the app.
echo Press Ctrl+C to stop the server.
echo.

"%PYTHON_EXE%" tools\tts-video\server.py
