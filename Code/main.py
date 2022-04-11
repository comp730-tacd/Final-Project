milesPerGallon = 5
maxGas = int(input("Please input a value for the max amount of gas for this vehicle: "))
currentGas = maxGas
print ("Driving as far as possible on current tank.")
miles = int(0)
while currentGas > 0:
    #sleep(1)
    miles = miles + milesPerGallon
    currentGas = currentGas - 1
print ("Car is out of gas. You drove " +  str(miles) +  " miles!")