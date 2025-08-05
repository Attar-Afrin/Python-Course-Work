n=int(input("Enter the no of Messeges"))
chat={}
for i in range(n):
    name,msg=input().split(':')
    if name in chat:
        chat[name].append((i,msg.strip()))
    else:

        chat[name]=(i,msg.strip())
print(chat)
while True:
    print("1.Count total number of messeges")
    print("2.Identifying unique users in the chat")
    print("0.Exit")
    ch=int(input("Enter the choice : "))
    if ch==0:
        break
    elif ch==1:
        print("Total no of messeges are ",n)
    elif ch==2:
        print()
    else:
        print("Invalid Choice")