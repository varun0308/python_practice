import numpy as np

arr1 = [1,2,3,4]
arr2 = [6,7,8,9]
arr3 = np.stack((arr1,arr2),axis=1)

print(type(arr3))
print(arr3.size)
print(arr3[3][1])


print(arr3)
# output --> 
# [[1 6]
#  [2 7]
#  [3 8]
#  [4 9]]

''' Should be interpreted as 1 row, each of that row has 2 rows & 1 column'''