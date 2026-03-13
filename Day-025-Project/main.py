import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
# image = "Day-025-Project/blank_states_img.gif"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


right_guess = []
missing_state = []
score = 0
states = 5

# data = pd.read_csv("Day-025-Project/50_states.csv")
data = pd.read_csv("50_states.csv")
# print(data.head)

states = data['state'].to_list()

is_game = len(right_guess) < 50
while is_game:
    answer_state = screen.textinput(title=f"{score}/50 Guess a State", prompt="What's another State name?").title() 

    if answer_state == "Exit" or answer_state == 'E':
        for state in states:
            if state not in right_guess:
                missing_state.append(state)
        new_doc = pd.DataFrame(missing_state)
        new_doc.to_csv("learn_this_states.csv") 
        break
    print(missing_state)    
    if answer_state in states:
    # print("right")
        x_cord = int(data[data['state'] == answer_state]['x'])
        y_cord = int(data[data['state'] == answer_state]['y'])
        right_guess.append([x_cord,y_cord])
        score +=1

    print(score)    
    print(right_guess)
    
    

print(right_guess)

# This is how you get the X and Y values used in the CSV file.
# def get_mouse_click(x, y):
#     print(x,y)


# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()screen.exitonclick()

