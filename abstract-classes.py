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
        print("You drive the car")

    def stop(self):
        print("This car has stopped")


class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("This motorcycle stopped")

class Bicycle(Vehicle):
    def go(self):
        print("You drive the bicycle")

    def stop(self):
        print("This bicycle has stopped")

car = Car()
motorcycle = Motorcycle()
bicycle = Bicycle()

car.go()
car.stop()
motorcycle.go()
motorcycle.stop()
bicycle.go()
bicycle.stop()