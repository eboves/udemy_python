"""
Day XXX - [Project Name]
100 Days of Code - Python
Angela Yu's Python Bootcamp

Description:
[Brief description of what this program does]

Author: [Your Name]
Date: [Date]
Course: Udemy - 100 Days of Code: The Complete Python Pro Bootcamp
"""
import tkinter as tk
import tkinter.ttk

def count_click():
    # label['text'] = "I got clicked"
    # label.config(text="I got clicked")
    user_input = input.get()
    label.config(text=user_input)

window = tk.Tk()
window.title("First GUI Project")
window.minsize(width='500', height='300')

label = tk.Label(text="Hello", font=('Arial',24,'bold'))
# label.pack()
label.grid(column=0,row=0)

input = tk.Entry()
# print(input.get())
# input.pack()
input.grid(column=3, row=2)

button = tk.Button(text="click me", command=count_click)
# buttom.pack()
button.grid(column=1,row=1)

button_1 = tk.Button(text="new buttom", command=count_click)
# button.pack()
button_1.grid(column=2, row=0)


window.mainloop()