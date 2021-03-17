from numpy import random

# Random number x
x = random.rand()
print(x)

# Random integer x
x = random.randint(10)
print(x)

# 4 random integer
x = random.randint(20,size=4)
print(x)

# Makes a np array of size (3,5) with only 3,5,7,9
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# Makes a np array of size (3,5) with numbers from 0 to 19
x = random.choice(20, size=(3, 5))
print(x)