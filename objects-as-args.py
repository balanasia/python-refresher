from email.errors import NonPrintableDefect


class Car:

    color = None

class Motorcycle:

    color = NonPrintableDefect
    

def change_color(vehicle, color):
    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()

motorcycle1 = Motorcycle()
motorcycle2 = Motorcycle()
motorcycle3 = Motorcycle()

change_color(car1, "Green")
change_color(car2, "Pink")
change_color(car3, "Purple")

change_color(motorcycle1, "Orange")
change_color(motorcycle2, "Black")
change_color(motorcycle3, "Maroon")

print(car1.color)
print(car2.color)
print(car3.color)

print(motorcycle1.color)
print(motorcycle2.color)
print(motorcycle3.color)