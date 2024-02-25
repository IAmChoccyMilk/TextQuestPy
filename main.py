from tkinter import *
import Game.engine

# Creates a root window
root = Tk()

#Sets the title of the root window
root.title("Welcome to TextQuestPy")

# Sets the window size
root.geometry('1920x1080')

txtBox = Entry(root, width = 250)
txtBox.grid(column = 10, row = 9)

# Keeps window open in the main loop.
root.mainloop()
