t = int(input())

for _ in range(t) :
    n,k = [int(x) for x in input().split(" ")]
    s = input()
    s1 = "*"*k
    count = True

    for i in range(n-k+1) :
        if s[i] == "*" and s[i:i+k] == s1:
            print("YES")
            count = False
            break
    if count :
        print("NO")