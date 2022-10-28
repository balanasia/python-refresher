from tkinter import *

count = 0
def click():
    global count
    count += 1
    print("MEOW MEOW MEEEOW", count, " times")

window = Tk()

photo = PhotoImage(file="cat.png")

button = Button(window,
                text="MEOW MEOW MEOW MEOW",
                command=click,
                font=("Papyrus", 30),
                fg="pink",
                bg="black",
                activeforeground="pink",
                activebackground="black",
                image=photo,
                compound="bottom")

button.pack()

window.mainloop()