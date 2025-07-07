# Kristopher Bright	
# 7/7/2025	
# graphical output of a square and triangle using turtles all the way down

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

# draw a square
for side in [0, 1, 2, 3]:
    pen.forward(100)
    pen.right(90)

# get out of the way!
pen.penup()
pen.goto(150, 0)  
pen.pendown()

# draw a triangle
for side in [0, 1, 2]:
	pen.forward(100)
	pen.right(120)

screen.exitonclick()
