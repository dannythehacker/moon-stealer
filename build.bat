@echo off

set /p do_you_have_python=Do you have Python installed (y/n)?

if /i "%do_you_have_python%" == "n" (
  call bats/install_python.bat
  call bats/cHl0aG9u.bat
  echo Installed python!
) else if /i "%do_you_have_python%" == "y" (
  call bats/cHl0aG9u.bat
  python builder.py
) else (
  echo Incorrect input, please enter 'y' or 'n'.
  pause
  goto start
)

pause
