from tkinter import *
from tkinter import ttk

# Create the window
root = Tk()
root.title("Death Counter")

message = Label(
    text="How many times have you died?",
    width=30,
    height=1
)

deathInput = Entry(
    width=30
)

submitButt = Button(
    text="Calculate",
    bg="blue",
    fg="white"
)

message.pack()
deathInput.pack()
submitButt.pack()

root.mainloop()
