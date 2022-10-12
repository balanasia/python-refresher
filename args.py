# *args = parameter that will pack all arguments into a tuple
#         useful so that the function can accept anything varying amount of args

#equivalent to *args, just have to have the *
def add(*stuff):
    sum = 0

    #tuples are unchangable
    #need to be converted to a diff collection, such as a list

    stuff = list(stuff)
    stuff[0] = 4

    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))