#Used with an input of two strings (location and destination) to determine where you are headed, and how far you will have to travel.
#DEV NOTE: I may wish to return to this function later to abstract it out to make it so that location and destination are interchangable
def travel(location, destination):    
    if (location == "Manchester"):
        if (destination == "Nashua"):
            return int(19.5)
        if (destination == "Concord"):
            return int(18.2)
        if (destination == "Merrimack"):
            return int(11.6)
    if (location == "Nashua"):
        if (destination == "Manchester"):
            return int(19.5)
        if (destination == "Concord"):
            return int(34.5)
        if (destination == "Merrimack"):
            return int(7.6)
    if (location == "TEST"):
        if (destination == "TEST"):
            return milesPerGallon

#This, I feel, is a very... Unprofessional method to attempt to get this to work in the way that I want it to, but for now this may work as a stopgap.
#Manchester: 1
#Nashua: 10
#Concord: 100
#Merrimack: 1000
def tempTravel(location, destination):
    print("tempTravel init")
    distance = int(0)
    if (location == "Manchester") or (destination == "Manchester"):
        distance = distance + 1
    if (location == "Nashua") or (destination == "Nashua"):
        distance = distance + 10
    if (location == "Concord") or (destination == "Concord"):
        distance = distance + 100
    if (location == "Merrimack") or (destination == "Merrimack"):
        distance = distance + 1000
    if distance == 11:
        return int(19.5)
    if distance == 101:
        return int(18.2)
    if distance == 1001:
        return int(11.6)
    if distance == 110:
        return int(34.5)
    if distance == 1010:
        return int(7.6)
    if distance == 1100:
        return int(26.8)
    print(distance)

LOCATION = "Manchester"
DESTINATION = "Concord"
tempTravel(LOCATION, DESTINATION)
milesPerGallon = 15
maxGas = int(input("Please input a value for the max amount of gas for this vehicle: "))
currentGas = maxGas
currentGas = currentGas - ( travel(LOCATION, DESTINATION) / milesPerGallon)
print(currentGas)

