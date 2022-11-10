from tkinter import *

window = Tk()

def dragStart(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def dragMotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

label = Label(window, bg="pink", width=10, height=5)
label.place(x=0,y=0)

label.bind("<Button-1>", dragStart)
label.bind("<B1-Motion>", dragMotion)

label2 = Label(window, bg="purple", width=10, height=5)
label2.place(x=100,y=100)

label2.bind("<Button-1>", dragStart)
label2.bind("<B1-Motion>", dragMotion)

window.mainloop()