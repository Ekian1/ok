@echo off
title Destructive Malware Simulator (SAFE DEMO)
color 0C
cls

echo ======================================================
echo  WARNING - THIS IS A SAFE MALWARE SIMULATION
echo ------------------------------------------------------
echo  It will NOT touch your files or apps.
echo  It will just flash colors, fake “chaos”,
echo  then pretend to shut down and delete itself.
echo ======================================================
echo.
set /p confirm=Type YES to run this demo: 

if /I not "%confirm%"=="YES" (
  echo Exiting safely...
  pause
  exit /b
)

:: Countdown
cls
echo Starting in 5 seconds... Press CTRL+C to abort.
for /l %%S in (5,-1,1) do (
  <nul set /p "=%%S "
  timeout /t 1 >nul
)
echo.

:: Visual chaos loop
for /l %%I in (1,1,30) do (
  cls
  color %random%
  echo !!!
  echo WARNING - System files corrupting... (SIMULATION)
  echo !!!
  echo.
  dir C:\Windows\System32 /b | sort /R | more
  timeout /t 1 >nul
)

:: Fake app movement
cls
color 1E
echo Moving applications... (SIMULATION)
ping localhost -n 2 >nul
echo [##########........] 40%%
ping localhost -n 2 >nul
echo [##################] 100%%
ping localhost -n 2 >nul

:: Fake error screen
cls
color 1F
echo.
echo A critical error has occurred.
echo Your PC will shut down in 10 seconds... (SIMULATION)
echo.
timeout /t 10 >nul

:: Fake shutdown
cls
color 0A
echo Shutting down...
timeout /t 3 >nul

:: Self-delete
del "%~f0"
exit
