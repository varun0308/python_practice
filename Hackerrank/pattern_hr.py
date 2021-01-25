n , m = [int(x) for x in input().split()]

for x in range(n):
    i = x + 1
    if i == (n+1)//2 :
        print("-" * ((m-7)//2) + "WELCOME" + "-" * ((m-7)//2) )
    elif i < (n+1)//2 :
        print("-" * ((m-3*(2*i-1))//2) + (".|." * (2*i-1)) + ("-" * ((m-3*(2*i-1))//2)))
    else :
        print(('.|.' * ((n-i)*2+1)).center(m, "-")) 



# ((n-i)*2-1)