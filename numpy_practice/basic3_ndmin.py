import numpy as np

# ndmin creates the specified dimension
# Not same as reshaping

arr = np.array([1,2,3,4,], ndmin = 3)
arr1 = np.array([1,2,3,4,5,6,7,8],ndmin = 2)

# makes a 3-dimension array
print(arr)      
print(arr1)

"""
 Prints : 
 [[[1 2 3 4]]]
 [[1 2 3 4 5 6 7 8]]
"""