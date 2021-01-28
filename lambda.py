# Lambda if similar to a def function
# except, you don't have to return a statement
# It is allso called as anonymous function

lst = [2,6,13,99,54,7,21]

# Assigning a variable to store the lambda
k = lambda x : x>12 
p = lambda x : x*2
# filter always takes a function and a list as input
print(list(filter(k,lst)))

# map always takes a function and a list as input and prints a list(default)
print(list(map(p, lst)))