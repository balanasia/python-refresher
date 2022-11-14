from tkinter import *

def moveUp(event):
    label.place(x=label.winfo_x(), y = label.winfo_y()-10)

def moveLeft(event):
    label.place(x=label.winfo_x()-10, y = label.winfo_y())

def moveRight(event):
    label.place(x=label.winfo_x()+10, y = label.winfo_y())

def moveDown(event):
    label.place(x=label.winfo_x(), y = label.winfo_y()+10)

window = Tk()
window.geometry("500x500")

window.bind("<w>", moveUp)
window.bind("<a>", moveLeft)
window.bind("<s>", moveDown)
window.bind("<d>", moveRight)

# arrow keys
window.bind("<Up>", moveUp)
window.bind("<Left>", moveLeft)
window.bind("<Down>", moveDown)
window.bind("<Right>", moveRight)

myimage = PhotoImage(file="neko-arc.png")
label = Label(window, image = myimage)
label.place(x=0,y=0)

window.mainloop()