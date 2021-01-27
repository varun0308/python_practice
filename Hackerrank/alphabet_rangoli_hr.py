Order = "abcdefghijklmnopqrstuvwxyz"
    
def print_rangoli(s):
    if s == 1 :
        print("a")
    
    else :
        lst = list(Order[s-1].center(4*s-3,"-"))
        print("".join(lst))

        for i in range(2*s-3):
            if i < s-1 :
                lst1 = lst[2:2*s-1]
                lst1.append("-")
                lst1.append(Order[s-2-i])
                l = lst1[0:2*s]
                lst1.reverse()
                l.extend(lst1[1:])
                lst = l
                print("".join(l))

            else :

                lst1 = lst[0:2*s-2] + lst[2*s+2 :]
                lst1.append("-") ; lst1.append("-")
                lst1.insert(0,"-") ; lst1.insert(0,"-")
                print("".join(lst1))
                lst = lst1

        lst = list(Order[s-1].center(4*s-3,"-"))
        print("".join(lst))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


