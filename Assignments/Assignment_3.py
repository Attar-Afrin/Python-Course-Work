def quiz(n):
    global ans_count
    if n==1:
        ans="b"
        print(f"Question 1. What is the correct file extension for Python files?")
        print(f"a)  .jpg")
        print(f"b)  .py")
        print(f"c)  .java")
        print(f"d)  .pi")
        print("Your Answer  (a/b/c/d)",end=" ")
        ch=input().lower()
        if ch==ans:
            print("Yes Correct")
            ans_count+=1
        else:
            print("No")
            ans_count-=1   
    return ans_count 

        
         
n=1
global ans_count
ans_count=0
wrg_count=0
print("Welcome to the Python Quiz Game Organized By Afreen")
res=[]
while n<10:
    i=quiz(n)
    res.append(i)
    n+=1
print(f"Your Final Score : {ans_count}/10")
print("Great job! Keep Practicing!")

