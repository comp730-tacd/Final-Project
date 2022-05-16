from functions import VehicleCommands, LocationCommands


class UnitTests:
    def __init__(self):
        pass

    def unit_test_1(self):
        milage = 20
        cur_amount = 5

        print(VehicleCommands.range(self, milage, cur_amount))

    def unit_test_2(self):
        capacity = 20
        cur_amount = -1

        print(VehicleCommands.gas_capacity(self, capacity, cur_amount))

    def unit_test_3(self):
        capacity = 2000
        cur_amount = 10
        cur_location = None

        print(LocationCommands.pumpGas(self, capacity, cur_amount, cur_location))


print("Unit test 1 should return 20 * 5 = 100:")
UnitTests().unit_test_1()

print("\nUnit test 2 should say gas tank is empty")
UnitTests().unit_test_2()

print("\nUnit test 3 should return -10 as that is the error for not at gas station")
UnitTests().unit_test_3()
