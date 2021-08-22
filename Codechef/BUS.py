t = int(input())

for _ in range(t):
    N,M,Q = [int(x) for x in input().split()] 
    seq = []
    flag = 0
    in_bus = 0
    for __ in range(Q):
        ch,i = [x for x in input().split()]
        if ch == '+':
            in_bus += 1
            seq.append(int(i))
        else :
            in_bus -= 1
        if ch == '-' and int(i) not in seq and flag == 0:
            flag = 1
        if in_bus > M and flag == 0:
            flag = 1
    if flag == 0:
        print("Consistent")
    else:
        print("Inconsistent")