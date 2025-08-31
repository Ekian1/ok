@echo off
title Malware Simulator (SAFE DEMO)
color 4F
cls

echo ======================================================
echo  WARNING - This is a HARMLESS malware *SIMULATION*
echo ------------------------------------------------------
echo  It only makes a test folder, fakes encryption,
echo  then restores everything and deletes the folder.
echo  It NEVER touches files outside its folder.
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
echo Launching simulation...
timeout /t 1 >nul

:: --- Sandbox setup ---
set "SIM=%cd%\SimSandbox"
set "LOG=%SIM%\simulator.log"

if exist "%SIM%" rd /s /q "%SIM%"
md "%SIM%"

echo [%DATE% %TIME%] Simulator started > "%LOG%"

:: --- Make dummy files ---
echo Creating dummy files...
for /l %%I in (1,1,10) do (
  echo This is harmless file %%I > "%SIM%\file%%I.txt"
)
echo [%DATE% %TIME%] Dummy files created >> "%LOG%"

:: --- Fake encryption (rename extensions) ---
echo Simulating encryption...
for %%F in ("%SIM%\*.txt") do ren "%%F" "%%~nF.locked"
echo [%DATE% %TIME%] Files renamed to .locked >> "%LOG%"

:: --- Fake ransom note ---
echo ### RANSOM NOTE (SIMULATION) ### > "%SIM%\READ_ME.txt"
echo Your files are locked (not really). >> "%SIM%\READ_ME.txt"

:: --- Fake scary message ---
color 0C
echo.
echo !!! SYSTEM COMPROMISED (SIMULATION) !!!
timeout /t 3 >nul

:: --- Restore files ---
echo Restoring files...
for %%F in ("%SIM%\*.locked") do ren "%%F" "%%~nF.txt"
echo [%DATE% %TIME%] Files restored >> "%LOG%"

:: --- Cleanup ---
rd /s /q "%SIM%"
echo [%DATE% %TIME%] Sandbox deleted >> "%LOG%"

echo.
echo Simulation finished. All safe.
pause
exit /b
