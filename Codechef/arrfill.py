def find_max(arr, sum, x, y):
    N = len(arr)
    newsum = (N - N//y) * x

    # return max(find_max(arr, sum+newsum, x2, y2), find_max(arr, sum, x2, y2))

t = int(input())

for _ in range(t):
    N,M = [int(x) for x in input().split()]
    list_operation = []
    for __ in range(M):
        list_operation.append([int(x) for x in input().split()])
    print(list_operation)