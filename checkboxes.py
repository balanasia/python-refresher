from tkinter import *

window = Tk()
x = BooleanVar()

neco_arc = PhotoImage(file="neko-arc.png")

def display():
    if (x.get()):
        print("You agwee ^_^")
    else:
        print("You don't agwee :c")

check_button = Checkbutton(window, 
                            text="I agwee", 
                            variable=x,
                            onvalue = True,
                            offvalue = False,
                            command = display,
                            font=("Papyrus", 50),
                            fg = 'pink',
                            bg='black',
                            activebackground='black',
                            activeforeground='pink',
                            padx=25,
                            pady=10,
                            image = neco_arc,
                            compound = 'left')
check_button.pack()

window.mainloop()