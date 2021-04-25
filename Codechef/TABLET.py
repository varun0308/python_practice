test_case = int(input())

for _ in range(test_case):
    n, b = [int(x) for x in input().split()]
    max_area = 0
    for __ in range(n):
        l, h, p =  [int(x) for x in input().split()]
        if p <= b and l*h > max_area:
            max_area = l*h

    if max_area > 0:
        print(max_area)
    else :
        print("no tablet")