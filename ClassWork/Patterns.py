'''Enter n value 6
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 

'''
n=int(input("Enter n value"))
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()  

'''
Enter n value5
0 0 0 0 0 
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''
n=int(input("Enter n value"))
for row in range(n):
    for col in range(n):
        print(row,end=" ")
    print()  


'''
Enter n value6
0 1 2 3 4 5 
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
0 1 2 3 4 5
'''

n=int(input("Enter n value"))
for row in range(n):
    for col in range(n):
        print(col,end=" ")
    print()

'''
*
* *
* * *
'''

n=int(input("Enter n value"))
for row in range(n):
    for col in range(row):
        print("*",end=" ")
    print()

