password=input("Enter Password")
valid=False
for i in password:
    if 6<=len(password)<=30:
        if password[0].isupper():
            if  " " not in password and "/" not in password and "-" not in password and "?" not in password:
                valid=True
print(valid)