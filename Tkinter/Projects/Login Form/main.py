import tkinter
from tkinter import messagebox

def login():
    username="admin"
    password="12345"

    if username_entry.get()==username and password_entry.get()==password:
        print("Successfully logged in")
        messagebox.showinfo(title="Login success", message="You successfully logged in")
    else:
        print("Invalid login")
        messagebox.showerror(title="Login error", message="Invalid login")


window = tkinter.Tk()

window.title("Login Form")
window.geometry("340x440")
window.config(bg="#141526")


frame = tkinter.Frame(window, bg="#141526")


login_label = tkinter.Label(frame, text="Login", bg="#141526", fg="#ffffff", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg="#141526", fg="#ffffff", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg="#141526", fg="#ffffff", font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#0730e6", fg="#ffffff", font=("Arial", 16), command=login)


login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
