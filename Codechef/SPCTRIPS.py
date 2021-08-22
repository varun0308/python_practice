t = int(input())

for _ in range(t):
    N = int(input())
    count = 0
    for i in range(1,N+1):
        for n in range(2,(N+1)//i + 1):
            if i*n <= N :
                count += (N-i)//(i*n) + 1
                continue
            break    
    print(count)