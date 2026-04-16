@echo off
chcp 65001 >nul
title Stop Django + Telegram Bot

echo ================================================
echo        Остановка Django + Telegram Bot
echo ================================================
echo.

REM -------------------------------
REM 1. Остановка Django (порт 8001)
REM -------------------------------
echo [1/2] Поиск Django-сервера на порту 8001...

for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8001 ^| findstr LISTENING') do (
    echo Найден процесс Django с PID %%a
    taskkill /PID %%a /F >nul 2>&1
    echo Django-сервер остановлен.
    set DJANGO_KILLED=1
)

if not defined DJANGO_KILLED (
    echo Django-сервер не найден.
)

echo.

REM -------------------------------
REM 2. Остановка Telegram-бота
REM -------------------------------
echo [2/2] Поиск процесса Telegram-бота (bot_main.py)...

for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%bot_main.py%%'" get ProcessId /format:csv ^| findstr /R "[0-9]"') do (
    echo Найден процесс бота с PID %%a
    taskkill /PID %%a /F >nul 2>&1
    echo Telegram-бот остановлен.
    set BOT_KILLED=1
)

if not defined BOT_KILLED (
    echo Telegram-бот не найден.
)

echo.
echo ================================================
echo        Остановка завершена
echo ================================================
echo.
pause
