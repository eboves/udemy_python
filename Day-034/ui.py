import tkinter as tk

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.canvas = tk.Canvas(height=250, width=300)
        self.canvas_text = self.canvas.create_text(125,15, text=E)



        self.window.mainloop()

# # -- canvas --
# card = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# card_front_image = tk.PhotoImage(file="Day-031/resources/images/card_front.png")
# card_back_image = tk.PhotoImage(file="Day-031/resources/images/card_back.png")
# back_ground_card = card.create_image(400, 263, image=card_front_image,)
# # -- Title Label --
# title_label = card.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
# # -- Word Label --
# word_label = card. create_text(400, 263, text="Word",fill="black" ,font=("Ariel", 60, "bold"))
# card.grid(row=0, column=0, columnspan=2)

# # -- X Button --
# wrong_btn_img = tk.PhotoImage(file="Day-031/resources/images/wrong.png")
# wrong_button = tk.Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
# wrong_button.grid(row=1, column=0)

# # -- Ok Button --
# right_btn_img = tk.PhotoImage(file="Day-031/resources/images/right.png")
# right_button = tk.Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
# right_button.grid(row=1, column=1)