from tkinter import *
from tkinter import filedialog

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

window  = Tk()
button = Button(text="Save", command=saveFile)
button.pack()

text = Text()
text.pack()

window.mainloop()