@echo off
setlocal

cd /d "%~dp0"

if "%PORT%"=="" set "PORT=4173"
set "NODE_EXE=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"

echo Starting print layout web tool...
echo URL: http://localhost:%PORT%
echo.
start "" "http://localhost:%PORT%"

if exist "%NODE_EXE%" (
  "%NODE_EXE%" tools\print-layout\server.js
) else (
  node tools\print-layout\server.js
)

if errorlevel 1 (
  echo.
  echo Could not start the print layout web tool.
  echo Install Node.js or run this from Codex where the bundled runtime is available.
  echo.
  pause
)

endlocal
