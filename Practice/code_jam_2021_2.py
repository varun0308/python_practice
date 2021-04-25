t = int(input())

for p in range(t):
    x , y , string = input().split(" ")
    string = string.replace('?', '')
    string1 = ""
    cost = 0

    if string == "" :
        print("Case #{}: {}".format((p+1),0))
        continue

    string1 += string[0]
    
    for i in range(1,len(string)):
        if string[i] != string[i-1]:
            string1 += string[i] 


    for i in range(0,(len(string1)-1)):
        if string1[i] == 'C' and string1[i+1] == 'J' :
            cost += int(x) 
        elif string1[i] == 'J' and string1[i+1] == 'C':
            cost += int(y)

    print("Case #{}: {}".format((p+1),cost))

    