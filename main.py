# TURTLE AND THE GRAPHICAL USER INTERFACE
import random
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("RoyalBlue4")

# GUI - Graphical User Interface

# Challenge 1 - Drawing a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Importing Modules
#   Basic import: import turtle
#   from turtle import Turtle - useful when using module a lot
#   from turtle import * - imports ALL modules

# Alias Modules
#   import turtle as t - an alias that WE define

# Installing Modules
#   must install modules before importing them
#   red light bulb prompts to install the package when importing

# Challenge 2 - Draw a Dashed Line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3

# def draw_shape(sides):
#     angle = 360/sides
#     colormode(255)
#     tim.pencolor(
#         randint(0, 255),
#         randint(0, 255),
#         randint(0, 255)
#     )
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

# # Challenge 4 - Random Walk
#
#


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
#
#
# degrees = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(10)
# colormode(255)
#
# for _ in range(200):
#     tim.setheading(random.choice(degrees))
#     tim.pencolor(random_color())
#     tim.forward(30)

# Python Tuples
#   (1, 3, 8) - round brackets with three items separated by a comma
#   tuple[2] // 8
#   A tuple is carved in stone and you cannot change the values (immutable)
#   list(tuple) converts a tuple into a list
#   Turtle colors can be an rgb tuple -- rgb(0, 0, 0)

# Challenge 5 - Spirograph


colormode(255)
angle = 0
tim.speed('fastest')

while angle <= 360:
    tim.pencolor(random_color())
    tim.setheading(angle)
    tim.circle(100)
    angle += 10


screen = Screen()
screen.exitonclick()
