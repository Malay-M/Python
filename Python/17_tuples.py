# tuple = collection which is ordered and unchangeable 
#         used to group together related data

student = ("student1", 21, "male")

print(student.count("student1"))

print(student.index("male"))

for x in student:
    print(x)

if "student1" in student:
    print("Student is here!")