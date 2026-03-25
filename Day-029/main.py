import tkinter as tk

app = tk.Tk()
app.title("Password Manager")
app.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="Day-029/resources/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# ---- WEBSITE LABEL ----
website = tk.Label(text="Website:")
website.grid(row=1, column=0)

# ---- WEBSITE ENTRY FIELD ----
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1)

# ---- EMAIL/ USER NAME FIELD ----
email_username = tk.Label(text="Email/Username:")













app.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #













