from cgi import test
import os

path = "/Users/anastasiiabalakhan/Desktop/test"

if os.path.exists(path):
    print("That locaiton exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("That location doesn't exist")
