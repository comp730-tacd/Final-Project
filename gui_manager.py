from tkinter import *

root = Tk()
 

# Adjust size 
root.geometry("800x470")
  
# Add image file
bg = PhotoImage(file = "assets/house.png")
  
# Create Canvas
location_image = Canvas( root, width = 800, height = 600)
top_menu = Canvas(root, width = 800, height = 100, background="Black" )  


# Display image
location_image.create_image( 0, 0, image = bg, anchor=NW)


# functions
def click_travel():
    pass

def click_save():
    pass

def click_load():
    pass

# Create Buttons
travel_button = Button(root, text="Travel", padx=50, pady=10, command=click_travel,fg="white", bg="#929493")
save_button = Button(root, text="Save", padx=50, pady=10, command=click_save,fg="white", bg="#929493")
load_button = Button(root, text="Load", padx=50, pady=10, command=click_load,fg="white", bg="#929493")

# display
# travel_button.grid(row=0, column=0)
# save_button.grid(row=0, column=1)
# load_button.grid(row=0, column=2)

button1_canvas = top_menu.create_window( 10, 30, anchor = "nw", window = travel_button)
  
button2_canvas = top_menu.create_window( 190, 30, anchor = "nw", window = save_button)
  
button3_canvas = top_menu.create_window( 370, 30, anchor = "nw", window = load_button)

top_menu.grid(row=0, column=0)
location_image.grid(row=1, column=0)


# Execute tkinter
root.mainloop()