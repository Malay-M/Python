from tkinter import *

def create_window():
    #new_window = Toplevel() #Toplevel() = new window 'on top' of other windows, linked to a button window
    new_window = Tk()        #Tk() = new independent window
    window.destroy()


window = Tk()

button = Button(window, text="create new window", command=create_window)
button.pack()


window.mainloop()
