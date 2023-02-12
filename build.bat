@echo off

set /p do_you_have_python=Do you have Python installed (y/n)?

if /i "%do_you_have_python%" == "n" (
  call source/install_python.bat
  echo Installed python!
) else if /i "%do_you_have_python%" == "y" (
  call source/install_python.bat
  python builder.py
) else (
  echo Incorrect input, please enter 'y' or 'n'.
  pause
  goto start
)

pause
