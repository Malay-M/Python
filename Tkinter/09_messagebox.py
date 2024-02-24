from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info message box', message="This is a message")

    #messagebox.showwarning(title='Warning', message="This is a message")

    #messagebox.showerror(title='error', message="Something went wrong")

    # choice = messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the things?")

    # if choice:
    #     print("You did yes")
    # else:
    #     print("You canceled")

    # choice = messagebox.askretrycancel(title="ask retry cancel", message="Do you want to retry the things?")
    # if choice:
    #     print("You retried")
    # else:
    #     print("You canceled")

    # choice = messagebox.askyesno(title="ask yes or no", message="Do you like cake?")
    # if choice:
    #     print("You like cake")
    # else:
    #     print("You don't like cake")

    # answer = messagebox.askquestion(title="ask question", message="Do you like cake?")
    # if answer == "yes":
    #     print("You like cake")
    # else:
    #     print("You don't like cake")

    choice = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?", icon='info')
    if choice == True:
        print("You like to code")
    elif choice == False:
        print("You don't like code")
    else:
        print("You canceled the question")

    
window = Tk()


button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
