def count_substring(string, sub_string):
    len_ss = len(sub_string) 
    len_s = len(string)
    c = 0
    
    for i in range(len_s-len_ss+1):
        if string[i:(len_ss+i)] == sub_string.strip() :
            c += 1
    
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)