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
* * * *
* * * * *
* * * * * *
'''

n=int(input("Enter n value"))
for row in range(n):
    for col in range(row):
        print("*",end=" ")
    print()

'''
* * * * * * 
* * * * *
* * * *
* * *
* *
*
'''

n=int(input("Enter n value"))
for row in range(n):
    for col in range(n-row):
        print("*",end=" ")
    print()

n=int(input("Enter n value"))
for row in range(n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col in range(row):
        print("*",end=" ")
    print()
'''
* * * * * * * 
  * * * * * *
    * * * * *
      * * * *
        * * *
          * *
            *
'''

n=int(input("Enter n value"))
for row in range(n):
    for col in range(row):
        print(" ",end=" ")
    for col in range(n-row):
        print("*",end=" ")
    print()

'''
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''

n=int(input("Enter n value"))
for row in range(n):
    if row<=n//2:
    
        for col in range(row+1):
            print("*",end=" ")
    else:

        for col2 in range(n-row):

            print("*",end=" ")
    print()

'''
* * * * * * * 
*           *
*           *
*           *
*           *
*           *
* * * * * * *
'''

n=int(input("Enter n value for square pattern"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=" ")
        else:

            print(" ",end=" ")
    print()

'''
* * * * * * * 
*           *
*           *
* * * * * * *
*           *
*           *
* * * * * * *
'''
n=int(input("Enter n value for square pattern"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:

            print(" ",end=" ")
    print()

'''
* * * * * * * * 
            *
          *
        *
      *
    *
  *
* * * * * * * *
'''
n=int(input("Enter n value for z---pattern"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1:
            print("*",end=" ")
        else:

            print(" ",end=" ")
    print()

'''
* * * * * * * * * 
  *           *
    *       *
      *   *
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''

n=int(input("Enter n value for z---pattern"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1 or row==col:
            print("*",end=" ")
        else:

            print(" ",end=" ")
    print()










