def print_rangoli(s):
    order = "abcdefghijklmnopqrstuvwxyz"
    k = order[s-1]
    
    for i in range(2*s-1):
        print(k.center(s*s,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)