
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Can't divide by zero silly")
    print(e)
except ValueError as e:
    print("Can only use numbers")
    print(e)
except Exception as e:
    print("Something went wrong :c")
    print(e)
else:
    print(result)
# finally:
#     print("This will always execute")