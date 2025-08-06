#Lambda Functions
#Square Number
sq=lambda n: n*n
print(sq(4)) #16

#Even
even=lambda n:"True"if n%2==0 else "False"
print(even(13)) #False

#Max Of 2Numbers
maxTwo=lambda a,b:a if a>b else b
print(maxTwo(234,654)) #654

#Muitiple Of Two Numbers
multiple=lambda a,b:a*b
print(multiple(10,6)) #60

#Sorting Of 2ndElement
l=[(1,2),(4,5),(10,1)]
print(sorted(l)) #[(1, 2), (4, 5), (10, 1)]
print(sorted(l,key=lambda i:i[1])) #[(10, 1), (1, 2), (4, 5)]

#Even Filter
l=[1,2,3,43,4,5,667,8]
even=list(filter(lambda i:i%2==0,l))
print(even) #[2, 4, 8]

#Square Element

sq=list(map(lambda i:i*i,l))
print(sq) #[1, 4, 9, 1849, 16, 25, 444889, 64]

names=['Afrin','sunitha','revathi']
upper=list(map(lambda i:i.upper(),names))
print(upper) #['AFRIN', 'SUNITHA', 'REVATHI']

#Sort List of Dictionaries



#return len of strin
length=lambda s:len(s)
print(length("Python"))


#startsWithVowel True otherwise false
vol="aeiouAEIOU"
check=lambda s: "True" if s[0] in vol else "False"
print(check("Afreen")) #True

