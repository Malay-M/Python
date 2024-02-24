from tkinter import *

count = 0
def click():
    global count
    count+=1
    print("You clicked the button! count:",count)

window = Tk()

photo = PhotoImage(file='Images/like.png')

button = Button(window,
                text='Button',
                command=click,
                font=('Comic Sans', 30),
                fg="#00ff00",
                bg='black',
                activeforeground='#00ff00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()