# abstract class = A class that can not instantiated on it's own, meant to be subclass,
#                   They can contain abstract methods, which are declared but have no implementation.
# abstract class benifits:
#               1. Prevents installation of the class itself 
#               2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('You drive the car')

    def stop(self):
        print('You stop the car')

class Motorcycle(Vehicle):
    def go(self):
        print('You ride the Motorcycle')

    def stop(self):
        print('You stop the Motorycle')

class Boat(Vehicle):
    def go(self):
        print('You sail the Boat')
    # def stop(self):
    #     print('You anchor the boat')


boat = Boat()

boat.go()