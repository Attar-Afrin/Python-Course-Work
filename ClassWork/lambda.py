#Lambda
#Syntax--->fun name=lambda parameters
#sumof three numbers
sumofthree=lambda a,b,c:a+b+c
print(sumofthree(12,13,14)) #39

#even oddchecking
evenOdd=lambda n:"Even" if n%2==0 else "Odd"
print(evenOdd(100))#Even

#Lambda Examples
sumn=lambda n:n+10
print(sumn(10)) #10

cube=lambda n:n**3
print(cube(20)) #8000

s=lambda s:s[0]
print(s("Python")) #P

#Greater

greater=lambda a,b:a if a>b else b
print(greater(123,3465)) #3465

# Map()  filter()   reduce()

#Map()
s='python programming'
changestr=list(map(lambda i:i.upper(),s))
print(changestr) #['P', 'Y', 'T', 'H', 'O', 'N', ' ', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G']     

assccii=tuple(map(lambda i:ord(i),s))
print(assccii) #(112, 121, 116, 104, 111, 110, 32, 112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103)       
 
 #Ascii value for the space is 32

t=(20,40,30,50,12,34,24,89)
tup=tuple(map(lambda i:i//10 , t))
print(tup)
#(2, 4, 3, 5, 1, 3, 2, 8)


vol="aeiouAEIOU"
frmt=list(map(lambda i: "*" if i in vol else "0",s))
print(frmt) #['0', '0', '0', '0', '*', '0', '0', '0', '0', '*', '0', '0', '*', '0', '0', '*', '0', '0']     

#Filter()
l=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda i:i%2==0,l))
print(even) #[2, 4, 6, 8, 10]

oddl=list(filter(lambda i:i%2==1,l))
print(oddl) #[1, 3, 5, 7, 9]

products={'mouse':10,'keyboard':0,'laptops':30,'phone':0,'charger':13}
result=list(filter(lambda i:products[i]>0,products))
print(result)
#['mouse', 'laptops', 'charger']

#reduce()
from functools import reduce
l=[1,2,3,4]
sum1=reduce(lambda a,i:a+i,l)
print(sum1) #10

s={'python','html','css','java','mysql'}
names=reduce(lambda n,name:n +' '+name,s)
print(names)
#css python java mysql html

t=(1,2,3,4,5)
product=reduce(lambda pro,item:pro*item,t)
print(product) #120







