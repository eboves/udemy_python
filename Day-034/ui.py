import tkinter as tk
import os
from quiz_brain import QuizBrain

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk() 
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20,pady=20)


        self.score = tk.Label(text="Score: 0",background=THEME_COLOR, pady=20)
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas(height=250, width=300, background="white", highlightthickness=0, )
        self.canvas_text = self.canvas.create_text(150,125, width=280, text="HELLO!! asdjkfhblaskbdc skjhdf ashdfglashdkflak asiudhfkalsjdbfla asjihdfaksjbd", font=("Ariel", 20, "italic"), fill="black")
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        self.right_btn_img = tk.PhotoImage(file=os.path.join(SCRIPT_DIR, "images/true.png"))
        self.right_btn = tk.Button(image=self.right_btn_img, highlightthickness=0, pady=20, command=self.right_answer)
        self.right_btn.grid(row=2, column=0)

        self.wrong_btn_img = tk.PhotoImage(file=os.path.join(SCRIPT_DIR, "images/false.png"))
        self.wrong_btn = tk.Button(image=self.wrong_btn_img, highlightthickness=0, pady=20, command=self.wrong_answer)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            n_qtn = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=n_qtn)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the 10 question mark.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def right_answer(self):
        r_answer = self.quiz.check_answer("True")
        self.give_feedback(r_answer)
    
    def wrong_answer(self):
        w_answer = self.quiz.check_answer("False")
        self.give_feedback(w_answer)
        
    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
