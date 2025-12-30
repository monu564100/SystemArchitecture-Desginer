@echo off
echo ================================================
echo    PromptCraft AI - Backend Start (Gemini)
echo ================================================
echo.

cd backend

:: Check if .env exists
if not exist ".env" (
    echo [!] .env file not found. Creating from .env.example...
    copy .env.example .env
    echo [!] Please edit backend\.env and add your GEMINI_API_KEY
    echo [!] Get your key from: https://makersuite.google.com/app/apikey
    pause
    exit /b 1
)

:: Create virtual environment if not exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate venv and install deps
call venv\Scripts\activate
echo Installing dependencies...
pip install -r requirements.txt -q

echo.
echo ================================================
echo    Backend starting at http://localhost:8000
echo    Using Google Gemini API
echo ================================================
echo.

python run.py
