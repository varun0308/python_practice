t = int(input())

for p in range(t) :
    n = int(input())
    list1 = [int(x) for x in input().split()]
    list2 = (list1.copy()).sort()
    cost_net = 0

    for i in range(n-1):
        k = min(list1[i:])
        for j in range(i,n):
            if k == list1[j] :
                pos = j
        
        cost = pos - i + 1

        cost_net += cost
        list1[i:pos+1] = reversed(list1[i:pos+1])

        if list1 == list2:
            break

    print("Case #{}: {}".format(p+1,cost_net))