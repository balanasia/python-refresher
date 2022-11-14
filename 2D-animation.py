from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

photoimage = PhotoImage(file="neko-arc.png")
myImage = canvas.create_image(0,0,image=photoimage,anchor=NW)

# will run until the window is open
while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)
    window.update()
    time(0.01)

window.mainloop()