def sorting(sample):
    order = "abcdefghijklmnopqrstuvwxyz\
             ABCDEFGHIJKLMANOPQRSTUVWXYZ1357902468"

    for i in order:
        for j in sample:
            if i == j :
                print(j, end='')


sample = input()

sorting(sample)
