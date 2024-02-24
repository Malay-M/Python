#radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ['Pizza', 'Burger', 'Hotdog']

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a burger")
    elif x.get() == 2:
        print("You ordered a hotdig")

window = Tk()


pizzaImage = PhotoImage(file='Images/pizza.png')
burgerImage = PhotoImage(file='Images/burger.png')
hotdogImage = PhotoImage(file='Images/hotdog.png')

foodImages = [pizzaImage, burgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, text= food[index],
                              variable=x, value=index,
                              padx=25,
                              font=("Impact", 50),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=0, #Eliminate circle indicators
                              width=400,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()