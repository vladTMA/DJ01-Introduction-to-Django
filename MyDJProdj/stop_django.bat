chcp 65001 >nul


@echo off
title Stop Django Server
echo ============================================
echo   Остановка Django-сервера (расширенная)
echo   %date% %time%
echo ============================================
echo.

setlocal enabledelayedexpansion
set FOUND=0

echo Поиск процессов Django на Python...
echo.

for /f "tokens=5" %%a in ('netstat -ano ^| findstr LISTENING ^| findstr python') do (
    set PID=%%a
    set FOUND=1
    echo Найден процесс Python/Django с PID=!PID!
    taskkill /PID !PID! /F >nul 2>&1
    echo Процесс !PID! завершён.
    echo.
)

if !FOUND! EQU 0 (
    echo Django-сервер не найден. Нет активных процессов Python, слушающих порты.
) else (
    echo Все найденные процессы Django успешно остановлены.
)

echo.
echo ============================================
echo   Завершено: %date% %time%
echo ============================================
echo.
echo Нажми любую клавишу, чтобы закрыть окно...
pause >nul
