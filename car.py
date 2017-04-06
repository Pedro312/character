class Vehicle(object):
    def __init__ (self, name, motor, material, vtype):
        self.motor = motor
        self.material = material
        self.name = name
        self.vtype = vtype
        
        
class Car(Vehicle):
    def __init__(self, name, motor, material):
        super(Car, self). __init__(name, motor, material, "Car")
        self.engine_status = False
    def move(self):
        if self.engine_status:
            print "You move forward"
        else:
            print "The car is off."
                
    def engine_on(self):
        self.engine_status =True
        print "You turn the key and the engine turns on."
        
        
class KeylessCar(Car):
    def __init__(self, name, motor, material):
        super(KeylessCar, self).__init__(name, motor, material)
    def move(self):
        if self.engine_status:
            print "You move forward"
        else:
            print "The car is off."
    def engine_on(self):
        self.engine_status =True
        print "You press a button and the engine turns on ."
    
        
#Test code
wiebe_car = KeylessCar("Wiebe Mobile", "V10", "Carbon Fiber")
wiebe_car.engine_on()
wiebe_car.move()