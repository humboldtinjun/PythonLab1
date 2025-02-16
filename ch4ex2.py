#Draw a rhombus
import turtle

def polyline(n, length, angle):
    """Draws n line segments with the given length and angle between them."""
    for _ in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def rhombus(side_length, angle):
    """Draws a rhombus using a for loop and polyline."""
    for _ in range(2):
        polyline(1, side_length, angle)  # Draw one side and turn
        polyline(1, side_length, 180 - angle)  # Draw the next side and turn back

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)

my_turtle = turtle.Turtle()
my_turtle.shape("circle")
my_turtle.color("pink")
my_turtle.speed(5)

# Test the rhombus function
rhombus(50, 60)

turtle.exitonclick()