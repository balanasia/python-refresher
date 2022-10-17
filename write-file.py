text = "Yo, whats up, BIIAAATCH\n Yo mister White\n"
text2 = "See ya"

with open('text.txt', 'w') as file:
    file.write(text)

with open('text.txt', 'a') as file:
    file.write(text2)