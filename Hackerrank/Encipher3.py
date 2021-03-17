p = int(input())
q = [int(x) for x in input().split(" ")]
lst = []

q.sort()
for i in q:
    if i not in lst:
        lst.append(i)

print(lst)

lst2 = [0]*(len(lst))

for i in range(len(lst)):
    for j in range(len(q)):
        if lst[i] == q[j]:
            lst2[i] += 1

print(lst2)

k = max(lst2)
print(len(q) - k)