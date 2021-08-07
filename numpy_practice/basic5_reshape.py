import numpy as np
from numpy.core.fromnumeric import shape

# reshape converts given matrix into a matrix of n*n
# If it is not possible, it gives error
# reshape(outer list,inner list,planes)

arr1 = np.array([1,2,3,4,5,6,7,8,9])
new1 = arr1.reshape(3,3)

print(arr1)
print(arr1.shape)   # Gives shape
print(arr1.size)    # Gives total no. of elements

print(new1)
print(new1.shape)
print(new1.size)


# output -->
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

# ------------------------------------------------------------

arr2 = np.arange(1,25)
new2 = arr2.reshape(2,6,2)
# Shape = 2,6,2

print(new2)
print(new2[0][3][1])

print(new2.shape)

# output -->
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]
#   [ 7  8]
#   [ 9 10]
#   [11 12]]

#  [[13 14]
#   [15 16]
#   [17 18]
#   [19 20]
#   [21 22]
#   [23 24]]]
