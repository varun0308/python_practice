import numpy as np

# Flattening (makes n-d matrix into 1-d matrix)
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
new1 = arr1.reshape(-1)
print(new1)