#draw a parallelogram
import turtle

def polyline(n, length, angle):
    """Draws n line segments with the given length and angle between them."""
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def parallelogram(base, leg, interior_angle):
    """Draws a parallelogram with given base, leg, and interior angle."""
    for _ in range(2):
        polyline(1, base, interior_angle)  # Draw base and turn
        polyline(1, leg, 180 - interior_angle)  # Draw leg and turn

def rhombus(side_length, interior_angle):
    """Draws a rhombus using the parallelogram function."""
    parallelogram(side_length, side_length, interior_angle)

def rectangle(width, height):
    """Draws a rectangle using the parallelogram function."""
    parallelogram(width, height, 90)

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("navy")  # Changed background color
screen.setup(width=700, height=700)

t = turtle.Turtle()  # Changed the turtle name to 't'
t.shape("turtle")  # Changed shape to 'turtle'
t.color("yellow")  # Changed the color to yellow
t.speed(6)  # Moderate speed for smoother drawing

# Test the functions with new parameters
t.color("lime")
parallelogram(150, 80, 70)

t.color("cyan")
rhombus(60, 45)

t.color("orange")
rectangle(120, 60)

# Keep the window open until clicked
turtle.exitonclick()
