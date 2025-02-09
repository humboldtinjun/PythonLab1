#rectangle
def rectangle(char, width, height):
    for i in range(height):
        print(char * width)

#test function
rectangle('h', 5, 4)