import math

s = [x for x in input().split()]
string = "".join(s)
k = len(string)
row = int(math.floor(math.sqrt(k)))

if (k == 1 or 4 or 9 or 16 or 25 or 36 or 49 or 81):
    col = row 
else:
    col = row + 1

list1 = []

if col*row < k:
    row += 1

for i in range(0,k,col):
    list1.append(string[i:i+col]) 

list1[-1] += " "*(col-len(list1[-1]))

for i in range(col):    
    for j in range(row):    
        print(list1[j][i] , end = "")
    if(list1[j][i] != " "):
        print(" ",end = "")   

