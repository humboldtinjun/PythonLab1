# Function Repeat
def repeat(text, times):
    """Prints the given string a specified number of times."""
    #if times <= 0:
        #print("Please provide a positive integer for times.")
        #return
    #for _ in range(times):
       #print(text)

# Example usage
repeat("Hello, world!", 3)
def repeat(text, n):
    print((text + '\\,n') * n, end='') # use '\\n' to add a new lin after repitition, i had to use the double \\ because python interpreted the single backslash as an escape sequence
#write a function named triangle that takes two parameters, a string and an integer.
#the function should use a for loop to print a pyramid of the string. the height of the pyramid
#should match the integer value, and the number of copies of the string should increase on each level

def triangle(char, height):
    for i in range(1, height + 1):
        print(char * i)
#debugging
def print_twice(string):
    print(cat)   # cat is not defined here
    print(cat)
#What’s wrong?cat is not defined inside the function or passed as a parameter.
# This will raise a NameError.