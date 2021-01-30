# NumPy used to create n-dimensional arrays
# Homogenous array (should be all int or all string.....)

import numpy as np

a= np.array(42)
b= np.array([1,3,2])
c= np.array([[[1,3,2]]])

# a.ndim gives the dimension of that array
print(a.ndim,b.ndim,c.ndim)








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



import pandas as pd

var = pd.Series([1,3,2,6,4,7])
print(var)

a = [1, 7, 2, 8]

myvar = pd.Series(a, index = ["x", "y", "z", "j"])

print(myvar)


