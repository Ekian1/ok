@echo off
color 57
echo Hey, do you love me? (only answer in yes or no)
set /p love=

if /i "%love%"=="yes" goto love
if /i "%love%"=="no" goto hate

:love
echo I love you too...
echo Meet you soon :)
pause
exit

:hate
echo Your PC will crash in 10 seconds!
timeout /t 10 /nobreak
shutdown -s -t 100
