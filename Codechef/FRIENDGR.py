t = int(input())

for _ in range(t):
    N,K = [int(x) for x in input().split()]
    S = input()
    S_dup = ""
    compare = '1'+'0'*K+'1'
    if K == 0:
        count = 0
        for i in S:
            count += 1
        print(count)
    else:
        j = 0
        for i in range(1,len(S)):
            if int(S[i-1:i+K+1]) == int(compare) :
                S_dup += S[j:i] + '1'
                print("dup: ",S_dup)
                j = i+K+1

