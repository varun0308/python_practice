numbers= ['2','5','7','1','9','8','-1','14']

greatest=0
for g in numbers:
    if int(g)>int(greatest):
        greatest=g

print('The greatest number is '+greatest)