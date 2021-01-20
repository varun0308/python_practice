# Not such a great example of  
# class and object program

class trial:
    # Random statement
    state = "My Code of classes "
    
    # One of the method
    def a(self,name):
        print("Hello",name)

    # __init__ method (suggested to use this)
    def __init__(self,name):
        self.name = name

    # Another method that uses __init__
    def b(self):
        print("Hello",self.name)

# Creating the object
obj = trial("Varun blah")

# Types of calling/printing
print(obj.state)
obj.a("Varun")
obj.b()
         