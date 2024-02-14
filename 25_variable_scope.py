# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

str1 = "global" # global scope (available inside & outside functions)

def display():
    str1 = "local" # local scope (available only inside this function)
    print(str1)

display()
print(str1)