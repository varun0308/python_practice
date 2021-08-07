import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

# In 2d array, slicing is done similar to indexing;
# arr(a,b) where a talks about the inner array 
# and b about each elements inside the array 

print(arr[1,1:4])
'[6 7 8]'

print(arr[0:2,2])
'[3 7]'

print(arr[0:2])
'''[[1 2 3 4]
    [5 6 7 8]]'''

print(arr[0:2,1:4])
'''[[2 3 4]
    [6 7 8]]'''

print(arr[:,:])
'''[[1 2 3 4]
    [5 6 7 8]]'''

print(arr.shape)
'(2,4)'

arr1 = np.array([[[11,22,33],[44,55,66],[77,88,99]],[[1,2,3],[4,5,6],[7,8,9]]])

print(arr1[0,:,1])
print(arr1[:,:,0])
print(arr1.shape)

"""
[22 55 88]
[[11 44 77]
 [ 1  4  7]]
(2, 3, 3)

"""