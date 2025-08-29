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