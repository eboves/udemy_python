import tkinter as tk

app = tk.Tk()
app.title("Password Manager")
app.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="Day-029/resources/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)



app.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #