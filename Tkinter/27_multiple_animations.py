class Ball:

    def __init__(self, canvas, x, y, diameter, xSpeed, ySpeed, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)

        if coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0:
            self.xSpeed = -self.xSpeed
        
        if coordinates[3]>=(self.canvas.winfo_width()) or coordinates[1]<0:
            self.ySpeed = -self.ySpeed

        self.canvas.move(self.image,self.xSpeed,self.ySpeed)


from tkinter import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volly_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volly_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
