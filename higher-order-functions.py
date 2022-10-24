# Higher Order Funcitons = a function either:
#                          1. accepts the function as an argument
#                                or
#                          2. returns a function
#                          (in python functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def divident(y):
        return y/x
    return divident

divide = divisor(2)
print(divide(10))

