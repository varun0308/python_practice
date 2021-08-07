def return_multiple_value(p,q,r):
    p += 1
    q += 1
    r += 1

    return (p,q,r)

a,b,c = [int(x) for x in input().split(" ")]

a,b,c = return_multiple_value(a,b,c)
print(a,b,c)