# Parent Class / superclass
class Vehicle:
    def __init__(self, color, maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed


# Derived class / child class
# inheriting maxSpeed and color properties from Parent class
class Car(Vehicle):
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        # using super().method name to access parent or super class
        super().__init__(color,maxSpeed)  # calling super class or parent class
                                          # and passing two values and using rest two here
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Color :", self.color)
        print("MaxSpeed :", self.maxSpeed)
        print("NumGears :", self.numGears)
        print("IsConvertible :", self.isConvertible)


c = Car("red", 150, 5, False)  # calling class passing values
c.printCar()
