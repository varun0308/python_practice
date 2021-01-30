# Parent class 
class Cars(): 
    # Variable passed through __init__ 
    def __init__(self, wheels, steering, mirror):
        self.wheels = wheels
        self.mirror = mirror
        self.steering = steering

# 1st child class  (inherited from Cars)
class Audi(Cars): 
    # Variable passed through properties function 
    def __init__(self, wheels, steering, mirror, petrol_consumption, range_fulltank, gears):
        Cars.__init__(self, wheels, steering, mirror)

        self.petrol_consumption = petrol_consumption
        self.gears = gears
        self.range_fulltank = range_fulltank

# 2nd child class (inherited from Cars)
class Tesla(Cars) :
    # Variable passed through properties function  
    def __init__(self, wheels, steering, mirror, battery_consumption, range_fullcharge):
        Cars.__init__(self, wheels, steering, mirror)

        self.battery_consumption = battery_consumption
        self.range_fullcharge = range_fullcharge


a,b,c = [int(x) for x in input().split()]
d,e,f = [int(x) for x in input().split()]
p,q   = [int(x) for x in input().split()]

# Initialising the objects
obj_a = Cars(a,b,c)
obj_b = Audi(a,b,c,d,e,f)
obj_c = Tesla(a,b,c,p,q)

print(obj_a.mirror)
print(obj_b.range_fulltank)
print(obj_c.battery_consumption)