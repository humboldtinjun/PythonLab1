#bottle verse
def bottle_verse(n):
    print(f"{n} bottles of beer on the wall")
    print(f"{n} bottles of beer")
    print("take one down, pass it around")
    print(f"{n-1} bottles of beer on the wall")
for n in range(99, 0, -1):
    bottle_verse(n) #this completes the whole song
    print()
#test function
bottle_verse(99)