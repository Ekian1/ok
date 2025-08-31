@echo off
setlocal EnableExtensions EnableDelayedExpansion
title Malware Simulator (SAFE) - Harmless Demo
mode con: cols=100 lines=35
color 4F

rem ===========================
rem SAFETY: This script is a harmless simulation.
rem It ONLY creates/renames/deletes files in .\SimSandbox
rem and then restores/cleans them up.
rem ===========================

:: --- Big warning screen ---
cls
echo ================================================================
echo                     !!!  WARNING  !!!
echo This is a HARMLESS *SIMULATION* of malware behavior.
echo It WILL NOT damage your system, but it will:
echo   - Create a .\SimSandbox folder in the current directory
echo   - Generate dummy files inside that folder
echo   - "Encrypt" them by renaming extensions
echo   - Pretend to delete and "exfiltrate" (simulated logs)
echo   - Restore everything and remove the folder at the end
echo.
echo It never touches files outside .\SimSandbox.
echo ================================================================
echo.
echo If you are not expecting this, close this window now.
echo.
pause

:: --- Double confirmation gate ---
set "CONFIRM1="
set "CONFIRM2="
cls
echo Type EXACTLY: I UNDERSTAND THIS IS A SIMULATION
set /p "CONFIRM1=> "
if /I not "%CONFIRM1%"=="I UNDERSTAND THIS IS A SIMULATION" (
  echo Confirmation failed. Exiting safely.
  goto :EOF
)

echo.
echo Final confirmation. Type EXACTLY: RUN SIMULATOR
set /p "CONFIRM2=> "
if /I not "%CONFIRM2%"=="RUN SIMULATOR" (
  echo Confirmation failed. Exiting safely.
  goto :EOF
)

:: --- Countdown with escape hint ---
cls
echo Starting in 5 seconds... Press CTRL+C to abort.
for /l %%S in (5,-1,1) do (
  <nul set /p "=%%S "
  timeout /t 1 >nul
)
echo.
echo Launching simulation...
timeout /t 1 >nul

:: --- Setup sandbox paths ---
set "ROOT=%cd%"
set "SIM=%ROOT%\SimSandbox"
set "LOG=%SIM%\simulator.log"

:: Clean old sandbox if it exists (SAFE: only inside SIM)
if exist "%SIM%" rd /s /q "%SIM%"
md "%SIM%\stage1" "%SIM%\stage2" "%SIM%\stage3" 2>nul

echo [%DATE% %TIME%] Simulator started > "%LOG%"

:: --- Generate dummy files (stage1) ---
echo Creating dummy files in "%SIM%\stage1" ...
for /l %%I in (1,1,50) do (
  set "F=%SIM%\stage1\report_%%I.txt"
  > "!F!" echo This is harmless dummy file number %%I
)
echo [%DATE% %TIME%] Created 50 files >> "%LOG%"

:: --- Simulate "enumeration" ---
echo Enumerating system info (simulated)...
ver >> "%LOG%"
echo USERNAME=%USERNAME% >> "%LOG%"
echo COMPUTERNAME=%COMPUTERNAME% >> "%LOG%"
timeout /t 1 >nul

:: --- Simulate "encryption" by renaming extensions ---
echo Simulating encryption...
for %%F in ("%SIM%\stage1\*.txt") do (
  ren "%%~fF" "%%~nF.locked" 2>nul
)
echo [%DATE% %TIME%] Renamed *.txt to *.locked >> "%LOG%"
call :progress "Encrypting" 40

:: --- Fake ransom note (inside sandbox only) ---
(
  echo ### Harmless Ransom Note (SIMULATION) ###
  echo Your files were "encrypted" for training.
  echo No real encryption occurred. This is a demo.
) > "%SIM%\stage1\READ_ME_SIMULATION.txt"

:: --- Simulate "exfiltration" (just copy internally) ---
echo Simulating exfiltration to stage2 (internal copy)...
xcopy /q /y "%SIM%\stage1\*.locked" "%SIM%\stage2\" >nul
echo [%DATE% %TIME%] Copied *.locked to stage2 >> "%LOG%"
call :progress "Exfiltrating" 30

:: --- Simulate "persistence" (writes a note only) ---
(
  echo [SIM ONLY] Would set persistence here; actually writing a note.
  echo Date: %DATE% %TIME%
) > "%SIM%\persistence_note.txt"
echo [%DATE% %TIME%] Wrote persistence_note.txt >> "%LOG%"
timeout /t 1 >nul

:: --- Fake scary messages & "shutdown" (not real) ---
color 0C
echo.
echo !!! SYSTEM COMPROMISED (SIMULATION) !!!
echo This is ONLY a demo. No changes outside SimSandbox.
echo Attempting system shutdown in 10 seconds... (SIMULATED)
call :countdown 10
echo (No real shutdown performed.)
echo [%DATE% %TIME%] Simulated shutdown >> "%LOG%"
timeout /t 1 >nul

:: --- Restore stage: undo "encryption" ---
echo Restoring files...
for %%F in ("%SIM%\stage1\*.locked") do (
  ren "%%~fF" "%%~nF.txt" 2>nul
)
echo [%DATE% %TIME%] Restored extensions >> "%LOG%"
call :progress "Restoring" 25

:: --- Cleanup sandbox completely ---
echo Cleaning up sandbox...
rd /s /q "%SIM%\stage2" "%SIM%\stage3" 2>nul
echo [%DATE% %TIME%] Removed stage2 and stage3 >> "%LOG%"
timeout /t 1 >nul

echo Finalizing...
echo [%DATE% %TIME%] Simulation complete >> "%LOG%"

:: Pack a summary report (kept for your review)
echo.
echo A log was saved here:
echo   %LOG%
echo You may open it to review simulated steps.
echo.
echo Press any key to delete the entire SimSandbox (recommended)...
pause >nul
rd /s /q "%SIM%"
echo Sandbox removed. Demo finished safely.
color 07
endlocal
goto :EOF

:: ================== helper routines ==================
:progress
:: %1 = label, %2 = steps
set "LBL=%~1"
set "STEPS=%~2"
set /a i=0
<nul set /p "=%LBL%: "
:progress_loop
if !i! GEQ %STEPS% goto :progress_end
<nul set /p ="#"
set /a i+=1
ping -n 1 127.0.0.1 >nul
goto :progress_loop
:progress_end
echo.
goto :eof

:countdown
:: %1 = seconds
set /a secs=%~1
for /l %%S in (%secs%,-1,1) do (
  <nul set /p ="%%S "
  timeout /t 1 >nul
)
echo.
goto :eof
