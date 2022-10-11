# index operator [] = gives access to a sequence's element (str,list,tulpes)
# 
name = "luz Noceda!"

# if(name[0].islower()):
#     name = name.capitalize()
#     print("Name has been capitalized: " + name)

first_name = name[0:3].upper()
last_name = name[4:-1].lower()
last_character = name[-1]

print(first_name + " " + last_name)
print(last_character)
