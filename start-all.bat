@echo off
echo ================================================
echo    PromptCraft AI - Full Stack (Windows)
echo ================================================
echo.

:: Start backend in new window
start "PromptCraft Backend" cmd /k "cd /d %~dp0 && call start-backend.bat"

timeout /t 5 >nul

:: Start frontend
echo Starting frontend...
cd /d %~dp0
call npm install
call npm run dev
