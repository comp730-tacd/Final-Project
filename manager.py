from functions import RuntimeCommands

class Main:
    def __init__(self):
        self.selection ='n/a'

    def manager(self):
        self.start_menu()

    def start_menu(self):
        while True:
            print("""
            1 = Start New Game
            2 = Load A Game
            3 = Enable_Dev_Mode
            4 = Quit
            """)
            response = input("Please select a Menu Option: ")
            if response == '1':
                self.create_new_save()

            elif response == '2':
                self.file_check()

            elif response == '3':
                self.enable_dev_mode()

            elif response == '4':
                exit()

            else:
                print("Not an accepted input")

    def create_new_save(self):
        RuntimeCommands.printMenu(self)

    def file_check(self):
        pass

    def load_save(self):
        pass

    def enable_dev_mode(self):
        pass


Main().manager()

if __name__ == "manager":
    mainObject = Main()
    mainObject.Manager()