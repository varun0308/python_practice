t = int(input())

for _ in range(t):
    N,p,K = [int(x) for x in input().split()]
    
    total = N//K
    remain = N%K
    pos = p%K
    total_days = total*(pos)
    total_days += p//K + 1
    
    if remain<pos :
            total_days += remain
    else :
        total_days += pos
    print(total_days)