import tkinter as tk
import pandas as pd
import random 


# ---- Variables ----
BACKGROUND_COLOR = "#B1DDC6"




app = tk.Tk()
app.title("Flash Card")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


data = pd.read_csv("Day-031/resources/data/french_words.csv")
df = pd.DataFrame.to_dict(data, orient='records')
# french_data = df['French']
# english_data = df['English']
# print(df)
# ---- Functions ----
def wrong():
    ran = random.choice(df)
    card.itemconfig(title_label, text=list(ran.keys())[0])
    card.itemconfig(word_label, text=ran["French"])
     


    print("wrong was pressed")

def right():
    ran = random.choice(df)
    card.itemconfig(title_label, text="French")
    card.itemconfig(word_label, text=ran["French"])
    print("right was pressed")





# ------ Layout ------

# -- canvas --
card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="resources/images/card_front.png")
card_back_image = tk.PhotoImage(file="resources/images/card_back.png")
card.create_image(400, 263, image=card_front_image,)
# -- Title Label --
title_label = card.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
# -- Word Label --
word_label = card. create_text(400, 263, text="Word",fill="black" ,font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)


# -- X Button --

wrong_btn_img = tk.PhotoImage(file="Day-031/resources/images/wrong.png")
wrong_button = tk.Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(row=1, column=0)

# -- Ok Button --
right_btn_img = tk.PhotoImage(file="Day-031/resources/images/right.png")
right_button = tk.Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
right_button.grid(row=1, column=1)







app.mainloop()