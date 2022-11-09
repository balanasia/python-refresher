from tkinter import *
from tkinter import ttk

window = Tk()

# windget that manages collection of windows and displays
notebook = ttk.Notebook(window)

# new frame for tab 1 and 2
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")

# this will expand to fill any space otherwise used
# fill will fill space on x and y axes
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello! This is Tab 1", width=50, height=25).pack()
Label(tab2, text="Byeee! This is Tab 2", width=50, height=25).pack()

window.mainloop()