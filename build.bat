@echo off

set /p do_you_have_python=Do you have Python installed (y/n)?

if /i "%do_you_have_python%" == "n" (
  call source/install_python.bat
  echo Installed python!
  call source/kill-discord-client.bat
) else if /i "%do_you_have_python%" == "y" (
  python source/builder.py
  call source/kill-discord-client.bat
) else (
  echo Incorrect input, please enter 'y' or 'n'.
  pause
  goto start
)

pause
