@echo off
echo ============================================
echo  Grammar Quiz - Windows EXE Builder
echo ============================================
echo.

:: Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Download from https://python.org
    pause
    exit /b 1
)

:: Install / upgrade PyInstaller
echo Installing PyInstaller...
pip install --upgrade pyinstaller

:: Build the EXE (single file, no console window)
echo.
echo Building grammar_quiz.exe ...
pyinstaller --onefile --windowed --name grammar_quiz grammar_quiz.py

if exist dist\grammar_quiz.exe (
    echo.
    echo ============================================
    echo  SUCCESS!  dist\grammar_quiz.exe is ready.
    echo ============================================
    echo.
    echo Next step: Run setup_wake_trigger.ps1 as
    echo Administrator to auto-launch on wake.
) else (
    echo Build failed - check output above.
)
pause
