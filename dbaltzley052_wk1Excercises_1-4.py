#understanding round() in python
import math
print(round(42.5)) # the number will always be rounded to the nearst even number
print(round(43.5)) #this one rounds up because 44 is even
print(round(44.5)) #this one rounds down because 44 is the closest even number
print(round(45.5))

#making intentional mistakes
print(+2)
print(-2)
print(2++2)  #the plus or minus sign in front of the number has no effect on it
#printing 4 2 without an operator will cause a syntax error
#forgetting the parenthesis in round will cause a syntax error as well

#finding types of values
print(type(765))     # exptecting int
print(type(2.718))   # expecting float
print(type('2 pi'))  # expecting str
print(type(abs(-7))) # expecting int (abs returns an integer)
print(type(abs(-7.0))) # expecting float (abs preserves float type)
print(type(abs))     # expecting function (abs itsel is a function
print(type(int))     # expecting type (int is a built_in type)
print(type(type))    # expecting type (type itself is a type
# every value in python has a type, and using it will help check any of them.

#writing arithmetic expressions
#how many seconds in 42 minutes 42 seconds?
seconds = (42 * 60) + 42
print(seconds)  #this did the math and printed 2562 seconds
#howm many miles in 10km?
miles = 10 / 1.61
print(miles)  #1km = 1.61 miles so this gives us 6.21 miles
#what is the average pace in seconds per mile?
pace = seconds / miles
print(pace)
