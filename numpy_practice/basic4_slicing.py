import numpy as np

arr1 = np.array([[1,2,3,4],[5,6,7,8]])

# In 2d array, slicing is done similar to indexing;
# arr1(a,b) where a talks about the inner array 
# and b about each elements indide the array 

print(arr1[1,1:4])
'[6 7 8]'

print(arr1[0:2,2])
'[3 7]'

print(arr1[0:2])
'''[[1 2 3 4]
 [5 6 7 8]]'''

print(arr1[0:2,1:4])
'''[[2 3 4]
 [6 7 8]]'''

print(arr1.shape)
'(2,4)'