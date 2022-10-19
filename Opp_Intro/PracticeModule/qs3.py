class Vehicle:
   #class attributes
    color="white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus(" Volvo", 180, 12)
print("Bus color:",School_bus.color,"Bus Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
