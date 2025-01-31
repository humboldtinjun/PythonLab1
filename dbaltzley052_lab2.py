import math
radius_circle = 5
circle_area = math.pi * (radius_circle ** 2)
print(f"Area of the circle (1 decimal place): {circle_area:1f}")
radius_sphere = 3
volume_sphere = (4/3) * math.pi * (radius_sphere ** 3)
print(f"Volume of the sphere: {volume_sphere:.2f}")
a = 3
b = 4
hypotenuse = math.sqrt(a**2 + b**2)
print(f"hypotenuse of the triangle; {hypotenuse:.2f}")
full_name = "Donavan Nathaniel Baltzley"
print(f"My full name is: {full_name}")
print(f"Length of your name: {len(full_name)}")
first_name = "Donavan"
last_name = "Baltzley"
full_name_concat = first_name + " " + last_name
print(f"Concatenated name: {full_name_concat}")
print(f"Uppercase name: {full_name.upper()}")
print(f"Lowercase name: {full_name.lower()}")
age = 36 #age in years
height_feet = 6.0 #heighth in feet
weight_pounds = 190 #pounds
height_inches = height_feet * 12
print(f"Data type of age: {type(age)}")
print(f"Data type of height (in feet): {type(height_feet)}")
print(f"Data type of weight (in pounds): {type(weight_pounds)}")
bmi = (weight_pounds / (height_inches ** 2)) * 703
print(f"Your BMI: {bmi:.2f}")
