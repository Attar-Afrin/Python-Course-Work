#1 Positional Arguments
'''def stu_names(name,rollno,marks,grades,course):
    print(name,rollno,marks,grades,course)

name=input("Name :")
rollno=int(input("Roll No"))
marks=input("Marks: ")
grades=input("Grades :")
course=input("Coures:")
stu_names(name,rollno,marks,grades,course)
'''
'''Name :Afrin
Roll No503
Marks: 100
Grades :A
Coures:python
Afrin 503 100 A python
'''
'''stu_names(rollno,marks,grades,course,name)
# Note===positional arguments takes the arguments in oreder wise we can give values statically
'''

#2 Keyword Arguments
def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name=name,rollno=rollno,marks=marks,grade=grade,course=student_course)

student_details(rollno=rollno,name=name,grade=grade,course=student_course,marks=marks)

student_details(rollno=56,name='ramya',grade='A',course='Mysql',marks=99)
'''
Name: Afreen
Roll no: 23
Marks: 432
Grade: a
Course: python
Name: Afreen
Rollno: 23
Marks: 432
Grade: a
Course: python
Name: Afreen
Rollno: 23
Marks: 432
Grade: a
Course: python
Name: ramya
Rollno: 56
Marks: 99
Grade: A
Course: Mysql
'''
