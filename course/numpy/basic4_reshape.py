import numpy as np

# reshape converts given matrix into a matrix of n*n
# If it is not possible, it gives error
# Try the following with arr1 and arr2

arr1 = np.array([1,2,3,4,5,6,7,8,9])
new1 = arr1.reshape(3,3)

# arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
# new2 = arr2.reshape(3,3)

print(new1)

# output -->
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
# ------------------------------------------------------------
# extra number inside (a,b,c) it makes c planes 
arr2 = np.arange(1,25)
new2 = arr2.reshape(2,6,2)
# Shape = 2,6,2

print(new2)
print(new2[0][3][1])



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

''' But we shouldn't interpret it as that output.
    It is a 3-d structure, with 2 rows, 6 columns, and 2 planes.
    Computers can't give a better output, hence that.
    After 3-d, hard for us too.
    INTUTION    
'''