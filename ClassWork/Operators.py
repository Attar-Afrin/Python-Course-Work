#1 ArithmaticOperators
a=10
b=20
print("Addition of (a+b)",a+b) #Addition of (a+b) 30
print("Subtraction of (a-b)",a-b) #Subtraction of (a-b) -10
print("Multiplication of(a*b)",a*b) #Multiplication of(a*b) 200
print("Division of (a/b)",a/b) #Division of (a/b) 0.5
print("Floor Division of(a//b)",a//b) #Floor Division of(a//b) 0
print("Modulus of(a % b)",a %b) #Modulus of(a % b) 10


#2 Comparison Operators
x=20
y=15
print("Equal to",x==y) #Equal to False
print("Not Equal to",x!=y) #Not Equal to True
print("Greater than",x>y) #Greater than True
print("Less than",x<y) #Less than False
print("Greater than or Equal to",x>=y) #Greater than or Equal to True
print("Less than or Equal to",x<=y) #Less than or Equal to False

#3 Assignment Operators
x=50
x+=5
print("Add & Assign",x) #Add & Assign 55
x-=10
print("Subtract & Assign ",x) #Subtract & Assign  45
x*=5
print("Multiply & Assign",x) #Multiply & Assign 225
x/=2
print("Divide & Assign",x) #Divide & Assign 112.5
x//=2
print("Floor Divide & Assign",x) #Floor Divide & Assign 56.0
x%=5
print("Modulus & Assign",x) #Modulus & Assign 1.0
x**10
print("Exponentiate & Assign",x) #Exponentiate & Assign 1.0


#4 Logical Operators
# AND Operator
print(True and True) #True
print(not True) #False
print(True or False) #True
x=10 
y=20
print(x > 5 and y < 30) #True
print(x > 15 or y < 30) #True
print(not (x > 5)) #False 
print(True | False) #Bitwise Or Opeartor #True
print(True & True) #Bitwise And Opeartor
print(~ True) # -2 #Bitwise Not


#5 Membership operator
# in not in
places=["Nandyal", "Hyderabad", "Kurnool", "Banglore"]
print("Nandyal" in places) #True
print("Ameerper" not in places) #True
print("Hyderabad" not in places) #False

name="Attar Afrin"
print(" " in name) # True
print("AA" in name) #False
print("A " in name) #False

#Bitwise Operators
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) #1 
print(x | y) #7 
print(x ^ y) #6
print(~x) #-6 
print(x << 1) #10 
print(x >> 1) #2 