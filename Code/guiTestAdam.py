#!/bin/python3.8
from tkinter import *

root = Tk()

#creating a label widget
myLabel = Label(root, text="Hello, world!")

#shoving it onto the screen
myLabel.pack()

root.mainLoop()
