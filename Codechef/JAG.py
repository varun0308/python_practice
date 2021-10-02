t = int(input())

for _ in range(t):
    N = int(input())
    W = [int(x) for x in input().split()]
    connected_components = N
    for i in range(N) :
        if 