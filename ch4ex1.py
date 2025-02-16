#excercis 1 draw a rectangle
import turtle

def polyline(n, length, angle):
    """Draws n line segments with the given length and angle between them."""
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def rectangle(width, height):
    """Draws a rectangle using polyline."""
    for i in range(2):
        polyline(1, width, 90) #draw the width and turn 90 degrees
        polyline(1, height, 90) #draw the height and turn 90 degrees

# set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("red")
screen.setup(width=700, height=700)

my_turtle = turtle.Turtle()
my_turtle.shape("circle")
my_turtle.color("pink")
my_turtle.speed(2)

# Test
rectangle(80, 40)

turtle.exitonclick()
