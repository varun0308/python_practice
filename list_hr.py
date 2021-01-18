n = int(input())
emp = []

for _ in range(n):
    l = [x for x in input().split()]

    if l[0] == 'insert' :
        emp.insert(int(l[1]), int(l[2]))

    elif l[0] == 'print' :
        print(emp)

    elif l[0] == 'remove' :
        emp.remove(int(l[1]))
    
    elif l[0] == 'append' :
        emp.append(int(l[1]))

    elif l[0] == 'sort' :
        emp.sort()

    elif l[0] == 'pop' :
        emp.pop()

    elif l[0] == 'reverse' :
        emp.reverse()
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.