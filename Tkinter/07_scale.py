from tkinter import *

def submit():
    print("The temperature is:",scale.get(),"degree C")

window = Tk()

hotImage = PhotoImage(file='Images/hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, from_=100, to=0,
              length=600,
              orient=VERTICAL,  #orientation of scale
              font = ('Consolas', 20),
              tickinterval=10, #adds numeric indicators for value
              #showvalue=0 #hide current value      
              resolution= 2, # increment of slider              
              troughcolor="#69eafe",
              fg = '#ff1c00',
              bg='black'
              )


scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file='Images/cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()


button = Button(window, text='submit', command=submit)
button.pack()


window.mainloop()