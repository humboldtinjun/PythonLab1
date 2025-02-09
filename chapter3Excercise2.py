#write a function called print_right
def print_right(text):
    spaces = 40 - len(text) # creates a variable called spaces
    print(" " * spaces + text)

#test the function
print_right("monty")
print_right("Python's")
print_right("Flying Circus")