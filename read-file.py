try:
    with open("text.txt") as file:
        # automatically closes the file
        print(file.read())
except FileNotFoundError:
    print("That file was not found:(")