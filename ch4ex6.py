#ask virtual assistant
import turtle


def spiral(step_length, angle, steps):
    """Draws a spiral by increasing the step length with each iteration.

    step_length: initial length of each step
    angle: how much to turn the turtle at each step
    steps: how many steps to draw
    """
    for i in range(steps):
        t.forward(step_length + i * 2)  # Increase step length with each iteration
        t.left(angle)


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgray")  # Background color
screen.setup(width=800, height=800)

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(10)  # Fast drawing speed

# Draw the spiral
spiral(step_length=5, angle=30, steps=60)

# Keep the window open until clicked
turtle.exitonclick()
