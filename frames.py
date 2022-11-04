from tkinter import *

window = Tk()

frame = Frame(window, bg='pink', bd=5, relief=SUNKEN)
frame.pack(side=BOTTOM)

Button(frame, text="w", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text="a", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="s", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="d", font=("Consolas", 25), width=3).pack(side=LEFT)



window.mainloop()