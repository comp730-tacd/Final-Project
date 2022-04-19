import locations
import vehicles

class VehicleCommands:
    '''
    Contains commands having to do with the vehicle that are not confined to a certain location
    '''
    def gas_capacity(self, capacity, cur_amount):
        '''
        Used to check the remaining gas capacity in the car.
        Returns: list
        ind0: the empty space in the tank
        ind1: string that describes the current state of the gas tank
        '''
        if(0 < cur_amount < capacity):
            state = f"Gas tank at {cur_amount/capacity * 100}!"
            remaining = capacity - cur_amount
        elif(cur_amount < 0):
            state = "Gas tank Empty!"
            remaining = capacity
        elif(cur_amount > capacity):
            state = "Gas tank Overfilled!"
            remaining = 0
        else:
            state = "Gas tank state undefined. Error!"
        return [remaining, state]

    def range(self, mileage, cur_amount):
        '''
        Calculates the range based on the mileage of the car and the current amount of gas in the tank
        '''
        range = mileage * cur_amount
        return range

class LocationCommands:
    '''
    Containts commands that are limited to certain locations
    '''
    def pumpGas(self, capacity, cur_amount, cur_location):
        '''
        Used to pump gas into the car. Also prevents user from pumping gas while they are not at the gas station.
        returns: int
        -10: error: not at gas station
        -1: tank is already full
        0: no gas bought
        any positive number: amount of gas bought
        '''
        if(cur_location != locations.Gas_Station):
            return(-10) #returns -10. This should trigger a message that the user is not at the gas station
        elif(cur_location == locations.Gas_Station):
            while True:
                ordered = input("How much gas would you like to buy?")
                gas_cap = VehicleCommands.gas_capacity(capacity, cur_amount)
                space_in_tank = gas_cap[0]
                if(space_in_tank == 0):
                    return(-1) #this should trigger a message that there is no space in the tank/the tank is already full
                else:
                    if(ordered < space_in_tank):
                        return ordered
                    else:
                        print("Not enough room in tank. Please enter a smaller amount.")
                    


                    

class RuntimeCommands:
    '''
    Contains commands that pertain to the operation of the game, not neccesarily having to do with vehicles.'''
    def printMenu(self):
        '''
        Prints the menu for vehicle selection at the beginning of the game, and when the user can change vehicles
        '''
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