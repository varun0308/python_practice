import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) 
arr2 = np.array([1,2,3,4,5,6])

# array_split is a method, it is overwritten on the earlier array
# Don't do arr2 = np.array_split(arr1,3)
arr3 = np.array_split(arr1,3)
np.array_split(arr2,3)

print(arr1)
print(arr3)
print(arr1[2])
print(arr1[2][1])
print(type(arr1))
print(arr1.shape)

print(arr2)
print(arr2.shape)