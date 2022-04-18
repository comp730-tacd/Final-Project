class Main:
    def __init__(self):
        self.selection ='n/a'


    def Manager(self):
        self.Start_Menu

    def Start_Menu(self):
        while True:
            print("""
            1 = Start New Game
            2 = Load A Game
            3 = Enable_Dev_Mode
            4 = Quit
            """)
            response = input("Please select a Menu Option: ")
            if response == '1':
                self.Create_New_Save

            elif response == '2':
                self.File_Check

            elif response == '3':
                self.Enable_Dev_Mode

            elif response == '4':
                break

            else:
                print("Not an accepted input")

    def Create_New_Save(self):
        pass

    def File_Check(self):
        pass

    def Load_Save(self):
        pass

    def Enable_Dev_Mode(self):
        pass


Main().Manager()

if __name__ == "manager":
    mainObject = Main()
    mainObject.Manager()