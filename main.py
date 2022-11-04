from tkinter import *
from tkinter import ttk

# Create the window
root = Tk()
root.title("Death Counter")


def start():
    Label(
        text="Welcome to the Death Counter!\nClick the button to start counting!",
        justify=CENTER,
        font=("Times New Roman", 12),
        fg="white",
        bg="black",
        height=10,
        width=30
    ).pack()

    Button(
        text="Start",
        font=("Times New Roman", 12),
        fg="white",
        bg="black",
        width=29,
        command="mainScreen"
    ).pack()


def mainScreen():
    Button().destroy()


def config():
    startMsg = Label(
        text="Welcome to the Death Counter!\nClick the button to start counting!",
        justify=CENTER,
        font=("Times New Roman", 12),
        fg="white",
        bg="black",
        height=10,
        width=30
    )


def add():
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


start()
root.mainloop()
