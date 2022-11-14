from tkinter import *

def moveUp(event):
    canvas.move(myImage, 0, -10)

def moveLeft(event):
    canvas.move(myImage, -10, 0)

def moveRight(event):
    canvas.move(myImage, 10, 0)

def moveDown(event):
    canvas.move(myImage, 0, 10)

window = Tk()
window.bind("<w>", moveUp)
window.bind("<a>", moveLeft)
window.bind("<s>", moveDown)
window.bind("<d>", moveRight)

# arrow keys
window.bind("<Up>", moveUp)
window.bind("<Left>", moveLeft)
window.bind("<Down>", moveDown)
window.bind("<Right>", moveRight)
canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="neko-arc.png")
myImage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()