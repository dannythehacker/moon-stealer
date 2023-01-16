pip install pyinstaller
set /P c=Directory of the python file: 
pyinstaller --onefile %c%
echo "Done! Now open the dist and you will see your exe there!"
