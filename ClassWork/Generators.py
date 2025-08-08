#Generators
l=['reels100','reels200','reels300','reels400']
def display(l):
    for i in l:
        return i
print(display(l))
print(display(l))
print(display(l))
"""
reels100
reels100
reels100

Note-->Here is the problem is when u call the function many number of times also it returns only one value
we cannot access the data in parts we cannot it return only one value
and `fun can only have one single return statement
If we want return the multiple statements then we have to go for generators
"""
l=['reels100','reels200','reels300','reels400']
def display(l):
    for i in l:
        yield i

scroll=display(l)
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
reels100
reels200
reels300
'''

def count(n):
    i=1
    while i<n:
        yield i
        i+=1
numCount=count(5)
print(next(numCount))
print(next(numCount))
print(next(numCount))
print(next(numCount))
'''
1
2
3
4
'''
def squr(n):
    for i in range(n):
        yield i**2
num=squr(10)
for i in range(10):
    print(next(num))

'''
1
4
9
16
25
36
49
64
81
'''
# This is for many number of times of retrieval of post from the social media platform 

def fetch():
    post_id=1
    while True:
        yield f"Post{post_id}"
        post_id+=1
newPost=fetch()
print(next(newPost))
print(next(newPost))
print(next(newPost))
print(next(newPost))
print(next(newPost))
print(next(newPost))
'''
Post1
Post2
Post3
Post4
Post5
Post6
'''
