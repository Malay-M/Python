# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives


def num(num1, num2, num3):
    print("Num1:", num1, "Num2:", num2, "Num3:", num3)

num(10,20, 30)

num(num3=50, num1=200, num2=100)