#frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="black", bd=5, relief=RAISED)
# frame.place(x=100,y=100)
frame.pack()

button = Button(frame, text="W", font=("Consolas", 25), width=3)
button.pack(side=TOP)
button = Button(frame, text="A", font=("Consolas", 25), width=3)
button.pack(side=LEFT)
button = Button(frame, text="S", font=("Consolas", 25), width=3)
button.pack(side=LEFT)
button = Button(frame, text="D", font=("Consolas", 25), width=3)
button.pack(side=LEFT)



window.mainloop()