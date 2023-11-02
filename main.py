import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data["state"].tolist()


# FONT = ("Courier", 8, "normal")
# class Score(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.penup()
#         self.hideturtle()
#     def update_state(self,x,y,answer):
#         self.goto(x,y)
#         self.write(answer, False, align="center", font=FONT)

# score = Score()
guessed_states = []
score_count=0

while len(guessed_states)< 50:
    answer = screen.textinput(title="Guess the State", prompt=f"{len(guessed_states)}/50 what's another states's name?").title()
    if answer in state_list:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)

    if answer =="Exit":
        missing = pd.DataFrame(list(set(state_list).difference(set(guessed_states)))).to_csv("states_to_learn.csv")
        break