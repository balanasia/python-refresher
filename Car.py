class Car():
    #class variable
    wheels = 4

    #constructor
    def __init__(self, make, model, year, color):
        # instance variables
        self.make = make 
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The " +  self.model + " is driving")

    def stop(self):
        print("The " + self.model +  " is stopped")