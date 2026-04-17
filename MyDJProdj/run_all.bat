@echo off
chcp 65001 >nul
title Django + Telegram Bot (logs to files)

echo ================================================
echo        Запуск Django + Telegram Bot
echo ================================================
echo.

cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Ошибка: не найден venv\Scripts\python.exe
    echo Создайте venv или поправьте путь.
    pause
    exit /b 1
)

set "PY=%~dp0venv\Scripts\python.exe"

if not exist logs mkdir logs

echo [1/2] Django runserver 8001...
start "" /B cmd /C "%PY% manage.py runserver 8001 >> logs/django.log 2>&1"

echo [2/2] Telegram Bot...
start "" /B cmd /C "%PY% bot_main.py >> logs/bot.log 2>&1"

REM --- Автоматически открыть браузер ---
start http://127.0.0.1:8001/

echo.
echo ================================================
echo Оба процесса запущены в фоне.
echo Логи пишутся в папку /logs:
echo   - django.log
echo   - bot.log
echo.
echo Для остановки используйте: stop_all.bat
echo ================================================
echo.

pause
