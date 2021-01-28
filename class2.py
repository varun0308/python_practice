class vehicle:

    def __init__(self,wheel,vehicle_,size):
        self.w = wheel
        self.v= vehicle_
        self.s = size

    def wheels(self):
        print("No. of wheels =",self.w) 

    def sizes(self):
        print("Size of the",self.v ,"is",self.s)

a=input()
b=input()
c=input()

obj = vehicle(a,b,c)

obj.wheels()
obj.sizes()

