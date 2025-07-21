#1 Creation of the Tuples using () and tuple() constructor
tuple1=(1,3,4,5,6)
print(tuple1) #(1, 3, 4, 5, 6)

tuple2=tuple((12,32,545,66,77,2))
print(tuple2) #(12, 32, 545, 66, 77, 2)

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
print(tuple1+23)