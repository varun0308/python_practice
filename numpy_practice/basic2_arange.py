import numpy as np 

print(np.arange(5))

print(np.arange(2,6))

print(np.arange(2,12,2))

print(np.arange(2.2,9.33))

print(np.arange(2.2,9.3,0.9))

# Can add 2 array element like this

arr = np.arange(10)
print(arr)
print(arr[2]+arr[4])

arr1 = np.array([[1,3,2,4],[5,7,6,8]])
print(arr1[1][3])