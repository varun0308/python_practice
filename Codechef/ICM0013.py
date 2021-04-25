t = int(input())

for _ in range(t):
    n = int(input())

    array = [int(x) for x in input().split()]
    print(array)
    sort_array = sorted(array)

    if array == sort_array :
        print("YES")
        print(0)
        
    else :
        a = min(array)
        b = max(array)
        c = array.index(b) + 1
        array1 = array[c:] + array[:c]
        
        if array1 == sort_array :
            print("YES")
            print(1)
        else :
            print("NO")