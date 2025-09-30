@echo off
REM Quick start script for Radiopaedia Pediatric Radiology (Windows)

echo ==================================================
echo   Radiología Pediátrica - Quick Start
echo ==================================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo Dependencies installed
) else (
    echo Dependencies already installed
)

echo.
echo Choose an option:
echo   1) Run the scraper (extract cases from Radiopaedia)
echo   2) Start the web application (view cases)
echo   3) Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    set /p url="Enter playlist URL (or press Enter for default): "
    if "!url!"=="" (
        python scraper.py
    ) else (
        python scraper.py !url!
    )
) else if "%choice%"=="2" (
    echo.
    echo Starting web application...
    echo Open your browser at: http://localhost:5000
    echo.
    python webapp.py
) else if "%choice%"=="3" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Exiting.
    exit /b 1
)

pause
