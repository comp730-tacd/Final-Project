import tkinter as tk                
from tkinter import font as tkfont  



class App(tk.Tk):
=======
class App():
    '''
    Manages the GUI, sets everything up, and makes everything work.
    '''
    def __init__(self):
        # core
        self.root = tk.Tk()
        self.root.title("Car Sim")


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, padx=50, pady = 50, bg = "#4E4187", relief= tk.SUNKEN)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.pbg = tk.PhotoImage(file = "assets/street_copy.png")

        pic_canvas = tk.Canvas(self, width=1000, height=778, bg="black")

        pic_canvas.create_image(500, 389, image = self.pbg)

        pic_canvas.grid(row=1, column=1)  

        

        new_game_button = tk.Button(self, text="New Game", padx=40, pady=11, font=("Arial", 11, 'bold'), command=lambda: controller.show_frame("PageOne"), fg="#fcfcfc", bg="#6806c9") 
        new_game_button = pic_canvas.create_window( 500 , 300, anchor = "center", window = new_game_button) 

        load_game_button = tk.Button(self, text="Load Game", padx=38, pady=11, font=("Arial", 11, 'bold'), command=lambda: controller.show_frame("PageTwo"), fg="#fcfcfc", bg="#6806c9") 
        load_game_button = pic_canvas.create_window( 500 , 375, anchor = "center", window = load_game_button) 

        dev_mode_button = tk.Button(self, text="Dev Mode", padx=41, pady=11, font=("Arial", 11, 'bold'), command=lambda: controller.show_frame("PageTwo"), fg="#fcfcfc", bg="#6806c9") 
        dev_mode_button = pic_canvas.create_window( 500 , 450, anchor = "center", window = dev_mode_button) 



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        # Layout "core"
        self.pbg = tk.PhotoImage(file = "assets/house.png")

        pic_canvas = tk.Canvas(self, width=1000, height=470)
        micro_canvas = tk.Canvas(self, width=498, height=230, bg="#929493")
        macro_canvas = tk.Canvas(self, width=1000, height=70, bg="black")
        term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")        

        pic_canvas.create_image(500, 200, image = self.pbg)

        pic_canvas.grid(row=0, column=1, columnspan=2)
        micro_canvas.grid(row=1, column=1)
        macro_canvas.grid(row=2, column=1, columnspan=2)
        term_canvas.grid(row=1, column=2)


        # Macro Buttons

        def click_travel():
            pass

        def click_save():
            pass

        def click_load():
            pass

        def click_quit():
            quit()


        travel_button = tk.Button(macro_canvas, text="Travel", padx=50, pady=10, command=click_travel,fg="white", bg="#777877")
        save_button = tk.Button(macro_canvas, text="Save", padx=50, pady=10, command=click_save,fg="white", bg="#777877")
        load_button = tk.Button(macro_canvas, text="Load", padx=50, pady=10, command=click_load,fg="white", bg="#777877")  
        quit_button = tk.Button(macro_canvas, text="Quit", padx=50, pady=10, command=click_quit,fg="white", bg="#777877")   
        main_menu_button = tk.Button(macro_canvas, text="Main Menu", padx=38, pady=10, command=lambda: controller.show_frame("StartPage"),fg="white", bg="#777877") 

        travel_button = macro_canvas.create_window( 70, 15, anchor = "nw", window = travel_button)    
        save_button = macro_canvas.create_window( 250, 15, anchor = "nw", window = save_button)   
        load_button = macro_canvas.create_window( 430, 15, anchor = "nw", window = load_button)  
        quit_button = macro_canvas.create_window( 790, 15, anchor = "nw", window = quit_button)  
        main_menu_button = macro_canvas.create_window( 610, 15, anchor = "nw", window = main_menu_button)  


        # Micro Buttons


        def click_int_one():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked One", font=("Arial", 22))
        
        def click_int_two():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked Two", font=("Arial", 22))
        
        def click_int_three():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked Three", font=("Arial", 22))

        def click_int_four():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked Four", font=("Arial", 22))

        def click_int_five():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked Five", font=("Arial", 22))
        
        def click_int_six():
            term_canvas = tk.Canvas(self, width=498, height=230, bg="#5e7ef2")
            term_canvas.grid(row=1, column=2)
            term_canvas.create_text(200,100, text="You picked Six", font=("Arial", 22))

        interaction_one = tk.Button(micro_canvas, text="Interaction 1", padx=50, pady=10, command=click_int_one,fg="white", bg="#777877")
        interaction_two = tk.Button(micro_canvas, text="Interaction 2", padx=50, pady=10, command=click_int_two,fg="white", bg="#777877")
        interaction_three = tk.Button(micro_canvas, text="Interaction 3", padx=50, pady=10, command=click_int_three,fg="white", bg="#777877")    
        interaction_four = tk.Button(micro_canvas, text="Interaction 4", padx=50, pady=10, command=click_int_four,fg="white", bg="#777877")
        interaction_five = tk.Button(micro_canvas, text="Interaction 5", padx=50, pady=10, command=click_int_five,fg="white", bg="#777877")
        interaction_six = tk.Button(micro_canvas, text="Interaction 6", padx=50, pady=10, command=click_int_six,fg="white", bg="#777877")   

        interaction_one = micro_canvas.create_window( 60, 30, anchor = "nw", window = interaction_one)    
        interaction_two = micro_canvas.create_window( 60, 90, anchor = "nw", window = interaction_two)   
        interaction_three = micro_canvas.create_window( 60, 150, anchor = "nw", window = interaction_three)  
        interaction_four = micro_canvas.create_window( 270, 30, anchor = "nw", window = interaction_four)    
        interaction_five = micro_canvas.create_window( 270, 90, anchor = "nw", window = interaction_five)   
        interaction_six = micro_canvas.create_window( 270, 150, anchor = "nw", window = interaction_six)  






class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()