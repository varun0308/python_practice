def solve(a):
    lst = []
    print(a)
    for i in range(a-1):
        j = i+1
        if a%j == 0:
            lst.append(j)
    print(lst)
    k = sum(lst)
    if k == a:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)