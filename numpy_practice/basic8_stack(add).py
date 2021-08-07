import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr3 = [[11,12,13,14,15],[16,17,18,19,20]]

arr = np.stack((arr1,arr2),axis = 0)
print(arr)
print(arr.shape)
"""
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
 (2,5)
"""

arr4 = np.stack((arr,arr3),axis = 1)
print(arr4)

"""
[[[ 1  2  3  4  5]
  [11 12 13 14 15]]

 [[ 6  7  8  9 10]
  [16 17 18 19 20]]]
"""

print(arr4.shape)
# (2, 2, 5)



