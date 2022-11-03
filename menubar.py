from tkinter import *
from tkinter import filedialog

window = Tk()

openImage = PhotoImage(file="neko-arc.png")

def openFile():
    file_path = filedialog.askopenfilename(title="Open file baka!")
    file = open(file_path, 'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', 
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML", ".html"),
                                        ("All files", ".*")])
    
    if file is None:
        return

    fileText = text.get(1.0, END)
#    write in a console window
#    filetext = input("Enter some text UwU")
    file.write(fileText)
    file.close()

def cut():
    pass

def copy():
    pass

def paste():
    pass

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Papyrus", 20))
menubar.add_cascade(label = "File", menu=fileMenu)

fileMenu.add_command(label="MEOW", command=openFile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile)
# separator
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

text = Text()
text.pack()

#edit 
fileMenu = Menu(menubar, tearoff=0, font=("Papyrus", 20))
menubar.add_cascade(label = "Edit", menu=fileMenu)

fileMenu.add_command(label="Cut", command=cut)
fileMenu.add_command(label="Copy", command=copy)
fileMenu.add_command(label="Paste", command=paste)


window.mainloop()