from tkinter import * 

#grid() = geometry manager that organized widgets in a table-like structure

window = Tk()

title = Label(window, text="Enter your info", font=("Arial", 25))
title.grid(row=0, column=0, columnspan=2)
firstNameLabel = Label(window, text="First name: ", width=20, bg="red")
# firstNameLabel.pack()
firstNameLabel.grid(row=1,column=0)

firstNameEntry = Entry(window)
# firstNameEntry.pack()
firstNameEntry.grid(row=1,column=1)


lastNameLabel = Label(window, text="Last name: ", bg="green")
lastNameLabel.grid(row=2,column=0)

lastNameEntry = Entry(window)
lastNameEntry.grid(row=2,column=1)


emailLabel = Label(window, text="Email:", bg="blue", width=30)
emailLabel.grid(row=3, column=0)

emailEntry = Entry(window)
emailEntry.grid(row=3,column=1)


submitButton = Button(text="submit")
submitButton.grid(row=4,column=0, columnspan=2)

window.mainloop()
