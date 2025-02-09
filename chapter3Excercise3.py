# write a function called triangle
def triangle(char, height):
    for i in range(1, height +1):
        spaces = height -i #calculates leading spaces
        print(" " * spaces + char * i) #prints spaces followed by letters

#test function
triangle('T', 15)
