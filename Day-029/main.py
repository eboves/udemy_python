import tkinter as tk

app = tk.Tk()
app.title("Password Manager")
app.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="Day-029/resources/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)



def add_pass():
    # print("hello")
    web = website_entry.get().title()
    email = email_username_entry.get()
    pswd = password_entry.get()
    full_string = f"{web} | {email} | {pswd}" 
    with open('pass_gen.txt', 'a') as output:
        output.write(full_string + "/n")

    # email.delete(0, "")
    # pswd.delete(0, "")









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
email_username_entry.grid(row=2, column=1, columnspan=2)

# ---- PASSWORD FIELD ----
password = tk.Label(text='Password: ')
password.grid(row=3, column=0)

# ---- PASSWORD ENTRY FIELD ----
password_entry = tk.Entry(width=21)
password_entry.grid(row= 3, column=1)

# ---- BUTTON FIELD ----
gen_pass_btn = tk.Button(text='Generate Password')
gen_pass_btn.grid(row=3, column=2)

# ---- BUTTON ENTRY FIELD ----
add_btn = tk.Button(text='Add', width=36, command=add_pass)
add_btn.grid(row=4, column=1, columnspan=2)









app.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #













