num=int(input("Enter the Number : "))
isPrime=False
for i in range(2,num//2+1):
    if num%i==0:
        isPrime=True
        break
if not isPrime:
    print("Prime Number")
else:
    print("Not a Prime Number")        