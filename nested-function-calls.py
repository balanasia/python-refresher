# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next function

print(round(abs(float(input("Enter a whole number: ")))))