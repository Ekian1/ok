@echo off
title Harmless Ransom Simulator
color 0C

:: --- Step 1: Warnings ---
echo WARNING: This is a FAKE ransomware simulator.
echo It is completely SAFE and does NOT delete or harm your files.
echo Press any key to continue...
pause >nul

echo Epilepsy Warning: Simulation may flash colors.
echo Press any key to continue...
pause >nul

:: --- Step 2: Setup ---
set SECRET_CODE=LETMEOUT
set ENCRYPTION_FOLDER=ENCRYPTION

if not exist "%ENCRYPTION_FOLDER%" mkdir "%ENCRYPTION_FOLDER%"

:: Copy files safely
for %%f in (*.*) do (
    if not "%%f"=="%~nx0" (
        copy "%%f" "%ENCRYPTION_FOLDER%" >nul
    )
)

:: --- Step 3: Ransom Simulation ---
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

:: --- Step 4: Simulate encryption visually ---
:FLASH
color 0C
echo Encrypting files...
ping localhost -n 1 >nul
color 0A
echo Encrypting files...
ping localhost -n 1 >nul
color 0E
echo Encrypting files...
ping localhost -n 1 >nul
goto FLASH

:: --- Step 5: Require code to exit ---
:: Note: User can press Ctrl+C to interrupt the flashing and enter the code
