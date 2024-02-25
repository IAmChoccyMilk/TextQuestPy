from tkinter import *
from tkinter import ttk
import Game.engine

# Creates a root window
root = Tk()

#Sets the title of the root window
root.title("TextQuestPy")
root.configure(bg = "black")

# Sets the window size
root.geometry("1920x1080")

txtBoxFrame = ttk.Frame(root, padding=10)
txtBoxFrame.grid()
welcomeLabel = ttk.Label (txtBoxFrame, text = "Welcome to Slavaria!").grid(column = 0, row = 0)
txtBox = Entry(txtBoxFrame, width = 10, background = "white")


# Keeps window open in the main loop.
root.mainloop()
