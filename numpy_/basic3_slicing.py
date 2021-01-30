import numpy as np

arr1 = np.array([[1,3,2,4],[5,7,6,8]])

print(arr1[1,1:4])
print(arr1[0:2,2])
print(arr1[0:2,1:4])

print(arr1.shape)