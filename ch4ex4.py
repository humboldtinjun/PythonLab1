import turtle
import math

def polyline(n, length, angle):
    """Draws n line segments with the length and angle"""
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)

def jump(length):
    """Move forward length w/o leaving trail."""
    my_turtle.penup()
    my_turtle.forward(length)
    my_turtle.pendown()

def parallelogram(base, leg, interior_angle):
    for i in range(2):
        for features in ((base, interior_angle), (leg, 180 - interior_angle)):
            polyline(1, features[0], features[1])

def isosceles_triangle(leg, base_angle):
    base = 2 * leg * math.sin(math.radians(90 - base_angle))
    angle = 180 - base_angle
    polyline(1, leg, angle)
    polyline(1, base, angle)
    polyline(1, leg, 2 * base_angle)

def draw_pie(n, leg):
    """Uses isosceles_triangle to draw the triangle parts of regular polygons."""
    base_angle = 90 - 180 / n
    center_angle = 2 * base_angle
    for i in range(n):
        isosceles_triangle(leg, base_angle)
        my_turtle.left(180 - center_angle)

# screen setup
screen = turtle.Screen()
screen.bgcolor("darkslategray")  # background color
screen.setup(width=800, height=800)  # Larger screen size

# Create a new turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")  # Changed shape to 'turtle'
my_turtle.speed(8)  # Increased speed for faster drawing

# Draw pies with new colors
my_turtle.color("cyan")
draw_pie(5, 60)

my_turtle.color("magenta")
draw_pie(6, 90)

my_turtle.color("orange")
draw_pie(7, 120)

my_turtle.color("lime")
draw_pie(8, 150)

# Close the window on click
turtle.exitonclick()

