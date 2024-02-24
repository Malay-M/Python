from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='Images/image.png')

label = Label(window, text="Hello World",
               font=('Arial', 40, 'bold'),
                 fg = 'green', bg='black',
                 relief=RAISED,
                 bd=10,
                 padx=20,pady=20,
                 image=photo,
                 compound='bottom')
label.pack() #It will place the label on center of the window
#abel.place(x=0,y=0) # set the position of the label (x,y pixel)

window.mainloop()