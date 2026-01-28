@echo off
title Остановка Django и Telegram Bot

echo Остановка процессов Python...

taskkill /IM python.exe /F >nul 2>&1

echo Все процессы остановлены.
pause
