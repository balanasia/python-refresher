# **kwargs = parameter that willpack all arguments into a dicitonary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs[first] + " " + kwargs[middle] + " " + kwargs[last])
    print("Hello!", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title = "Bro", first="Ana", middle="Peanut", last="Banana")