from tkinter import *
import time

WIDTH = 1000
HEIGHT = 1000

# image speed on x and y axis
xVelocity = 4
yVelocity = 6

window = Tk()

canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

bgimage = PhotoImage(file="grass.png", width=WIDTH, height = HEIGHT)
myBGimage = canvas.create_image(0,0,image=bgimage,anchor=NW)

photoimage = PhotoImage(file="neko-arc.png")
myImage = canvas.create_image(0,0,image=photoimage,anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()

# will run until the window is open
while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)

    # check if the image is at the end of the window
    # and bounce it back
    if(coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity

    if(coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity    

    canvas.move(myImage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()