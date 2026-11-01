@echo off
py -3 "%~dp0patch.py" %*
exit /b %errorlevel%
