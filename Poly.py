
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")


def describe_movement(vehicle):
    vehicle.move()


car = Car()
plane = Plane()
boat = Boat()


for v in [car, plane, boat]:
    describe_movement(v)
