@echo off
title Django + Telegram Bot

echo Запуск виртуального окружения...
cd /d "D:\Python projects\DJ\DJ01-Introduction-to-Django\MyDJProdj"
call venv\Scripts\activate

echo.
echo Запуск Django на порту 8001...
start "Django Server" cmd /k "python manage.py runserver 8001"

echo.
echo Запуск Telegram-бота...
cd /d "D:\Python projects\DJ\DJ01-Introduction-to-Django"
start "Telegram Bot" cmd /k "python bot_main.py"

echo.
echo Все процессы запущены.
pause
