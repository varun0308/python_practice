import itertools

def simplest_palindrome(number):
    length = len(number)
    if length%2 == 0:
        number_1 = number[0:length//2:] + number[(length//2)-1::-1]
    else :
        number_1 = number[0:(length//2)+1:] + number[(length//2)-1::-1]

    return number_1
        

t = int(input())

for _ in range(t):
    k = str(input()).strip()
    l = len(k)

    number = simplest_palindrome(k)
    if int(number) > int(k) :
        print(number)
        continue

    else :
        inc = 1
        if l%2 == 0 :
            for i in range(l//2 - 1,0,-1):
                k_new = k[0:i:] + str(((int(k[i]) + inc))%10) + k[i+1::]
                inc = (int(k[i]) + inc) // 10
                if inc == 0:
                    break
        else :
            for i in range(l//2 ,0,-1):
                k_new = k[0:i:] + str(((int(k[i]) + inc))%10) + k[i+1::]
                inc = (int(k[i]) + inc) // 10
                if inc == 0:
                    break

        print(simplest_palindrome(k_new))