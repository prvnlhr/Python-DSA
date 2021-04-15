# class Vehicle:
#      def __init__(self,color):
#          self.color = color
# class Car(Vehicle):
#      def __init__(self,color,numGears):
#          self.numGears = numGears
#  c= Car("black",5)
#  print(c.color)

class Vehicle:
     def __init__(self,color):
         self.color = color
class car(Vehicle):
     def __init__(self,color,numGears):
         super().__init__(color) #if this statement is not there we gets error
         self.numGears = numGears
c = car("black",5)
print(c.color)
