# Loop Control statements

# break = terminate loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter You Name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if(i== "-"):
        continue
    print(i, end="")

for i in range(1, 21):

    if i == 13:
        pass
    else:
        print(i)