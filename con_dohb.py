dict_ = { 10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
g =""

# 10    12     A  1010
def convert_to_octal(a):
    p = str(a//8)
    q = str(a%8)
    if a<8:
        return(a)
    elif a>7 and a<80: 
        if int(q) == 0:
            return(p+'0') 
        else :
            return(p+q)
    else :
        if int(q) == 0:
            return(str(p)+'0') 
        else :
            return(p+q)

def convert_to_hex(a):
    r = str(a%16)
    s = str(a//16)
    if a<16:
        if a<10:
            return(a)
        else :
            return(dict_[a])
    elif a>15 :
        if int(r) == 0:
            return(s+'0') 
        elif int(r) >= 10 :
            return(s+dict_[r])
        else :
            return(s+r)

def convert_to_binary(a,g):
    if a%2 != 0:
        while(a!=1):
            h = a%2
            a = a//2
            g += str(h)
    else :
        while(a!=0):
            h = a%2
            a = a//2
            g = str(h) + g
    if a ==1:
        g += "1"  
    
    return(g)

k = int(input())

z = convert_to_binary(k,g)
l = int(len(z))

for j in range(k):
    i = j+1
    x = convert_to_octal(i) 
    y = convert_to_hex(i)
    z = convert_to_binary(i,g)
    
    print('%s %ls %ls %ls' % (i,x,y,z))
