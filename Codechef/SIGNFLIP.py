t= int(input())

for _ in range(t):
    N,K = [int(x) for x in input().split()] 
    A = [int(x) for x in input().split()] 
    max_in_A = max(A)
    sum = 0
    for i in A:
        if abs(i) >= max_in_A :
            K -= 1
            sum += abs(i)