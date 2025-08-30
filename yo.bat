@echo off
title Harmless Ransom Simulator

:: --- Step 1: Warnings ---
echo WARNING: This is a FAKE ransomware simulator.
echo It is completely SAFE and does NOT delete or harm your files.
echo Press any key to continue...
pause >nul

echo Epilepsy Warning: The simulation may flash colors or display a fullscreen effect.
echo Press any key to continue...
pause >nul

:: --- Step 2: Setup ---
set SECRET_CODE=LETMEOUT
set ENCRYPTION_FOLDER=ENCRYPTION

:: Create fake encryption folder
if not exist "%ENCRYPTION_FOLDER%" mkdir "%ENCRYPTION_FOLDER%"

:: Copy files to fake encryption folder (safe)
for %%f in (*.*) do (
    if not "%%f"=="%~nx0" (
        copy "%%f" "%ENCRYPTION_FOLDER%" >nul
    )
)

:: --- Step 3: Ransom Note ---
cls
echo ==========================================
echo       ⚠⚠⚠ YOUR FILES HAVE BEEN "ENCRYPTED" ⚠⚠⚠
echo.
echo This is a FAKE ransomware simulator.
echo Do NOT worry, your files are SAFE.
echo All your files have been copied to the folder "%ENCRYPTION_FOLDER%"
echo They were NOT deleted or harmed.
echo.
echo To exit this simulator, type the secret code below:
echo SECRET CODE: %SECRET_CODE%
echo For entertainment and content creation only.
echo ==========================================
echo.

:: --- Step 4: Require code to exit ---
:ASKCODE
set /p USERCODE=Enter Secret Code to exit: 
if /i "%USERCODE%"=="%SECRET_CODE%" goto END
echo Incorrect code. Try again.
goto ASKCODE

:END
echo Exiting simulator...
pause >nul
exit
