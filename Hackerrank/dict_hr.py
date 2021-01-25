n = int(input())

# Empty dictionary
name_scores = {}

for _ in range(n):  # -------> This line loops the input the "line" number of times
    # Input directly into name, s1, s2, s3.
    name , s1, s2, s3 = [x for x in input().split()]
    
    # Putting into dictionary as {name : [s1, s2, s3]}
    name_scores[name] = [float(s1) , float(s2) , float(s3)]

required = input()

# Sum of the list of the required name's average
a = sum(name_scores[required])
print(('%.2f'%(a/3)))