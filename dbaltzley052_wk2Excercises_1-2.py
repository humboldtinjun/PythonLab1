# chapter 2 exercises
# what happens if you do 17 = n?
from dbaltzley052_chapter1excercises import e_squared_op

n = 17 # if tried in reverse you get a syntax error, values cannot be assigned var.
t = y = 1
print(t, y) # you get 1 1
      # you can chain assign variables to the same number
# what happens if you put a semicolon at the end of a statement?
# nothing happens, python ignores semicolons, unless used as seperators

# what happens if you put a period?
x=5 #if you put a period it will cause a syntax error
# what happens if you spell math as maath?
# python is case sensitive and will cause a syntax error

# use python as a calculator
import math
radius = 5 # cm
volume = (4/3) * math.pi * (radius ** 3) #volume of sphere formula
print("volume:", volume, "cubic cm")  # 523.6
x = 42 # degrees
#convert to degrees to radians becuz math.sin and math.cos use radians
radians = math.radians(x)

#compute sine and cosine
sin_x = math.sin(radians)
cos_x = math.cos(radians)
#compute sum of squares
sum_of_squares = sin_x**2 + cos_x**2
print("sin^2 + cos^2 =", sum_of_squares) #

#compute e2 in three ways
e_squared_op = math.e ** 2 #using **
e_squared_pow = math.pow(math.e, 2) #using math.pow
e_squared_exp = math.exp(2)  #using math.exp

print(f"e^2 using **: {e_squared_op:.20f}")
print(f"e^2 using math.pow: {e_squared_pow:.20f}")
print(f"e^2 using math.exp: {e_squared_exp:.20f}") #this is the most accurate for exponents
