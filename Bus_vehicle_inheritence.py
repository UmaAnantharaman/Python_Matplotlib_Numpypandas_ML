#Base class
class Vehicle:
    def __init__(self,mode):
        self.public =  mode


    def Vehicle_passengers(self):
        self.no_of_passengers = int(input())
        print("Vehicle passengers",self.no_of_passengers)
        

#Derived class
class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self,"private")

    def Bus_passengers(self):
        self.capacity = 50
        print("Bus passengers",self.capacity)


b = Bus()
#Able to access base class method
b.Vehicle_passengers() 
b.Bus_passengers()
    


