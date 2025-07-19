#1 Built-in String Functions
text = "Hello World"
print(len(text)) #11

print(max("Python PRogramming")) #y
print(min("JavaProgramming")) #J

'''NOTE---->The Ascii value of a space is 32
 ,value of 'A' is 65 and a is 97'''

print(sorted("python")) #['h', 'n', 'o', 'p', 't', 'y']

#Character to ascii
print(ord('Z'))  #90

#Character to ascii
print(chr(49)) #1

#2 Case Conversion Methods

print("Attar Afrin".upper()) #ATTAR AFRIN
print("Hello".lower()) #hello
print("python".capitalize()) #Python
print("hello world".title()) #Hello World
print("PyThOn pRograMMing".swapcase()) #pYtHoN PrOGRAmmING
print("ß".casefold()) #ss

#3 Alignment & Formatting Methods
print("python".center(10, "*")) #**python**
print("py".ljust(5, "-") ) #py---
print("py".rjust(5, "-")) #---py
print("42".zfill(5)) #00042
print("Name: {}, Age:{}".format("Tom", 25)) #Name: Tom, Age:25
print("{name} is{age}".format_map({'name':'Tom', 'age': 25})) #Tom is25

#4 Search & Find Methods
print("hello".find("l")) #2
print("hello".rfind("l")) #3
print("hello".index("e")) #1
print("hello".rindex("l")) #1
print("banana".count("a")) #3

#5 String Testing Methods



