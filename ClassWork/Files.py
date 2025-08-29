try:
    file=open('Sets.py','r+')
except FileNotFoundError:
    print("File is not present")
else:
    print(f"File is opened{file.read()}")
    file.seek(0)
    print(f"File is read only first value{file.readline()}")
    file.seek(0)
    print(f"To read all the content in list form {file.readable()}")
    file.close()
#NOTE---->r is only for read but r+ is read and append

try:
    file=open('Sets.py','r+')
except FileNotFoundError:
    print("File is not present")
else:
    print(f"File is opened{file.read()}")
    file.seek(0)
    print(f"File is read only first value{file.readline()}")
    file.seek(0)
    print(f"To read all the content in list form {file.readable()}")
    file.write("Saikumar\nAkash\nAdarsh")
    file.seek()
    print(file.read())

    file.close()

#Without close of file close method we have the way is with using
try:
    with open('Sets.py','r+') as file:

        print(f"File is opened{file.read()}")
        file.seek(0)
        print(f"File is read only first value{file.readline()}")
        file.seek(0)
        print(f"To read all the content in list form {file.readable()}")
        file.write("Saikumar\nAkash\nAdarsh")
        file.seek()
        print(file.read())

        file.close()
except FileNotFoundError:
    print("File is not present")