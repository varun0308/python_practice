class Parent():
    def __init__(self,name,a,b,c):
        self.n = name
        self.a = a
        self.b = b
        self.c = c

    def score(self):
        s = self.a+self.b+self.c
        return s

class Child(Parent):
    def pass_fail(self, s):
        if s>=100:
            print("Pass")
        else:
            print("Fail")


obj1 = Parent("Varun", 2 , 5 , 18)
print(obj1.score())

obj2 = Child("Varun", 2 , 5 , 18)
obj2.pass_fail(obj1.score())