from tkinter import *
  
root = Tk()
 

# Adjust size 
root.geometry("1920x1200")
  
# Add image file
bg = PhotoImage(file = "assets/house.png")
  
# Create Canvas
location_image = Canvas( root, width = 1000, height = 800)
top_menu = Canvas(root, width = 1000, height = 200 )  

  
# Display image
location_image.create_image( 0, 0, image = bg)
top_menu.create_rectangle(0, 0, 100, 100)
  

# functions
def click_travel():
    pass

def click_save():
    pass

def click_load():
    pass

# Create Buttons
travel_button = Button(root, text="Travel", padx=50, command=click_travel,fg="white", bg="#929493")
save_button = Button(root, text="Save", padx=50, command=click_save,fg="white", bg="#929493")
load_button = Button(root, text="Load", padx=50, command=click_load,fg="white", bg="#929493")

# display
# travel_button.grid(row=0, column=0)
# save_button.grid(row=0, column=1)
# load_button.grid(row=0, column=2)

top_menu.grid(row=1, column=0)
location_image.grid(row=2, column=0)


# Execute tkinter
root.mainloop()