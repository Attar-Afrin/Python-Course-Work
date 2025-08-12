# 1 Add Two Numbers

num=list(map(int,input("Enter Two numbers").split()))
print(sum(num))
# Enter Two numbers10 20
# 30
 #2 Square Number
n=int(input("Enter Number to Square"))
sq=n*n
print(sq) #Enter Number to Square6
# 36

#3 Area of a circle
rad=int(input("Enter Radius"))
area=3.14*(rad**2)
print(area)

#Greet The User
name=input("Enter name")
print(f"Hello {name} Good Morning And Have a nice day")

#Convert From Celsius to fahrenheit
celsius=int(input("Enter Temperature in celsius: "))
Fahrenheit=celsius*9/5+32
print(Fahrenheit)

#Multiple Three Numbers
n,m,p=list(map(int,input("Enter Three numbers: ").split()))
print(n*m*p)  #Enter Three numbers: 6 2 4
# 48

#Calculate Simple intrest
p,t,r=tuple(map(int,input("Enter principal,Rate and Time").split()))
si=p*t*r/100
print(si)


# Find length Of String
strlen=input("Enter String :")
print(len(strlen))
#Enter String :hello
#5

# Append Element in a list
l=list(map(int,input().split()))
print(l)
print(l.append(7)) #None
print(l)



'''1 2 4
[1, 2, 4]
None
[1, 2, 4, 7]
'''



#doubling Each Element
def double(l):
    res=[]
    for i in range(len(l)):
        res.append(l[i]*2)
    return res
print(double([1,2,3]))
#[2, 4, 6]

#Sort a list
def listSort(l):
    print(l.sort())
    print(l)
listSort([5,2,9,1]) #[1, 2, 5, 9]


#Clear a list Inside Function
def lstClear(l):
    l.clear()
    print(l) 
lstClear([1,2,6,6]) #[]


#Update Dictionary value

def update(d):
    d[1]='apple'
    print(f"A for {d[1]}")
    print(d) #{1: 'apple'}
update({1:'a'}) #A for apple

#Remove Element from list

def valRem(l):
    l.remove(3)
    l.pop(0)
    l.pop(0) #[4, 5, 6, 7, 8]
    del l[0:2] #[6, 7, 8]
    del l[1] #[6, 8]
    print(l)
valRem([1,2,3,4,5,6,7,8]) #[1, 2, 4, 5, 6]




#Add key to Dict
def update_d(d):
    key=input("Enter Key")
    val=int(input("Enter Val"))
    d[key]=val
    print(d)
update_d({'afreen':1})

'''
Enter Keyharini
Enter Val2
{'afreen': 1, 'harini': 2}
'''
#Increment All Values in dict


def incr_dict(d):
    for key,val in d.items():
        d[key]+=1
    print(d)
incr_dict({'a':1,'b':2,'c':3}) #{'a': 2, 'b': 3, 'c': 4}

#17 Factorail Of Number

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
print(fact(3)) #6

#19 Sum of First natural Number
def NatSum(n):
    s=0
    for i in range(n+1):
        s=s+i
    return s
print(NatSum(10)) #55 n*(n+1)//2
   
#Power of Number Using Recursion
def PowNum(l):

    print(l[0]**l[1])
    
PowNum([2,3]) #8

def maximum(a,b,c):
    return max(a,b,c)
maxNum=maximum(22,45,12)
print(maxNum) #45

