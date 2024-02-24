from tkinter import *
import time 


WIDTH = 500
HEIGHT = 500
xSpeed = 3
ySpeed = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

backgroundImage = PhotoImage(file='Images/space.png')
background = canvas.create_image(0,0, image=backgroundImage, anchor=NW)

photo_image = PhotoImage(file='Images/ufo.png')
my_image = canvas.create_image(0,0,image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()


while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0:
        xSpeed = -xSpeed
    if coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0:
        ySpeed = -ySpeed
    canvas.move(my_image, xSpeed, ySpeed)
    window.update()
    time.sleep(0.01)


window.mainloop()