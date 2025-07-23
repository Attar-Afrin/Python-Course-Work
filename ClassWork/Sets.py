#1. Creation of Sets
my_set = {1, 2, 3, 4}
print(my_set)

#2. Operations on Sets
#a. Membership
print(3 in my_set) #True
print(6 not in my_set) #True

#b. Union Method
set1={1,2,4,56,7}
set2={9,8,7,6,5}
print(set1|set2) #{1, 2, 4, 5, 6, 7, 8, 9, 56}
print(set1.union(set2)) #{1, 2, 4, 5, 6, 7, 8, 9, 56}

#c. Intersection (& or intersection() method)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2
print(result) #{3}



