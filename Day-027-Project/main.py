# print("Hello, World")
"""
This project converts miles to km. Using Tkinter as the GUI


"""

import tkinter as tk

def calculate():
    user_input = float(entry_mile.get())
    calc = user_input * 1.6
    label_zero.config(text=calc)



window = tk.Tk()
window.title("Converter Calculator")
window.minsize(width=500, height=300)

entry_mile = tk.Entry()
entry_mile.grid(column=1, row=0)

label_miles = tk.Label(text="Miles")
label_miles.grid(column=2,row=0)

label_equal = tk.Label(text="Is equal to")
label_equal.grid(column=0, row=1)

label_zero = tk.Label(text="0")
label_zero.grid(column=1, row=1)

label_km = tk.Label(text="Km")
label_km.grid(column=2, row=1)

calc_but = tk.Button(text="Calculate", command=calculate)
calc_but.grid(column=1, row=2)






window.mainloop()
