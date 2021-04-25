import numpy as np

t = int(input())

for _ in range(t):
    n,m,k = [int(x) for x in input().split(" ")]
    
    matrix = [[0]*m]*n
    count = 0

    for i in range(n):
        matrix[i] = [int(x) for x in input().split()]

    arr = np.array(matrix)

    for z in range(1,min(n,m)+1):
        for i in range(n):
            for j in range(m):
                if i+z < n+1 and j+z < m+1  :
                    print(z,i,j,arr[i:i+z,j:j+z])
                    if np.sum(arr[i:i+z,j:j+z])/(z*z) >= k :
                        count += 1
                
                    
    print(count)