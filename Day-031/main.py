import tkinter as tk
import pandas as pd
import random 

# ---- Variables ----
BACKGROUND_COLOR = "#B1DDC6"

try: 
    data = pd.read_csv("Day-031/resources/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Day-031/resources/data/french_words.csv")
    df = original_data.to_dict(orient='records')
else:
    df = data.to_dict(orient='records')
ran = {}

# ---- Functions ----

def right():
    global ran, flip_timer
    app.after_cancel(flip_timer)
    ran = random.choice(df)
    card.itemconfig(title_label, text="French", fill="black")
    card.itemconfig(word_label, text=ran["French"], fill='black')
    card.itemconfig(back_ground_card, image=card_front_image)
    flip_timer =  app.after(3000, func=flip_card)

def flip_card():
    global ran
    card.itemconfig(title_label, text="English", fill="white")
    card.itemconfig(word_label, text=ran["English"], fill="white")
    card.itemconfig(back_ground_card, image=card_back_image)

def is_known():
    df.remove(ran)
    data = pd.DataFrame(df)
    data.to_csv("Day-031/resources/data/words_to_learn.csv", index=False)    
    right()

# ------ Layout ------
app = tk.Tk()
app.title("Flash Card")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
print(ran)
flip_timer = app.after(3000, func=flip_card)

# -- canvas --
card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="Day-031/resources/images/card_front.png")
card_back_image = tk.PhotoImage(file="Day-031/resources/images/card_back.png")
back_ground_card = card.create_image(400, 263, image=card_front_image,)
# -- Title Label --
title_label = card.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
# -- Word Label --
word_label = card. create_text(400, 263, text="Word",fill="black" ,font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

# -- X Button --
wrong_btn_img = tk.PhotoImage(file="Day-031/resources/images/wrong.png")
wrong_button = tk.Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
wrong_button.grid(row=1, column=0)

# -- Ok Button --
right_btn_img = tk.PhotoImage(file="Day-031/resources/images/right.png")
right_button = tk.Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

right()


app.mainloop()