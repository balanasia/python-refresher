# zip(*iterables) = aggregate elements from two or more iterables(list, tuples, sets etc)
#                   creates a zip object paired with elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ["password", "abc123", "guest"]
login_date = ["1.1.2021", "1.2.2021", "1.3.2021"]

# users = dict(zip(usernames, passwords,))

# for key,value in users.items():
#     print(key + " : " + value)

users = zip(usernames, passwords, login_date)
for i in users:
    print(i)