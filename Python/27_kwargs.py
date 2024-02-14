# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments


def num(**kwargs):
    print("num1:", kwargs['num1'], "num3:", kwargs['num3'])

    for key,value in kwargs.items():
        print(value, end=" ")

num(num1=10, num2 = 30, num3 = 40, num4 = 50)