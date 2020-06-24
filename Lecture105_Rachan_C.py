class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAC(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello Driver!!")
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAC()
car1.sayHello()
pickup1 = Pickup()
pickup1.turnOnAC()
van1 = Van()
van1.turnOnAC()
estatecar1 = Estatecar()
estatecar1.turnOnAC()