area_required = int(input())

if area_required == 1 :
    a,b,c = [float(x) for x in input().split(" ")]
    s = (a+b+c)/2
    area = s**2

elif area_required == 2 :
    a,b = [float(x) for x in input().split(" ")]
    area = a*b

print("%0.2f"%area)