def quiz(n):
    global ans_count
    global ch
    if n==1:
        ans="b"
        print(f"Question 1. What is the correct file extension for Python files?")
        print(f"a)  .jpg")
        print(f"b)  .py")
        print(f"c)  .java")
        print(f"d)  .pi")
        print("Your Answer  (a/b/c/d)",end=" ")
        ch=input().lower()
        if ans==ch:
            print("Yes Correct")
            ans_count+=1
        else:
            print("No")
            ans_count-=1   
    if n==2:
        ans="b"
        print(f"2. Which keyword is used to define a function in Python?")
        print("a)  define")
        print("b)  def")
        print("c)  function")
        print("d)  fun")
        print("Your Answer  (a/b/c/d)",end=" ")
        ch=input().lower()
        if ch==ans:
            print("Yes Correct")
            ans_count+=1
        else:
            print("No")
            ans_count-=1   
    if n==3:
        ans="b"
        print(f"3. Which of the following is a correct variable name?\na)  1value\nb)  value1\nc)  @value\nd)  value-1")
        print("Your Answer  (a/b/c/d)",end=" ")
        ch=input().lower()
        if ch==ans:
            print("Yes Correct")
            ans_count+=1
        else:
            print("No")
            ans_count-=1   
    if n==4:
        ans="c"
        print("4. Which of the following is a tuple?\na)  [1, 2, 3]\nb)  {1, 2, 3]\nc)  (1, 2, 3)\nd)  <1, 2, 3>")
        print("Your Answer  (a/b/c/d)",end=" ")
        ch=input().lower()
        if ch==ans:
            print("Yes Correct")
            ans_count+=1
        else:
            print("No")
            ans_count-=1 
    if n==5:
        ans="c"
        print("5. Which function is used to get input from the user in Python?\na)  get()\nb)  scan()\nc)  input()\nd)  read()")
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
while n<=5:
    quiz(n)
    n+=1
print(f"Your Final Score : {ans_count}/10")
print("Great job! Keep Practicing!")

