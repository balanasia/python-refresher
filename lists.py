# list = stores multiple items in a single variable

food = ["pizza", "HAMBORGER", "coolcat", "SPAGETT"]
print(food)
print(food[2])

food[0] = "sushi"

for i in food:
    print(i)

food.append("icecream")
print(food)

food.remove("coolcat")
print(food)

food.pop()
print(food)

food.insert(1, "CAKE")
print(food)

food.sort()
print(food)

food.clear()
print(food)
