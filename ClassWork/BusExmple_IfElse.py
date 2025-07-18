seats={ 'L1':True,'L2':False,'L3':True,'L4':False,'U1':True,'U2':True,'U3':False
}
seatno=input("Enter the seat Number ").upper()
if seatno in seats:
    if seats[seatno]:
       print("Seat is Not Available, Please Book with the another Number")
    else:

        print("Seat is available book the Seat with this number") 
else:
    print("Enter the proper seat no")

   