@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..\..") do set "REPO_ROOT=%%~fI"
set "GCLOUD_PY=%LOCALAPPDATA%\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython\python.exe"

if not exist "%GCLOUD_PY%" (
  echo Google Cloud SDK bundled Python was not found:
  echo   %GCLOUD_PY%
  echo.
  echo Install Google Cloud SDK or update tools\tts-video\start_tts_video_server.cmd.
  exit /b 1
)

cd /d "%REPO_ROOT%"
echo TTS video web tool: http://localhost:4174
echo Press Ctrl+C to stop the server.
"%GCLOUD_PY%" -X utf8 "tools\tts-video\server.py"
