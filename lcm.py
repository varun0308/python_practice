x ,y = sorted([int(z) for z in input().split()])

if y%x == 0 :
    print(y)

m=y
while(m%x != 0):
    m += y
print(m)    