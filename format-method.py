# str.format() = optinal method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item + ";")
print("The {} jumped over the {};".format(animal, item))
print("The {} jumped over the {};".format(animal, item)) # POSITIONAL ARGUMENT
print("The {animal} jumped over the {item};".format(animal="goat", item="sun")) 

text = "The {} jumped over the {}"
print(text.format(animal,item))

# add padding
name = "Ana"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}, nice to meet you".format(name))
# left align
print("Hello, my name is {:<10}, nice to meet you".format(name))
# right align
print("Hello, my name is {:>10}, nice to meet you".format(name))
# center
print("Hello, my name is {:^10}, nice to meet you".format(name))

number = 3.14159
#
print("The number pi is {:.2f}".format(number))
print("The number big number is is {:,}".format(10000))
print("The number in binary is {:b}".format(10000))
print("The number in octal is {:o}".format(10000))
print("The number in number is {:X}".format(10000))
print("The number in scientific is {:E}".format(10000))