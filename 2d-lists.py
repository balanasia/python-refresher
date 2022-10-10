drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
desert = ["cake", "icecream", "tiramisu"]

print("Hi, welcome to the meal generator.")

user_drink = int(input("Pick a number from 1 to 3 for your drink: ")) - 1
user_dinner = int(input("Pick a number from 1 to 3 for your dinner option: ")) - 1
user_desert = int(input("Pick a number from 1 to 3 for your desert: ")) - 1

user_meal = [drinks[user_drink], dinner[user_dinner], desert[user_desert]]

print("Here is your meal: ")
for i in user_meal:
    print(i)