#Reverse Number
n=123456789
while n>0:
    r=n%10
    print(r,end=" ")
    n//=10