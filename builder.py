webhook = input("What is your webhook? ")

search_text = "whook"
replace_text = webhook

try:
    with open(r'main.py', 'r') as file:
  
        data = file.read()
  
        data = data.replace(search_text, replace_text)
  
    with open(r'main.py', 'w') as file:
  
        file.write(data)
    print("Successfully wrote your webhook to the src. Make sure again you entered a correct one!")
    time.sleep(0.5)
    print(f"This is the webhook you entered: {webhook}")
except:
    print("Failed to write your webhook to the src. Make sure the code is correct and has not been changed.")
    time.sleep(0.5)
    print(f"This is the webhook you entered: {webhook}")
