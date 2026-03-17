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

# window = tkinter.ttk()
window = tk.Tk()
window.title("First GUI Project")
window.minsize(width='500', height='300')



label = tk.Label(text="Hello", font=('Arial',24,'bold'))
label.pack()

input = tk.Entry()
input.pack()


print(input)


def count_click():
    # label['text'] = "I got clicked"
    # label.config(text="I got clicked")
    print("before get")
    print(input.get())

    user_input = input.get()
    label.config(text=user_input)
    print("after config")






buttom = tk.Button(text="click me", command=count_click)
buttom.pack()









window.mainloop()