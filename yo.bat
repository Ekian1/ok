@echo off
title Malware Simulator (SAFE Demo)
color 4F
cls

echo ======================================================
echo   !!!  WARNING - SAFE MALWARE SIMULATION  !!!
echo ------------------------------------------------------
echo This script is a harmless VISUAL demo.
echo It will:
echo   - Flash CMD colors and titles
echo   - Move fake "apps" (just text) around
echo   - Pretend to corrupt the system
echo   - Do a fake shutdown
echo   - Delete only itself at the end
echo
echo It NEVER touches your files or apps.
echo ======================================================
echo.
set /p confirm=Type YES to continue: 

if /I not "%confirm%"=="YES" (
  echo Exiting safely...
  pause
  exit /b
)

:: --- Countdown ---
cls
echo Starting in 5 seconds... Press CTRL+C to abort.
for /l %%S in (5,-1,1) do (
  <nul set /p "=%%S "
  timeout /t 1 >nul
)
echo.
echo Simulation starting...
timeout /t 1 >nul

:: --- Flashing colors and titles ---
for /l %%i in (1,1,12) do (
  color 0A
  title VIRUS ALERT %%i
  ping -n 1 127.0.0.1 >nul
  color 0C
  title SYSTEM COMPROMISED %%i
  ping -n 1 127.0.0.1 >nul
)

:: --- Fake "apps" moving around ---
cls
setlocal enabledelayedexpansion
for /l %%x in (1,1,30) do (
  cls
  set /a xpos=!random! %% 40
  set /a ypos=!random! %% 15
  for /l %%y in (1,1,!ypos!) do echo.
  for /l %%z in (1,1,!xpos!) do <nul set /p= 
  echo [APP %%x]
  ping -n 1 127.0.0.1 >nul
)

:: --- Fake corruption effect ---
for /l %%i in (1,1,20) do (
  color 0C
  echo ######## SYSTEM FILES DELETED ########
  ping -n 1 127.0.0.1 >nul
  color 0A
  echo @@@@@@@@ DATA CORRUPTION @@@@@@@@@@
  ping -n 1 127.0.0.1 >nul
)

:: --- Scary banner ---
color 0C
cls
echo *******************************************************
echo !!!  SYSTEM FAILURE - SIMULATION ONLY  !!!
echo *******************************************************
timeout /t 4 >nul

:: --- Fake shutdown ---
echo Simulating shutdown...
timeout /t 3 >nul
:: Uncomment the next line if you want REAL shutdown
:: shutdown -s -t 5

:: --- Self-delete ---
echo Cleaning up (self-delete)...
(
  echo @echo off
  echo timeout /t 2 >nul
  echo del "%%~f0"
) > "%temp%\deleteme.bat"
start "" "%temp%\deleteme.bat"

exit /b
