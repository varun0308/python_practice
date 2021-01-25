def split_and_join(line):
    split_ = line.split(' ')
    print(split_)
    k = "-".join(split_)
    return k
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)