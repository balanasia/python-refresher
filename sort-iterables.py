# sort() method   = used with lists
# sort() funciton = used with iterables

# SORT LIST
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Crabs"]
# students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Crabs")

students_tuple = [("Squidward", "F", 60), 
                  ("Sandy", "A", 33), 
                  ("Patrick", "D", 36), 
                  ("Spongebob", "B", 20), 
                  ("Mr. Crabs", "C", 78)]


students_tuples = (("Squidward", "F", 60), 
                  ("Sandy", "A", 33), 
                  ("Patrick", "D", 36), 
                  ("Spongebob", "B", 20), 
                  ("Mr. Crabs", "C", 78))

# # sort list in alphabetical order
# students.sort(reverse=True)
# #sort a tuple
# sorted_students = sorted(students_tuple, reverse=True)

# for i in sorted_students:
#     print(i)

print("--------")
print("Sort by grade: ")
grade = lambda grades:grades[1]
students_tuple.sort(key=grade, reverse=True)
for i in students_tuple:
    print(i)

print("--------")
print("Sort by age: ")
# sort by age
age = lambda ages:ages[2]
students_tuple.sort(key=age)
for j in students_tuple:
    print(j)

print("--------")
print("Sorted tuple of tuples: ")
sorted_tuple = sorted(students_tuples)
for k in sorted_tuple:
    print(k)