# str.format() = optinal method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item + ";")
print("The {} jumped over the {};".format(animal, item))
print("The {} jumped over the {};".format(animal, item)) # POSITIONAL ARGUMENT
print("The {animal} jumped over the {item};".format(animal="goat", item="sun")) 