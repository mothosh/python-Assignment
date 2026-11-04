class Vehicle:
    def __init__(self):
        self.reg_number = ""
        self.model = ""

    def displayVehicle(self):
        print(f"Registration Number: {self.reg_number}")
        print(f"Model: {self.model}")

class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.passenger_capacity = 0

    def displayBus(self):
        self.displayVehicle()
        print(f"Passenger Capacity: {self.passenger_capacity} passengers")

bus = Bus()
bus.reg_number = "KDA 123A"
bus.model = "Isuzu"
bus.passenger_capacity = 62
bus.displayBus()
