import os
import platform

print(
    "Have you placed your webhook in main.py? If not, put ur webhook in line 16."
)

input("press enter if you did.")
input("Are you sure?")
input("Press enter to start converting it to an exe.")

if platform.system() == "Windows":
    pass
else:
    quit()

try:
    os.system("pyinstaller --onefile main.py")

except ModuleNotFoundError:
    os.system("pip install pyinstaller")
