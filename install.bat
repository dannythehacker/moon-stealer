@echo off
title moon
color 0a
cls

python --version 2>&1 | findstr " 3.11" >nul
if %errorlevel% == 0 (
    echo python 3.11.x and up are not supported by empyrean. Please downgrade to python 3.10.x.
    pause
    exit
)

py -3.10 -m pip install --upgrade -r requirements.txt

cls

py -3.10 builder.py

pause
