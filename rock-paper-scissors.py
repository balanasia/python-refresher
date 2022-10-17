import random

def welcomeMessage():
    print("Welcome to the Rock Paper and Scissors!\n")

userPick = input("Your move! \nEnter 'r' for rock, 'p' for paper and 's' for scissors: ")
#print(userPick)

# will make sure the user input the right input
while (userPick == "") or (userPick != "r" or userPick != "p" or userPick != "s"):
    if (userPick == "r" or userPick == "p" or userPick == "s"):
        break
    else: 
        userPick = input("Invalid input. Enter 'r' for rock, 'p' for paper and 's' for scissors: ")

myList = ['rock', 'paper', 'scissors']
computerPick = random.choice(myList)
print("Computer pick: " + computerPick)

# draw
if (userPick=="p" and computerPick=="paper") or (userPick=="r" and computerPick=="rock") or (userPick=="s" and computerPick=="scissors"):
    print("It's a draw!")
elif (userPick=="p" and computerPick=="scissors") or (userPick=="r" and computerPick=="paper") or (userPick=="s" and computerPick=="rock"):
    print("Computer wins!")
elif (userPick=="p" and computerPick=="rock") or (userPick=="r" and computerPick=="scissors") or (userPick=="s" and computerPick=="paper"):
    print("Player wins!")
else:
    print("Something went wrong")
#print(computerPick)

