# function = a block of code that is executed only when its called

name = input("What's your name?: ")
fave_animal = input("What's your favorite animal?: ")
math_question = input("WHAT'S 2+2?: ")

def hello(name, animal, math_question):
    print("Hello " + name + " c:")
    print("Your fave animal is " + animal)

    if (math_question != "4"):
        print("Your math aint mathing, you said that 2+2 is " + str(math_question))
    else:
        print("Have a blessed day!")

hello(name, fave_animal, math_question)