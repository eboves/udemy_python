import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "Day-025-Project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


right_guess = []
score = 0
states = 5

answer_state = screen.textinput(title="Guess a State", prompt="What's another State name?").title()
# print(answer_state)
data = pd.read_csv("Day-025-Project/50_states.csv")
# print(data.head)
coordiantes = data[data['state'] == answer_state]
# print(coordiantes)








# This is how you get the X and Y values used in the CSV file.
# def get_mouse_click(x, y):
#     print(x,y)


# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()screen.exitonclick()

