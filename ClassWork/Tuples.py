#1 Creation of the Tuples using () and tuple() constructor
tuple1=(1,3,4,5,6)
print(tuple1) #(1, 3, 4, 5, 6)

tuple2=tuple((12,32,545,66,77,2))
print(tuple2) #(12, 32, 545, 66, 77, 2)

numbers=1,2,3,4
print(numbers)
num=1,3,44,55,66,"Apple","Bag",4.5
print(num) #(1, 3, 44, 55, 66, 'Apple', 'Bag', 4.5)

#2. Accessing Tuple Elements
print(tuple2[2]) #545
print(tuple2[-1]) #2
#  print(tuple2[45]) #IndexError

#3 Slicing
print(tuple2[1:]) #(32, 545, 66, 77, 2)
print(tuple2[:]) #(12, 32, 545, 66, 77, 2)
print(tuple2[::-1]) #(2, 77, 66, 545, 32, 12)

#4 Operations On Tuples
# 4.1 Concatination
print(tuple1+tuple2) #(1, 3, 4, 5, 6, 12, 32, 545, 66, 77, 2)
 # print(tuple1+23) 
 #NOTE--->We can add tghe two tuples but we cannot add the element explicitely into the tuples

 #4.2 Repetition
my_tuple=(1,2,3)
print(my_tuple*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)
print((11,22,33,44) *2) #(11, 22, 33, 44, 11, 22, 33, 44)

#4.3 Membership
print(2 in my_tuple) #True
print(22 not in my_tuple) #True

#4.4 Tuple Unpacking
my_tuple=(1,3,5,7,9)
a,s,d,f,g=my_tuple
print(a,s,d) #1 3 5 NOTE---->To unpack the tuples from brackets to normal numbers then output will be without brackets by using variables

#5 Tuple Methods
print(my_tuple.count(2)) #0
print(my_tuple.count(3)) #1
print(my_tuple.index(5)) #2
# NOTE---->to get index of the element inedx function is used to get the element using index used by[]

#6 Built-in-Functions
print(len(my_tuple)) #5
print(max(my_tuple)) #9
print(min(my_tuple)) #1
print(sum(my_tuple)) #25
print(list(my_tuple)) #[1, 3, 5, 7, 9]
# print(my_tuple[0]=10)#----->SyntaxError

#7 Nested Lists
nested_tuple=(1,[2,3,4])
nested_tuple[1][0]=100
print(nested_tuple) #(1, [100, 3, 4])
nested_tuple[1][1]=200
print(nested_tuple) #(1, [100, 200, 4])

