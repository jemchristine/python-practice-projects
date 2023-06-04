
"""
def main():
    height = get_height()
    for i in range(height):
        print("#")

#while loop is to ask user to input again if value input is negative or zero
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


main()
"""
"""
for i in range(4):
    print("?", end="!")
print()
"""

#print("?" * 4)


#for i in range(3):
#    print("#" * 3)