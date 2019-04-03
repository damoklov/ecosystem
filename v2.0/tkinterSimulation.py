from tkinter import *
from simulation import string_placement


window = Tk()
window.title("ECOSYSTEM 1.0")
lbl = Label(window,
            text="GREETINGS IN ECOSYSTEM 1.0!\nPress <Start simulation>\n",
            fg="Black",
            font=("Helvetica", 15))
lbl.place(x=50, y=50)
window.geometry('900x600')


def clicked():
    """Checks if button was clicked"""
    lbl.configure(text=string_placement())
    lbl.update()


btn = Button(window, text="Start simulation", command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
