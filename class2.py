class vehicle:

    def __init__(self,wheel,vehicle_,size):
        self.wheel = wheel
        self.vehicle_ = vehicle_
        self.size = size

    def wheels(self):
        print("No. of wheels =",self.wheel) 

    def sizes(self):
        print("Size of the",self.vehicle_ ,"is",self.size)

a=input()
b=input()
c=input()

obj = vehicle(a,b,c)

obj.wheels()
obj.sizes()

