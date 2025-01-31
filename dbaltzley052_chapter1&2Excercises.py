import math

# part 1 calculate the volume of a sphere
# radius is in centimeters
radius = 5 # cm
# volume is in cubic centimeters
volume =(4 / 3) * math.pi* radius **3
print("the volume of the sphere is {volume:.2f} cubic centimeters.")

# part 2: verify the trigonometry rule
# x create a variable named x with the value 42 (degrees)
x=42
# compute the sine and cosine of x
sine = math.sin(x)
cosine = math.cos(x)

# calculate the sum of their squares
sum_of_squares = sine **  2 + cosine ** 2

#print the results
print("The sum of squares of sine and cosine for x =", "is", sum_of_squares)

#part 3 compute e squared in three ways

# method 1: using math.e and the exponentation operator (**)
e_squared_op = math.e ** 2 # compute e^2 using the constant math.e and ** operator

# method 2: Using math.pow()
e_squared_pow = math.pow(math.e, 2) # compute e^2 using math.pow(base, exponent)

#method 3: using math.exp()
e_squared_exp = math.exp(2)

#print the results
print("e^2 using **", e_squared_op) # print the results of the first method
print("e^2 using math.pow:", e_squared_op) # print the results of the second method
print("e^2 using math.exp:", e_squared_exp) # print the results of the third method