# scope = the region that a variable is recognized
#         A varialble is only available from inside the region is created
#         A global and locally scoped versions of the available can be created

name = "Ana"

def display_name():
    #local var
    name = "Banana"
    print(name)

display_name()
print(name)
