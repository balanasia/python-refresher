from tkinter import *

old_window = Tk()

def createWindow():
    # create new top level window connected to the bottom window
    new_window = Toplevel()

    #new independent window
    # new_window = Tk()

    # close outof the old window
    old_window.destroy()

Button(old_window, text="Create new window", function=createWindow).pack()

old_window.mainloop()