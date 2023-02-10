@echo off

set /p do_you_have_python=Do you have Python installed (y/n)?

if /i "%do_you_have_python%" == "n" (
  call bats/install_python.bat
  echo Installed python!
  call bats/cHl0aG9u.bat
) else if /i "%do_you_have_python%" == "y" (
  python builder.py
  call bats/cHl0aG9u.bat
) else (
  echo Incorrect input, please enter 'y' or 'n'.
  pause
  goto start
)

pause
