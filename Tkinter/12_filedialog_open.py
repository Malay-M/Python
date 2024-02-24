from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="F:\Code\Python\Tkinter\Tkinter",
                                          title="Open file",
                                          filetypes=(('text files','*.txt'),("all files","*.*")))
                                                                              
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()


button = Button(text='open', command=openFile)
button.pack()


window.mainloop()