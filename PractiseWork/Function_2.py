#18 Fibonacci number
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=' ')
        a=b
        b=a+b
fibonacci(6)

#20 Reverse a string using Recursion
def string(text):
    print(text[-1])
   


#22 Sum of digits using Recursion


#25 maximun of 3 numbers using max
l=map(int,input("Enter Three Numbers ").split())
print(max(l)) #7

#26 Sort a list using Sorted
lst=list(map(int,input().split()))
print(sorted(lst)) #[0, 1, 3, 7, 9]


#27 Sum of elements using sum
nums=map(int,input().split())
print(sum(nums)) #4 5 6 7 ----->22


#28 Find Data Type using Type
a=10
b='hii'
c=10.3
lst=['bec']
st={2.3,4}
d={1:37,31:82}
print(type(a))
print(type(b))
print(type(c))
print(type(lst))
print(type(st))
print(type(d))
'''
<class 'int'>
<class 'str'>
<class 'float'>
<class 'list'>
<class 'set'>
<class 'dict'>
'''

#29 print Even Numbers upto N
n=int(input("Enter number "))
for i in range(n+1):
    if i%2==0:
        print(i,end=" ")

#30 return list of squares
def lstSq(l):
    res=[]
    for i in range(1,len(l)+1):
        res.append(i**2)
    return res
l=list(map(int,input("Enter List of numbers ").split()))
print(lstSq(l)) #Enter List of numbers 1 2 3
                 #[1, 4, 9]

#31 check if number is prime or not
def prime_checking(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "True"
    else:
        return "False"
n=int(input())
print(prime_checking(n)) #7----->True

#32 Count vowels in a string
vow="aeiouAEIOU"
text=input("Enter String")
c=0
for i in text:
    if i in vow:
        c+=1
print(c)    #education--->5

#33 multiply by 2 using lambda

