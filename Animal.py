class Animal():

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

class Fish(Animal):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.eat()
hawk.fly()