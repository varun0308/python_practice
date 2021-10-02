import typing


t = int(input())

for _ in range(t):
    N,K = [int(x) for x in input().split()] 
    A = [int(x) for x in input().split()] 
    count = 0
    maximum = max(A)
    times = A.count(maximum)
    if times == 1:
        pos_max = A.index(maximum)
        if pos_max >= K-1 :
            count = N-pos_max
    
    else :
        for i in range(N): 
            if A[i] == maximum :
                if i >= K-1 :
                    count += (N-i)
        
    print(count)