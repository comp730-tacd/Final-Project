from re import L
from tkinter import *

root = Tk()

root.geometry("400x400")



# functions
def click_yes():
    mylabel1 = Label(root, text="You selected Yes!")
    mylabel1.grid(row=0, column=0)

def click_no():
    mylabel1 = Label(root, text="You selected No!")
    mylabel1.grid(row=0, column=0)

def click_enter():
    input = "hello " + entry_box.get()
    mylabel2 = Label(root, text=input)
    mylabel2.grid(row=6, column=0)

# create
entry_box = Entry(root)
entry_box.insert(0, "Enter your name!")

mylabel1 = Label(root, text="Select your option!")
mylabel2 = Label(root)

mybutton1 = Button(root, text="yes", padx=50, command=click_yes,fg="white", bg="#929493")
mybutton2 = Button(root, text="no", padx=50, command=click_no,fg="white", bg="#929493")
mybutton3 = Button(root, text="Enter", padx=50, command=click_enter,fg="white", bg="#929493")


# display
entry_box.grid(row=5, column=0)

mylabel1.grid(row=0, column=0)

mybutton1.grid(row=4, column=0)
mybutton2.grid(row=4, column=1)
mybutton3.grid(row=5, column=1)

root.mainloop()