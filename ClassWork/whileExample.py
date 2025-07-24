moves=40
winningpoint=int(input("Enter the winning point"))
while moves>0:
    if moves==winningpoint:
        print("Congrats ! You have won the game")
        break
    print(f"{moves} left !You can play")
    moves-=1
else:
    print("Game Over")