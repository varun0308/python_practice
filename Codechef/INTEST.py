n,k = [int(x) for x in input().split()]

count = 0
for _ in range(n):
    p = int(input())
    if p%3 == 0:
        count += 1

print(count)