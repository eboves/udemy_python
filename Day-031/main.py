import tkinter as tk


# ---- Variables ----
BACKGROUND_COLOR = "#B1DDC6"




app = tk.Tk()
app.title("Flash Card")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



# ---- Functions ----





# ------ Layout ------

# -- canvas --
card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="Day-031/resources/images/card_front.png")
card.create_image(400, 263, image=card_front_image,)
# -- Title Label --
title_label = card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
# -- Word Label --
word_label = card. create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)


# -- X Button --

wrong_btn_img = tk.PhotoImage(file="Day-031/resources/images/wrong.png")
wrong_button = tk.Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

# -- Ok Button --
right_btn_img = tk.PhotoImage(file="Day-031/resources/images/right.png")
right_button = tk.Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)







app.mainloop()