import random

while True:
    print("Welcome to the Rock Paper and Scissors!\n")

    choices = ['rock', 'paper', 'scissors']

    userPick = ""
    #print(userPick)

    # will make sure the user input the right input

    while userPick not in choices:
        userPick = input("Your move! \nRock, paper or scissors?: ")

    computerPick = random.choice(choices)
    print("Computer pick: " + computerPick)

    # draw
    if userPick == computerPick:
        print("It's a draw!")
    elif (userPick=="papper" and computerPick=="scissors") or (userPick=="rock" and computerPick=="paper") or (userPick=="scissors" and computerPick=="rock"):
        print("Computer wins!")
    elif (userPick=="paper" and computerPick=="rock") or (userPick=="rock" and computerPick=="scissors") or (userPick=="scissors" and computerPick=="paper"):
        print("Player wins!")
    else:
        print("Something went wrong")
    #print(computerPick)

    play_again = input("Play again? yes/no: ")
    if play_again != "yes":
        break

print("Bye! Have a good day!")