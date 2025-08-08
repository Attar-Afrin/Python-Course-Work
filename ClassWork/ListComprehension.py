even=[]


l=[2,3,4,1,6,7,8,9]
res=[]
for i in l:
    if i%2==0:
        res.append("Even")
    else:
        res.append("Odd")
ures=["Even" if i%2==0 else "Odd" for i in l]
print(res,ures)

l=[[1,2],[3,4],[5,6],[7,8]]
res=[]
for i in l:
    res.append(sum(i))
    
    print(i)

    
