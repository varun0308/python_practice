n = int(input())

list_ = []
# Input as a list
list_ = [int(x) for x in input().split()]

#Defining an empty list
new = []

#No repeatation condition
for l in list_:
    if l not in new:
        new.append(l)

a = (sorted(new, reverse = True) )
print(a[1])

'''
lst = [] 
  
n = int(input()) 
  
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
'''