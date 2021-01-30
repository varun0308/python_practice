import numpy as np
arr = np.array([3,2,0,1,8,6,7,4,9,5])

# where method is like if-else
x = np.where(arr%2 == 0)
print(x)

# Sorts the array
print(np.sort(arr))

# Similar to where()
bool_result = (arr % 2 == 0)
newarr = arr[bool_result]
print(bool_result)
print(newarr)