class Vehicle:
    def calculateFare(self, distance):
        pass

class Bus(Vehicle):
    def calculateFare(self, distance):
        return distance * 50

class Taxi(Vehicle):
    def calculateFare(self, distance):
        return distance * 100

bus = Bus()
taxi = Taxi()
distance = 10

print(f"Bus Fare for {distance}km: KSh {bus.calculateFare(distance)}")
print(f"Taxi Fare for {distance}km: KSh {taxi.calculateFare(distance)}")
