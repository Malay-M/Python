# if statement = a block of code that will execute if it's condition is True

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("Your age is not valid!")
else:
    print("You are a child!")