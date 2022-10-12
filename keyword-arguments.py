# keyword arguments = arguments proceeded by the identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional positional arguments
#                     Python knows the names of the arguments that our function recieves

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(first="Ana", middle="Peanut", last="Banana")