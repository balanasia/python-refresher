from tkinter import *
from tkinter import filedialog

window = Tk()

def openFile():
    file_path = filedialog.askopenfilename(title="Open file baka!")
    file = open(file_path, 'r')
    print(file.read())
    file.close()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()