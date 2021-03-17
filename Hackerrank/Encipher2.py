p = int(input())
list1 = [0]*p
list2 = [0]*p
list3 = [0]*p

q = [int(x) for x in input().split()]

for i in range(p):
    for ii in range(i,-1,-1):
        if q[i] < q[ii]:
            list2[i] = ii+1
            break
        
for i in range(p):
    for ii in range(i,p):
        if q[i] < q[ii]:
            list3[i] = ii+1
            break
        
for i in range(p):
    list1[i] = (list3[i]*list2[i])

print(list2,list3)

print(max(list1))        
