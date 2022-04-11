# TACD - COMP 730 Project
# Chris Inzinga

carSelection = "null"

def carSelect():

    print("1. Compact Car\n2. Electric Car\n3. Truck\n4. SUV")
    response = input("Please choose an option: ")

    if response == "1":
        selection = "Compact Car"
        return selection
    elif response == "2":
        selection = "Electric Car"
        return selection
    elif response == "3":
        selection = "Truck"
        return selection
    elif response == "4":
        selection = "SUV"
        return selection
    else:
        print("Error")




def main():
    carSelect()


if __name__ == '__main__':
    main()
