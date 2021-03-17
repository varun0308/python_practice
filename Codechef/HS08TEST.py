withdraw, amount = [float(x) for x in input().split()]


if ((withdraw%5 == 0) and (withdraw < amount)):
    print("%.2f"%(amount - withdraw - 0.50))
else :
    print(amount)
