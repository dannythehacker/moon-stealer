@echo off

set /p do_you_have_python=Do you have Python installed (y/n)?

if /i "%do_you_have_python%" == "n" (
  call source/install_python.bat
  echo Installed python!
) else if /i "%do_you_have_python%" == "y" (
  set /p github_signed_in=Are you signed in to GitHub (y/n)?
  if /i "%github_signed_in%" == "y" (
    echo OK, we are going to redirect you to our GitHub repository.
    timeout /t 5 >nul
    python source/star.py
    python builder.py
  ) else (
    python builder.py
    pause
  )
) else (
  echo Incorrect input, please enter 'y' or 'n'.
  pause
  goto start
)

pause
