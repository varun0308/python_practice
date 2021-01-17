# Original list
numbers = [6,9,8,5,0,1,9,7,3,3,8,2,0,1,3,9,7,6]

# New empty list
new=[]


for x in numbers:
    if x not in new:
        # new.append(x) puts the element x in 
        # new empty list 
        new.append(x)
        
print(new)
