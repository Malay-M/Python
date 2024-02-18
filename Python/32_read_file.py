try:
    with open('text.txt') as file:
        print(file.read())
except FileExistsError:
    print("That file was not found")

print(file.closed)