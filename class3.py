# Parent class A
class A: 
    # Variable passed through __init__ 
    def __init__(self, n):
        self.name = n 

    def age(self, a):
        self.age_ = a

# 1st child class B (inherited from A)
class B(A): 
    # Variable passed through __init__ 
    def __init__(self, name, age_ ,roll):

        # A class and __init__ func. is being called
        A.__init__(self, name)
        # A class and age_ func. is being called
        A.age(self, age_)
        # Variables defined inside __init__ of class B
        self.roll = roll 

        print(self.name)
        print(self.roll)
        print(self.age_)

# 2nd child class C (inherited from A)
class C(A) :
    # Variable passed through __init__ 
    def __init__(self,name ,idnumber):

        # A class and __init__ func. is being called
        A.__init__(self, name)
        # Variables defined inside __init__ of class C
        self.id = idnumber

        print(self.name)
        print(self.id)


# Initialising the objects
# No need to print anything, cause it has been told already
obj_a = A("Varun")
obj_b = B("Rahul",10, 4)
obj_c = C("Varun",20996)

