t = int(input())
    
for _ in range(t) :
    N,X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    
    XOR_dict = {}
    count = {}

    for i in A :
        operation = i^X

        if operation in XOR_dict.keys() :
            XOR_dict[operation] += 1
        else :
            XOR_dict[operation] = 1

        if i in count.keys() :
            count[i] += 1
        else :
            count[i] = 1
 
    max_number_of_int = 0
    min_number_of_operations = N

    print(count)
    print(XOR_dict)
    
    for i in XOR_dict :
        if i in list(count.keys()) :
            if min_number_of_operations > XOR_dict[i]:
                min_number_of_operations = XOR_dict[i]

            if max_number_of_int < (count[i] + XOR_dict[i]) :
                max_number_of_int = count[i] + XOR_dict[i]

    print(max_number_of_int,min_number_of_operations) if max_number_of_int != 0 else print(max(count.values()),0)  