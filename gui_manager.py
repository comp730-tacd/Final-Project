import tkinter as tk


class App():
    def __init__(self):
        # core
        self.root = tk.Tk()
        self.root.title("Car Sim")

        self.frame = tk.Frame(self.root, padx=50, pady = 50, bg = "#4E4187", relief= tk.SUNKEN) 

        self.pbg = tk.PhotoImage(file = "assets/house.png")


        self.pic_canvas = tk.Canvas(self.frame, width=1000, height=470)
        self.micro_canvas = tk.Canvas(self.frame, width=498, height=230, bg="#929493")
        self.macro_canvas = tk.Canvas(self.frame, width=1000, height=70, bg="black")
        self.term_canvas = tk.Canvas(self.frame, width=498, height=230, bg="green")

        self.pic_canvas.create_image(500, 200, image = self.pbg)

        self.pic_canvas.grid(row=0, column=1, columnspan=2)
        self.micro_canvas.grid(row=1, column=1)
        self.macro_canvas.grid(row=2, column=1, columnspan=2)
        self.term_canvas.grid(row=1, column=2)

        # Macro Buttons

        def click_travel():
            pass

        def click_save():
            pass

        def click_load():
            pass

        self.travel_button = tk.Button(self.macro_canvas, text="Travel", padx=50, pady=10, command=click_travel,fg="white", bg="#777877")
        self.save_button = tk.Button(self.macro_canvas, text="Save", padx=50, pady=10, command=click_save,fg="white", bg="#777877")
        self.load_button = tk.Button(self.macro_canvas, text="Load", padx=50, pady=10, command=click_load,fg="white", bg="#777877")    

        self.macro_travel = self.macro_canvas.create_window( 30, 15, anchor = "nw", window = self.travel_button)    
        self.macro_save = self.macro_canvas.create_window( 210, 15, anchor = "nw", window = self.save_button)   
        self.macro_load = self.macro_canvas.create_window( 390, 15, anchor = "nw", window = self.load_button)  

        # Micro Buttons

        def click_int_one():
            pass
        
        def click_int_two():
            pass
        
        def click_int_three():
            pass
        
        def click_int_four():
            pass
        
        def click_int_five():
            pass
        
        def click_int_six():
            pass

        self.interaction_one = tk.Button(self.micro_canvas, text="Interaction 1", padx=50, pady=10, command=click_int_one,fg="white", bg="#777877")
        self.interaction_two = tk.Button(self.micro_canvas, text="Interaction 2", padx=50, pady=10, command=click_int_two,fg="white", bg="#777877")
        self.interaction_three = tk.Button(self.micro_canvas, text="Interaction 3", padx=50, pady=10, command=click_int_three,fg="white", bg="#777877")    
        self.interaction_four = tk.Button(self.micro_canvas, text="Interaction 4", padx=50, pady=10, command=click_int_four,fg="white", bg="#777877")
        self.interaction_five = tk.Button(self.micro_canvas, text="Interaction 5", padx=50, pady=10, command=click_int_five,fg="white", bg="#777877")
        self.interaction_six = tk.Button(self.micro_canvas, text="Interaction 6", padx=50, pady=10, command=click_int_six,fg="white", bg="#777877")   

        self.micro_interaction_one = self.micro_canvas.create_window( 60, 30, anchor = "nw", window = self.interaction_one)    
        self.micro_interaction_two = self.micro_canvas.create_window( 60, 90, anchor = "nw", window = self.interaction_two)   
        self.micro_interaction_three = self.micro_canvas.create_window( 60, 150, anchor = "nw", window = self.interaction_three)  
        self.micro_interaction_four = self.micro_canvas.create_window( 270, 30, anchor = "nw", window = self.interaction_four)    
        self.micro_interaction_five = self.micro_canvas.create_window( 270, 90, anchor = "nw", window = self.interaction_five)   
        self.micro_interaction_six = self.micro_canvas.create_window( 270, 150, anchor = "nw", window = self.interaction_six)  



        self.frame.pack()
        self.root.mainloop()



a = App()


