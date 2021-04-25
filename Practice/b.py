import numpy as np

matrix = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(matrix)

for i in range(3):
        for j in range(3):
            for z in range(1,3):
                print(i,j,z,arr[i:i+z,j:j+z])

print(matrix[0:1][0:2])
print(matrix[0:1][0:1])