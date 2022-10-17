import os

source = "text.txt"
destination = "/Users/anastasiiabalakhan/Downloads/text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print("Perhaps " + source + " was not found") 