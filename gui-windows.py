from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# instantiate an instance of window
window = Tk()
window.geometry("420x420")
window.title("MEOW MEOW MEOW MEOW")

icon = PhotoImage(file='cat.png')
window.iconphoto(True, icon)
window.config(background="pink")

# dispaly a window, listen to events
window.mainloop()

