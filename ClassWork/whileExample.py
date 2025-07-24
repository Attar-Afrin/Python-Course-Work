moves=40
winningpoint=int(input("Enter the winning point"))
while moves>0:
    if moves==winningpoint:
        print("Congrats ! You have won the game")
        break
    print(f"{moves} left !You can play")
    moves-=1
else:
    print("Game Over") #Enter the winning point35
# 40 left !You can play
#39 left !You can play
#38 left !You can play
#37 left !You can play
#36 left !You can play
#Congrats ! You have won the game


# Sum of the Numbers
n=int(input("Enter the Number : "))
s=0
while(n>0):
    s+=(n%10)
    n//=10
print(s)


