#1. Creation of the Dictionary
student = {

"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student) #{'name': 'Alice', 'age': 21, 'course': 'Computer Science'}

#2 Accessing Values
print(student["name"]) #Alice
print(student.get("course"))#Computer Science
# print(student["Duration"]) NOTE-->KeyError
print(student.get("Duration")) #None
print(student.get("Duration","6")) #6 Second one is default if the key is not present then it shows deafault

#2.2 Adding And Updating
student["age"]=22
print(student) #{'name': 'Alice', 'age': 22, 'course': 'Computer Science'}
student["Time"]="Afternoon"
print(student) #{'name': 'Alice', 'age': 22, 'course': 'Computer Science', 'Time': 'Afternoon'}

#2.3 Removing elements
print(student.pop("age")) #22
print(student) #{'name': 'Alice', 'course': 'Computer Science', 'Time': 'Afternoon'}

del student["course"]
print(student) #{'name': 'Alice', 'Time': 'Afternoon'}

print(student.popitem()) #('Time', 'Afternoon')
#NOTE---->PopItem is used to delete the last item of the dictionary

print(student.clear()) #None
print(student) #{}

#3. Built-in-Methods
#3.1 Accessing Data

student = {

"name": "Alice",
"age": 21,
"course": "Computer Science",
"duration":6,
"Fav":"Reading"

}
print(student.get("Fav")) #Reading
print(student.keys()) #dict_keys(['name', 'age', 'course', 'duration', 'Fav'])
print(student.values()) #dict_values(['Alice', 21, 'Computer Science', 6, 'Reading'])
print(student.items()) #dict_items([('name', 'Alice'), ('age', 21), ('course', 'Computer Science'), ('duration', 6), ('Fav', 'Reading')])

#3.2 Adding and Updating Data
print(student.update({"age":"25"})) #None
print(student) #{'name': 'Alice', 'age': '25', 'course': 'Computer Science', 'duration': 6, 'Fav': 'Reading'}Hyderabad
print(student.setdefault("city","Hyderabad"))
print(student) #{'name': 'Alice', 'age': '25', 'course': 'Computer Science', 'duration': 6, 'Fav': 'Reading', 'city': 'Hyderabad'}

#3.3 Removing Data
print(student.pop("age")) #25
print(student.popitem()) #('city', 'Hyderabad')
del student["Fav"]
print(student) #{'name': 'Alice', 'course': 'Computer Science', 'duration': 6}
# print(del student["name"]) NOTE---->Print Function should always allows a return value inside the function

#4 Built-in_function
print(len(student)) #3
print(max(student)) #name
print(sorted(student))