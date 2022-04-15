class Vehicle_Commands:
    def gas_capacity(self, capacity, cur_amount):
        if(0 < cur_amount < capacity):
            state = "good"
        elif(cur_amount < 0):
            state = "Gas tank Empty!"
        elif(cur_amount > capacity):
            state = "Gas tank Overfilled!"
        else:
            state = "Error: Gas tank state undefined."
        return state