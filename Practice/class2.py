class vehicle:

    def __init__(self,wheel,company,seats):
        self.w = wheel
        self.c = company
        self.s =seats

    def wheels(self):
        print("No. of wheels =",self.w) 

    def company(self):
        print("Vehicle is of",self.c,"company")
    
    def seats(self):
        print("Vehicle has",self.s,"seats")

for i in range (3) :
    print("Give no. of wheels,company and no. of seats")
    a,b,c = [x for x in input().split()]

    vehicle1 = vehicle(a,b,c)
    vehicle1.wheels()
    vehicle1.company()
    vehicle1.seats()

