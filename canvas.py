from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# pink_line = canvas.create_line(0,0,500, 500, fill="pink", width=5)
# blue_line = canvas.create_line(0,500,500, 0, fill="purple", width=5)
# canvas.create_rectangle(50, 50, 250, 250, outline="red")
# points =  [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(points, fill="yellow")
# canvas.create_arc(0,0,500,500, fill = "green", style="pieslice", start=180, extent=180)

# pokeball

canvas.create_arc(0, 0, 500, 500, fill="red", extent = 180, width=10, outline="black")
canvas.create_arc(0, 0, 500, 500, fill="white", extent = 180, start=180, width=10, outline="black")
canvas.create_oval(190, 190, 310, 310, fill = "white", width=10, outline="black")

canvas.pack()

window.mainloop()