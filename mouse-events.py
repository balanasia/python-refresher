from tkinter import *

window = Tk()

def doSomething(event):
    print("Mouse Coordinates: " + str(event.x))

# left mouse click
# window.bind("<Button-1>", doSomething) 
# # scroll wheel click
# window.bind("<Button-2>", doSomething) 
# # right mouse click
# window.bind("<Button-3>", doSomething) 

# window.bind("<ButtonRelease>", doSomething) 
# enter the window
# window.bind("<Enter>", doSomething) 
# # leave the window
# window.bind("<Leave", doSomething) 

# tells the coordinate of where the mouse moves
window.bind("<Motion>", doSomething) 

window.mainloop()