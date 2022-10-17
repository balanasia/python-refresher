# -------------------------#
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1;

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------#
def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1
    else: 
        print("Wrong :c")
        return 0

# -------------------------#
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your Score is: " + str(score) + "%")

# -------------------------#
def play_again():
    response = input("Do you want to play again? yes/no: ").upper()
    if response == "YES":
        return True
    else:
        return False


# dictionary
questions = {
    "Who created Python? ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy show?: ": "C",
    "Is the Earth round?: ": "A",
}

# 2D list
options = [
    ["A. A. Guido van Rossum", "B. Mark Zucc", "C. Elon Busk", "D. Gill Bates"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 1998"],
    ["A. Smosh", "B. Friends", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What is Earth?"]
]

new_game()
while play_again():
    new_game()

print("Byeeeeee!")