n = int(input())

# Empty list
table = []
score_list = []
empty = []
unsorted = []

def repeat_cancel(score_list):
    for i in score_list:
        if i not in empty:
            empty.append(i)


def selection(table):
    for lst in table:
        if lst[1] == k:
            unsorted.append(lst[0])

    order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in order:
        for j in unsorted :
            if i == j[0]:
                print(j)

for i in range(n):
    # Taking input
    name = input()
    score = float(input())
    # Appending [name,score] into the empty table
    # The [] is necessary (creating a list inside a list)
    table.append([name,score])

    # Appending score into score_list
    score_list.append(score)

a = sorted(score_list )
repeat_cancel(a)

k = empty[1]

selection(table)
