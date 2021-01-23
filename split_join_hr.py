def split_and_join(line):
    split_and_join = line.split(' ')
    k = "-".join(split_and_join)
    return k
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)