t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = {}
    for i in range(n):
        if a[i] not in count :
            count[a[i]] = 1
        else :
            count[a[i]] += 1
    
    value = list(count.values())

    pairs = 0  
    for i in range(len(value)):
        pairs += value[i]*(sum(value[i+1:]))
            
    print(2*pairs)