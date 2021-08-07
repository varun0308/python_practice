import numpy as np 

# arange creates an numpy array
# arange(start,finish,step)

print(np.arange(5))

print(np.arange(2,6))

print(np.arange(2,12,2))

print(np.arange(2.2,9.33))

print(np.arange(2.2,9.3,0.9))


"""
Prints : 
[0 1 2 3 4]
[2 3 4 5]
[ 2  4  6  8 10]
[2.2 3.2 4.2 5.2 6.2 7.2 8.2 9.2]
[2.2 3.1 4.  4.9 5.8 6.7 7.6 8.5]

"""

# Can add 2 array element like this

arr = np.arange(10)
print(arr)
print(arr[2]+arr[4])

"""
Prints : 
[0 1 2 3 4 5 6 7 8 9]
6
"""