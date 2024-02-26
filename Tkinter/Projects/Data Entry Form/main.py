import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accept = accept_var.get()

    if accept == "Accepted":

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:

            title = title_combobox.get()
            age = age_spinbox.get()
            continent = continent_comnobox.get()
            numcourse = numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()
            registered_status = reg_check_var.get()


            print("First Name: ", firstname, "Last Name: ", lastname)
            print("Title: ", title, "Age: ", age, "Continent:", continent)
            print("Courses: ", numcourse, "Semesters: ", numsemester)
            print("Registration status:", registered_status)
            print("-------------------------------------------------------------")
        
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required")


    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")


frame = tkinter.Frame(window)
frame.pack()


#User info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=10, pady=5)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1, padx=10, pady=5)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0, padx=10, pady=5)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2, padx=10, pady=5)
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.", "Mrs.", "Dr."])
title_combobox.grid(row=1, column=2, padx=10, pady=5)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0, padx=10, pady=5)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0, padx=10, pady=5)

continent_label = tkinter.Label(user_info_frame, text="Continent")
continent_label.grid(row=2, column=1, padx=10, pady=5)

continent_comnobox = ttk.Combobox(user_info_frame, values=["Asia","Africa","Anterctica","Europe","North America","South America","Oceania"])
continent_comnobox.grid(row=3, column=1, padx=10, pady=5)


#Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_label.grid(row=0, column=0, padx=10, pady=5)

reg_check_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_check_var,
                                       onvalue= "Registered", offvalue="Not Registered")
registered_check.grid(row=1, column=0, padx=10, pady=2)

numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_label.grid(row=0, column=1, padx=10, pady=5)
numcourses_spinbox = ttk.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_spinbox.grid(row=1, column=1, padx=10, pady=5)

numsemester_label = tkinter.Label(courses_frame, text="Semesters")
numsemester_label.grid(row=0, column=2, padx=10, pady=5)
numsemester_spinbox = ttk.Spinbox(courses_frame, from_=0, to='infinity')
numsemester_spinbox.grid(row=1, column=2, padx=10, pady=5)

#Terms and conditions
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=0, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0, padx=10, pady=5)


#Button
button = tkinter.Button(frame, text="Enter Text", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
