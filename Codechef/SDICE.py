t = int(input())

def max_sum_topmost(n):
    if n%4 == 0 :
        top_sum = 60
    elif n%4 == 1 :
        top_sum = 76
    elif n%4 == 2 :
        top_sum = 88
    else :
        top_sum = 99
    
    return top_sum


for _ in range(t):
    n = int(input())
    
    if n>4 :
        k = (n//4) - 1
        total_sum = (44*k) + max_sum_topmost(n)

    else :
        if n == 1:
            total_sum = 20
        elif n == 2 :
            total_sum = 36
        elif n == 3 :
            total_sum = 51
        else :
            total_sum = 60

    print(total_sum)