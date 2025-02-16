import turtle
import math


def polyline(n, length, angle):
    """Draws multiple connected lines at given angles.

    n: number of segments
    length: how long each segment is
    angle: how much the turtle turns between each line (in degrees)
    """
    for _ in range(n):
        t.forward(length)
        t.left(angle)


def polygon(n, length):
    """Draws a regular polygon with n sides of the same length."""
    angle = 360.0 / n
    polyline(n, length, angle)


def arc(radius, angle):
    """Draws an arc, which is part of a circle.

    radius: how big the circle is
    angle: how much of the circle to draw (in degrees)
    """
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30  # Divide the arc into 30 segments for a smooth look
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)


def leaves(radius, angle=90):
    """Draws one leaf-like shape using two arcs."""
    for _ in range(2):
        arc(radius, angle)
        t.left(180 - angle)


def flower(num_leaves, radius, leaf_angle=None):
    """Draws a flower with multiple leaves (petals).

    num_leaves: how many leaves (or petals) the flower will have
    radius: how big each leaf is
    leaf_angle: how wide each leaf should be (default is based on num_leaves)
    """
    rotate_angle = 360 / num_leaves
    leaf_angle = rotate_angle if not leaf_angle else leaf_angle
    for _ in range(num_leaves):
        leaves(radius, leaf_angle)
        t.left(rotate_angle)


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("darkblue")  # Changed background color
screen.setup(width=700, height=700)  # Larger screen size

# Create a new turtle object
t = turtle.Turtle()
t.shape("turtle")  # Changed shape to 'turtle'
t.color("magenta")  # Changed color to magenta
t.speed(8)  # Medium speed for better drawing experience

# Draw the flower
flower(12, 100, 75)  # Changed the flower to have 12 leaves with a 75-degree arc

# Keep the window open until clicked
turtle.exitonclick()