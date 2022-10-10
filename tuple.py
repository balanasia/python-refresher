# tuple = collection which is ordered and unchangeable 
#         used to group togetehr related data

student = ("Hunter", "16", "male")
print(student.count("Hunter"))
print(student.index("16"))

for i in student:
    print(i)

if "Hunter" in student:
    print("How's that therapy going")