import turtle
import random

# Create a turtle object
t = turtle.Turtle()
t.speed(10)
t.hideturtle()

# Create a window to draw in
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
t.clear()

# Generalized Functions (Part 1)
def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_rectangle(t, width, height):
    """Draws a rectangle with the given width and height."""
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Present and Ribbon Functions
def jump(t, x, y):
    """Moves the turtle to (x, y) without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_ribbon(t, x, y, base, height, color="green"):
    """Draws a ribbon at the given (x, y) with the specified base and height."""
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    draw_rectangle(t, base, height)
    t.end_fill()

def draw_present(t, x, y, base, height, ribbon_width, color="red"):
    """Draws a present with a ribbon at the given (x, y)."""
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    draw_rectangle(t, base, height)
    t.end_fill()

    # Draw vertical ribbon
    r_x = (x + (base / 2)) - (ribbon_width / 2)
    draw_ribbon(t, r_x, y, ribbon_width, height)

    # Draw horizontal ribbon
    r_y = (y + (height / 2)) - (ribbon_width / 2)
    draw_ribbon(t, x, r_y, base, ribbon_width)

# Test the functions from Part 1
t.pencolor("white")
draw_square(t, 100)
draw_circle(t, 50)
draw_polygon(t, 6, 50)

# Draw a present with a ribbon
draw_present(t, -50, -100, 200, 100, 20)

# Keep the window open until the user clicks
turtle.exitonclick()
