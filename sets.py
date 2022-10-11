# set =  a collection that is unordered, unindexed
#        no duplicate values

utensils = {"fork", "spoon", "knife"}

# utensils.add("chopsticks")
# utensils.remove("fork")

# for x in utensils:
#     print(x)

# utensils.clear()

dishes = {"bowl", "plate", "cup", "knife"}
# utensils.update(dishes)
# for x in utensils:
#     print(x)

# dishes.update(utensils)
# for x in dishes:
#     print(x)

# dinnertable = utensils.union(dishes)
# for x in dinnertable:
#     print(x)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))
