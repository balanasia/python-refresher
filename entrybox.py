from tkinter import *

window = Tk()

entry = Entry(window,
                font=('Papyrus', 50),
                fg='orange',
                bg='black',
                show="*")
# entry.insert(0, "Bone")
entry.pack(side='left')

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side='right')

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side='right')

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side='right')

window.mainloop()