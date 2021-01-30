# NumPy used to create n-dimensional arrays
# Homogenous array (should be all int or all string.....)

import numpy as np

a= np.array(42)
b= np.array([1,3,2])
c= np.array([[[1,3,2]]])

# a.ndim gives the dimension of that array
print(a.ndim,b.ndim,c.ndim)











import pandas as pd

var = pd.Series([1,3,2,6,4,7])
print(var)

a = [1, 7, 2, 8]

myvar = pd.Series(a, index = ["x", "y", "z", "j"])

print(myvar)


