import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)

# Challenge 1: Draw a Square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

# Challenge 2: Draw a Dashed Line
# for i in range(15):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()

# Challenge 3: Draw Different Shapes
# def draw_shape(num_of_sides):
#     angle = int(360 / num_of_sides)
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(n)

# Challenge 4: Draw a Random Walk
# angle = [0, 90, 180, 270]
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.width(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random.choice(colours))
#     tim.setheading(random.choice(angle))
#     tim.forward(30)


# Challenge 5: Draw a Spirograph
# t.colormode(255)
# tim.speed("fastest")
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)


# The Painting Project
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

tim.shape("circle")
tim.pensize(20)
tim.speed("fastest")
tim.hideturtle()
for i in range(1, 11):
    for j in range(1, 11):
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.pendown()


screen = t.Screen()
screen.exitonclick()
