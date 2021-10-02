t = int(input())

for _ in range(t):
    N = int(input())
    A = [int(x) for x in input().split()] 
    A.reverse()
    count = 0
    previous = A[0]
    index = 0

    for i in range(1,N):
        if A[i] >= A[i-1] :
            if A[i] > previous :
                count += 1
                previous = A[i]
                index = i
    
    if previous != A[N-1]:
        print(-1)
    elif previous == A[N-1] and index != N-1:
        print(count+1)
    else :
        print(count)
    