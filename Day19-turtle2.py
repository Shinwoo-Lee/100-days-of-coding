from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color of it.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    y_spot = -70 + (30 * index)
    new_turtle.goto(x=-230, y=y_spot)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()