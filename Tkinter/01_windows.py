from tkinter import *

# widgets = GUI elements: buttons, textbox, labels, image
# windows = serves as a contrainer to hold or contain these widgets

window =  Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Tkinter title")

#replace icon on window bar
icon = PhotoImage(file='Images/image.png')
window.iconphoto(True, icon)

#change background colour
window.config(background='#000000')

window.mainloop() #place window on computer screen, listen for events
