# Not such a great example of  
# class and object program

class trial:
    # Random value, but is hidden to the outside world
    # All attributes inside this class can access  
    # this variable 5 but outside doesn't know it exists
    __value = 5
    # Random statement
    state = "My Code of classes "
    
    # One of the method
    def a(self,name):
        print("Hello",name)

    # __init__ method (suggested to use this)
    # Only assigns values to the attributes
    def __init__(self,name):
        # self.n assigns n as name (value input of name goes to n)
        self.n = name

    # Another method that uses __init__
    def b(self):
        print("Hello",self.n)

# Creating the object
obj = trial("Varun blah")

# Types of calling/printing
print(obj.state)
obj.a("Varun")
obj.b()
         