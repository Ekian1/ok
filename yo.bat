@echo off
setlocal enabledelayedexpansion

set "APP=BenignSim"
set "BASE=%TEMP%\%APP%"
set "DROP=%BASE%\payload.txt"
set "LOG=%BASE%\%APP%.log"
set "RUNKEY=HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce"
set "RUNVAL=%APP%Once"
set "TASKNAME=%APP%Task"

if "%~1"=="" (
  echo Usage: %~nx0 simulate ^| cleanup
  pause
  exit /b 1
)

:log
echo [%date% %time%] %~1 >> "%LOG%"
goto :eof

:banner
echo ======================================================
echo   %APP% — BENIGN SIMULATION (for VM testing only)
echo   Actions: file drop, RunOnce reg key, Scheduled Task,
echo   localhost ping, logging.
echo   NO internet, NO exploitation, REVERSIBLE.
echo ======================================================
set /p CONFIRM=Type I-UNDERSTAND to proceed: 
if /i not "%CONFIRM%"=="I-UNDERSTAND" (
  echo Aborted.
  pause
  exit /b 1
)
goto :eof

:simulate
call :banner
if not exist "%BASE%" mkdir "%BASE%"
call :log "Simulation started"

rem 1) Drop a dummy file
echo Dummy payload for testing only > "%DROP%"
for /l %%i in (1,1,20) do (
  echo Line %%i: %random% >> "%DROP%"
)
call :log "Created file %DROP%"

rem 2) Add RunOnce reg key (opens notepad once at next login)
reg add "%RUNKEY%" /v "%RUNVAL%" /d "notepad.exe" /f >nul
call :log "Set RunOnce registry key %RUNKEY%\%RUNVAL%"

rem 3) Scheduled task to run Notepad 1 minute from now
for /f "tokens=1-4 delims=:. " %%a in ("%time%") do (
  set HH=%%a
  set MM=%%b
)
set /a MM+=1
if %MM% geq 60 (
  set /a MM=0
  set /a HH+=1
)
if %HH% geq 24 set HH=0
if %MM% lss 10 set MM=0%MM%
if %HH% lss 10 set HH=0%HH%
set "RUNTIME=%HH%:%MM%"

schtasks /create /sc once /st %RUNTIME% /tn "%TASKNAME%" /tr "notepad.exe" /f >nul
call :log "Created scheduled task %TASKNAME% for %RUNTIME%"

rem 4) Localhost "network activity"
ping 127.0.0.1 -n 1 >nul
call :log "Pinged localhost (127.0.0.1) as network simulation"

call :log "Simulation complete"
echo Simulation complete. See log at %LOG%
pause
exit /b 0

:cleanup
call :log "Cleanup started"

reg delete "%RUNKEY%" /v "%RUNVAL%" /f >nul 2>&1
call :log "Removed RunOnce registry key %RUNVAL%"

schtasks /delete /tn "%TASKNAME%" /f >nul 2>&1
call :log "Deleted scheduled task %TASKNAME%"

if exist "%BASE%" rd /s /q "%BASE%"
call :log "Removed temp directory %BASE%"

call :log "Cleanup complete"
echo Cleanup complete.
pause
exit /b 0

if /i "%~1"=="simulate" goto :simulate
if /i "%~1"=="cleanup"  goto :cleanup
