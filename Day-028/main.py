
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)
    canvas.itemconfig(timer_count,text=count)
    if count > 0:
        window.after(1000, count_down, count - 1 )

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

canvas = tk.Canvas(width=200, height=224)
tomato_img = tk.PhotoImage(file="Day-028/resources/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_count = canvas.create_text(105, 140, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"))
timer_label.grid(column=1, row=0)

start_btn = tk.Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(text="Reset", command="")
reset_btn.grid(column=2, row=2)

complete_checks = tk.Label(text="✔", fg=GREEN)
complete_checks.grid(column=1, row=3)






window.mainloop()


