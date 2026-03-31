import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

app = tk.Tk()
app.title("Password Manager")
app.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="Day-029/resources/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    list_letters = [random.choice(letters) for _ in range(nr_letters)]
    list_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    list_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = list_letters + list_symbols + list_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def add_pass():
    # print("hello")
    web = website_entry.get().title()
    email = email_username_entry.get()
    pswd = password_entry.get()
    email_pass = {web:{
        'email':email,
        'pswd':pswd
    }}


    if len(email) == 0 or len(pswd) == 0:
        messagebox.showinfo(title="Oops", message="Dont leave empty fields")
    else:
        
        with open('pass_gen.json', 'w') as output:
            json.dump(email_pass, output, indent=4)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)






# ---- WEBSITE LABEL ----
website = tk.Label(text="Website: ")
website.grid(row=1, column=0)

# ---- WEBSITE ENTRY FIELD ----
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# ---- EMAIL/ USER NAME FIELD ----
email_username = tk.Label(text="Email/Username: ")
email_username.grid(row=2, column=0)

# ---- EMAIL/ USER NAME ENTRY FIELD ----
email_username_entry = tk.Entry(width=35)
email_username_entry.insert(0, "mamin@aol.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# ---- PASSWORD FIELD ----
password_label = tk.Label(text='Password: ')
password_label.grid(row=3, column=0)

# ---- PASSWORD ENTRY FIELD ----
password_entry = tk.Entry(width=21)
password_entry.grid(row= 3, column=1)

# ---- BUTTON FIELD ----
gen_pass_btn = tk.Button(text='Generate Password', command=generate_password)
gen_pass_btn.grid(row=3, column=2)

# ---- BUTTON ENTRY FIELD ----
add_btn = tk.Button(text='Add', width=36, command=add_pass)
add_btn.grid(row=4, column=1, columnspan=2)









app.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #













