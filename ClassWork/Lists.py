# Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [10, "Python", 3.14, True]
print(numbers) #[1, 2, 3, 4, 5]
print(fruits) #['apple', 'banana', 'cherry']
print(mixed) #[10, 'Python', 3.14, True]
# print(list("Python","Programming"))
# 
#  #NOTE if we give the double values in the constructor then it will give as the error

#1.  Accessing Elements in a List
#1.1 Using Indexing
my_list = ["Python", "Java", "C++"]
print(my_list[0]) #Python
print(my_list[-1]) #C++
# print(my_list[4]) #IndexError

#1.2 Using Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) #[20, 30, 40]
print(numbers[:3]) # [10, 20, 30]
print(numbers[2:]) # [30, 40, 50]
print(numbers[-3:-1]) # [30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10]

#2 Modifying Lists
#2.1 Changing Elements
numbers = [10, 20, 30, 40]
numbers[2] = 100
print(numbers) # [10, 20, 100, 40]

#2.2 Adding Elements
numbers.append(50)
print(numbers) #[10, 20, 100, 40, 50]
numbers.insert(1, 15)
print(numbers) #[10, 15, 20, 100, 40, 50]
numbers.extend([60, 70, 80])
print(numbers) #[10, 15, 20, 100, 40, 50, 60, 70, 80]

#2.3 Removing Elements
numbers.remove(100)
print(numbers) #[10, 15, 20, 40, 50, 60, 70, 80]
print(numbers.pop(2)) #20

#3 List Methods
numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) # 2
print(numbers.index(4)) # 2
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers) # [9, 5, 4, 3, 1, 1]
numbers.append(123)
print(numbers) #[9, 5, 4, 3, 1, 1, 123]
numbers.sort(reverse=True)
print(numbers) #[123, 9, 5, 4, 3, 1, 1]
list2=numbers.copy()
print(list2)
print(max(numbers)) #123
print(min(numbers)) #1
print(sum(numbers)) #146
print(numbers) #[123, 9, 5, 4, 3, 1, 1]













