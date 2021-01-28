def calculate_lcm(m,n):
    if m > n:
        m,n = n,m
    lcm = n

    for i in range(1,m+1,1):
        lcm = n*(i)     
        if lcm%m == 0:
            break
    
    return(lcm)
    

def factor_multipication(a,b,c,d,lcm_):
    # finding the factor for numerator multiplication
    p = (lcm_)//c
    q = (lcm_)//d 

    # Changing the numerator
    a = a*p
    b = b*q

    # New nemerator and denominator 
    sum_of_num = a+b
    sum_of_den = lcm_

    # Removing the old values of index [0]
    numarators.remove(a/p)
    denominators.remove(c)

    # Replacing the old values of index [0]
    numarators[0] = sum_of_num
    denominators[0] = sum_of_den

def simplify_fraction(p,q):
    if p>q:
        p,q = q,p

    for i in range(1,p+1):
        if p%i == 0 and q%i ==0:
            hcf = i 
    return hcf


# Input as a list
numarators = [int(x) for x in input().split()]
denominators = [int(x) for x in input().split()]

y = len(numarators)

for _ in range(y-1):
    lcm = calculate_lcm(denominators[0],denominators[1])
    factor_multipication(numarators[0],numarators[1],denominators[0],denominators[1],lcm)

# Simplify fraction here
i = simplify_fraction(numarators[0],denominators[0])

# Prnt final answer
print(f"{numarators[0]//i}/{denominators[0]//i}")

