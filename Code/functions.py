import locations
import vehicles

class VehicleCommands:
    def gas_capacity(self, capacity, cur_amount):
        if(0 < cur_amount < capacity):
            state = f"Gas tank at {cur_amount/capacity * 100}!"
        elif(cur_amount < 0):
            state = "Gas tank Empty!"
        elif(cur_amount > capacity):
            state = "Gas tank Overfilled!"
        else:
            state = "error"
        return state

    def travel(self):    
        print("To be implemented")
        #Retrieve information on where you are, and where you're going, and add the two together to find your travel distance.
        #Once you have how far you're going to travel, take (distanceTravelled / milesPerGallon ) and subtract that from your current gas.

class RuntimeCommands:
    def printMenu(self):
        print("Select your vehicle by typing in the number: \n")
        print(f"1. {vehicles.Accord.name}, a {vehicles.Accord.v_type}, with a speed of {vehicles.Accord.speed} and gas mileage of {vehicles.Accord.mileage}")
        print(f"2. {vehicles.BMW2.name}, a {vehicles.BMW2.v_type}, with a speed of {vehicles.BMW2.speed} and gas mileage of {vehicles.BMW2.mileage}")
        print(f"3. {vehicles.CRV.name}, a {vehicles.CRV.v_type}, with a speed of {vehicles.CRV.speed} and gas mileage of {vehicles.CRV.mileage}")
        print(f"4. {vehicles.Camaro.name}, a {vehicles.Camaro.v_type}, with a speed of {vehicles.Camaro.speed} and gas mileage of {vehicles.Camaro.mileage}")
        print(f"5. {vehicles.Frontier.name}, a {vehicles.Frontier.v_type}, with a speed of {vehicles.Frontier.speed} and gas mileage of {vehicles.Frontier.mileage}")
        print(f"6. {vehicles.Fusion.name}, a {vehicles.Fusion.v_type}, with a speed of {vehicles.Fusion.speed} and gas mileage of {vehicles.Fusion.mileage}")
        print(f"7. {vehicles.Impala.name}, a {vehicles.Impala.v_type}, with a speed of {vehicles.Impala.speed} and gas mileage of {vehicles.Impala.mileage}")
        print(f"8. {vehicles.Mustang.name}, a {vehicles.Mustang.v_type}, with a speed of {vehicles.Mustang.speed} and gas mileage of {vehicles.Mustang.mileage}")
        print(f"9. {vehicles.Q3.name}, a {vehicles.Q3.v_type}, with a speed of {vehicles.Q3.speed} and gas mileage of {vehicles.Q3.mileage}")
        print(f"10. {vehicles.Ram.name}, a {vehicles.Ram.v_type}, with a speed of {vehicles.Ram.speed} and gas mileage of {vehicles.Ram.mileage}")
        print(f"11. {vehicles.Tucson.name}, a {vehicles.Tucson.v_type}, with a speed of {vehicles.Tucson.speed} and gas mileage of {vehicles.Tucson.mileage}")
        print(f"12. {vehicles.Tundra.name}, a {vehicles.Tundra.v_type}, with a speed of {vehicles.Tundra.speed} and gas mileage of {vehicles.Tundra.mileage}")