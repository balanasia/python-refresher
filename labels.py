from tkinter import *
from playsound import playsound

window = Tk()
window.geometry("420x420")
window.title("MEOW MEOW MEOW MEOW")
photo = PhotoImage(file='neko-arc.png')

label = Label(window, 
                text="MEOW MEOW MEOW MEOW MEOW", 
                font=('Bradley Hand', 40, 'bold'), 
                fg='pink', 
                bg='black',
                relief='raised',
                bd=10,
                padx=20,
                pady=20,
                image=photo
                )

# display text in the center of the window
label.pack()

# # specify where does the text live
# label.place(x=0, y=0)

window.mainloop()