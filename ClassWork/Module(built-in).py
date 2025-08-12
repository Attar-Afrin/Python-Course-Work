# System(sys)

import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print(sys.exit())

#Platform Module
import platform
print(platform.system()) #Windows

print(platform.release()) #11
print(platform.processor()) #Intel64 Family 6 Model 154 Stepping 4, GenuineIntel

#Math Module
import math
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.sqrt(100)) #10.0
print(math.pow(5,2)) #25.0
print(math.ceil(12.3)) #13
print(math.floor(12.99)) #12
print(abs(-13)) #13
print(math.fabs(-16)) #16.0
print(math.factorial(5)) #120
print(math.gcd(8,12)) #4

#GCD of Two Numbers
n1=int(input())
n2=int(input())
n=min(n1,n2)
for i in range(n,0,-1):
    if n1%i==0 and n2%i==0:
        print(i)              ###5
        break


#Factorail Of the Number
n=int(input())
fact=1
for i in range(n):
    fact*=i

print(fact)

import random
print(random.random()) #0.7402121000927757
print(random.randint(1,20)) #4
print(random.uniform(1,5)) #2.7802146343441625 Note--->Float random values
l=['afreen','keerthana','ramya','revathi']
print(random.choice(l))
print(random.choices(l,k=2))
print(l) #['afreen', 'keerthana', 'ramya', 'revathi']
random.shuffle(l)
print(l) #['afreen', 'ramya', 'keerthana', 'revathi']


from itertools import combinations, permutations
s="affu"
t=tuple(permutations(s,3))
print(t)
for i in t:
    print(''.join(i),end=",")

#aff,afu,aff,afu,auf,auf,faf,fau,ffa,ffu,fua,fuf,faf,fau,ffa,ffu,fua,fuf,uaf,uaf,ufa,uff,ufa,uff
s="rajjo"
r=tuple(combinations(s,2))
print(r)
for i in r:
    print(''.join(i),end=",")
#ra,rj,rj,ro,aj,aj,ao,jj,jo,jo,





