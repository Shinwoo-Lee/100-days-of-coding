import turtle
import pandas
FONT = ("Courier", 8, "bold")


# Basic setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0


df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
correct_answer_list = []
left_answer_list = []

game_is_on = True
while game_is_on:

    user = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another stste's name?")
    if user.lower() == "exit":
        game_is_on = False

        left_answer_list = list(set(all_states) - set(correct_answer_list))
        left_answer = pandas.DataFrame(left_answer_list)
        left_answer.to_csv("states_to_learn.csv")

    else:
        for name in df["state"]:
            # If user gets correct
            if user.lower() == name.lower():
                score += 1
                row = df[df["state"] == name]

                state_name = turtle.Turtle()
                state_name.hideturtle()
                state_name.penup()
                state_name.goto(int(row.x), int(row.y))
                state_name.write(name, align="center", font=FONT)

                correct_answer_list.append(name)
                if score == 50:
                    game_is_on = False
            else:
                pass
              
