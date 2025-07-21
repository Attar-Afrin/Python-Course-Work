seats={
    "U1":{'price':1029,'booking_status':True},
    "U2":{'price':1359,'booking_status':False},
    "M1":{'price':1879,'booking_status':True},
    "M2":{'price':2233,'booking_status':False},
    "L1":{'price':1275,'booking_status':False}
}
for i in seats:
    if seats[i]['booking_status']:
        print(f'***{i}***')
    else:
        print(f'{i}-seats[i]["price]') 

seatno=input("Enter the SeatNo").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print("Sorry! Seat is Already Booked")
    else:
        name=input("Enter the name")
        age=int(input("Enter the age"))  
        gender=input("Enter the gender(F/M)").upper()
        if age<=5:
            print(f'Hello {name} Your seat booked successfully with free of cost')
        elif age<=14:
            print(f'Hello {name} Your Seat is booked successfullt with half cost')
        else:
            print(f'Hello {name} you seat is booked succesfully.Pay the Payment of {seats[seatno]['price']}')     