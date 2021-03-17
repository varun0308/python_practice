import pandas as pd

var = pd.Series([1,3,2,6,4,7])
print(var)

a =[[1,7,2,8],[5,6,8,9]]

myvar = pd.Series(a, index = ["x", "y"])

print(myvar)
print(myvar["x"])



'''
output -->

0    1
1    3
2    2
3    6
4    4
5    7
dtype: int64
x    [1, 7, 2, 8]
y    [5, 6, 8, 9]
dtype: object
[1, 7, 2, 8]

'''