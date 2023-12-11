import tkinter as tk
from tkinter import ttk, messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_list = password_letter + password_symbol + password_number

    password = "".join(password_list)
    
    pass_entry.delete(0, "end")
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    
    if website == "" or password == "":
        warning = messagebox.showwarning(title="Warning",message="Please don't have any fields empty!")
    else: 
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered :\nemail : {user}\npassword : {password}\nIs it okay to save?")
        
        if confirmation:
            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"{website} | {user} | {password}\n")
        
            website_entry.delete(0,'end')
            pass_entry.delete(0,'end')
            user_entry.delete(0,'end')
        
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(window, width=200, height=200)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column=1, row=0)

website_label = ttk.Label(window, text = "Website :")
website_label.grid(column=0, row=1, pady=2)

user_label = ttk.Label(window, text="Email/Username :")
user_label.grid(column=0, row=2, pady=2)

pass_label = ttk.Label(window, text="Password :")
pass_label.grid(column=0, row=3)

website_entry = ttk.Entry(window, width = 35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", pady=2)
website_entry.focus()

user_entry = ttk.Entry(window, width=35)
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=2)

pass_entry = ttk.Entry(window, width=21)
pass_entry.grid(column=1, row=3, sticky="ew", pady=2)

pass_button = ttk.Button(window, text="Generate Password", command = generate)
pass_button.grid(column=2, row=3, sticky="ew", pady=2, padx=1)

add_button = ttk.Button(window, width=36, text="Add", command = save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()