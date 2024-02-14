# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains True


# while 1 == 1:
#     print("Infinite Loop")

name = ""

while len(name) == 0:
    name = input("Enter your name:")

print("Hello " + name)