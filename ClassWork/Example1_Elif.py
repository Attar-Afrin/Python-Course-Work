hr,min=list(map(int,input("Enter Time").split(" ")))
if hr>=0 and hr<=24 and min>=0 and min<=60:
    if hr>=0 and hr<4:
        print("It's high time Just Go to sleep")
    elif hr>=4 and hr<12:
        print("Good Morning And have a nice day")
    elif hr>=12 and hr<16:
        print("Good Afternoon And Have a Healthy Lunch")
    elif hr>=16 and hr<19:
        print("Good Evening And Have a Tasty Snack")
    elif hr>=19 and hr<24:
        print("Good Night And have a peac Sleep")

else:
    print("Invalid Input")