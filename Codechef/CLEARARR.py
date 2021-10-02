t = int(input())

for _ in range(t):
    N,K,X = [int(x) for x in input().split()] 
    sequence = [int(x) for x in input().split()]
    sequence.sort()
    cost = sum(sequence[0:N-2*K])

    if K>0:
        for i in range(N-2*K,N,2):
            total = sequence[i]+sequence[i+1]
            cost += min(total,X)
    else:
        cost += sum(sequence[N-2*K:])

    print(cost) 