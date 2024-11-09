@echo off
:: Check if a log type is provided
if "%1"=="" (
    echo Please specify the log type. For example, enter
    echo   log daily
    echo   log sim
    exit /b 1
)

:: Change directory to the location of this script (log.bat)
cd /d %~dp0/log

:: Call the Python script with the first log type argument
python log.py %1

:: Check for errors
if %errorlevel% neq 0 (
    echo Failed to create log file for type: %1
) else (
    echo Log file created successfully for type: %1
)
