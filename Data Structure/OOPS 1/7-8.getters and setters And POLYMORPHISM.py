class Vehicle:

    def __init__(self, color, maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed #this is private so can't be acess at line 24

    def getMaxSpeed(self):
        return self.__maxSpeed

#this function has no use in in code but we can use it if we want to set
    # def setMaxSpeed(self, maxSpeed):
    #     self.__maxSpeed = maxSpeed


class Car(Vehicle):
# step 1
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Color :", self.color)

        # print("MaxSpeed :", self.maxspeed) # here it cant be acessed
        print("MaxSpeed :", self.getMaxSpeed()) # we use getfunction to access

        print("NumGears :", self.numGears)
        print("IsConvertible :", self.isConvertible)

#-------------Inheritance continue
# we just moved the print color and maxSpeed to parent class
class Vehicle:

    def __init__(self, color, maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed

    # def getMaxSpeed(self):
    #     return self.__maxSpeed

    # def setMaxSpeed(self, maxSpeed):
    #     self.__maxSpeed = maxSpeed

    # from child class it has moved here
    def print(self):
        print("Color :", self.color)
        print("MaxSpeed :", self.__maxSpeed)


class Car(Vehicle):

    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible
    # access anything from parent class using super keyword
    def printCar(self):
        super().print() or self.print()  #acessing method of super class
        print("NumGears :", self.numGears)
        print("IsConvertible :", self.isConvertible)


c = Car("red", 15, 3, False)
c.printCar()


c = Car("red", 15, 3, False)
c.printCar()

#POLYMORPHISM CONCEPT
# this we first look for print function in Car class if found it will print. if not found
# it will look print function in parent class Vehicle if found there it will print if not it will move to its
# parent class if there
c.print()
# if we specifically create Vehicle class object and call print function:
v = Vehicle('red' , 18)
v.print()
# this will only look for print function in Vehicle class
