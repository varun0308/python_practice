s = input()
lst = [0,0,0,0,0]

for i in s :
    if i.isalnum() :
        lst[0] = 1

    if i.isalpha() :
        lst[1] = 1

    if i.isdigit() :
        lst[2] = 1

    if i.islower() :
        lst[3] = 1

    if i.isupper() :
        lst[4] = 1

for i in lst:
    if i :
        print(True)
    else :
        print(False)
