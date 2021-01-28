# Original list
numbers = [6,0,8,5,0,1,9,7,3,3,8,2,0,1,3,9,7,6]

# New empty list
new=[]


for x in numbers:
    if x not in new:
        # new.append(x) puts the element x in new empty list 
        new.append(x)
        
print(new)

##############################################################
# New set declared
new = set([])

# All repeatative elements are ignored    
for x in numbers:
    new.add(x)

# Set orders the list
print(list(new))