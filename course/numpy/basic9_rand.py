from numpy import random

x = random.rand()
print(x)

x = random.randint(10)
print(x)

x = random.randint(20,size=4)
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

x = random.choice(20, size=5)
print(x)

x = random.choice(20, size=(3, 5))
print(x)
