#1 Positional Arguments
def stu_names(name,rollno,marks,grades,course):
    print(name,rollno,marks,grades,course)

name=input("Name :")
rollno=int(input("Roll No"))
marks=input("Marks: ")
grades=input("Grades :")
course=input("Coures:")
stu_names(name,rollno,marks,grades,course)
stu_names(rollno,marks,grades,course,name)
# Note===positional arguments takes the arguments in oreder wise we can give values statically