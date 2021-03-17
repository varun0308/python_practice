import pandas as pd
# Ways to create pandas dataframe

# 1 (Nested array)
myvar = [["Tom",10],["Mark",15],["Tim",13],["Tim",12]]
df = pd.DataFrame(myvar , columns = ["Name","Age"])
print(df)

# 2 (Dictonary + list)
myvar = {
    "Name":["Tom","Mark","Tim","Julia"],
    "Age" : [10,15,13,12]
}

df = pd.DataFrame(myvar)
print(df)

# 3 (List + dictionary)
myvar = [{"Name":"Tom","Age":10},
        {"Name":"Mark","Age":15},
        {"Name":"Tim","Age":13},
        {"Name":"Julia","Age":12}]

df = pd.DataFrame(myvar)
print(df)


'''
All have same output -->

    Name  Age
0    Tom   10
1   Mark   15
2    Tim   13
3  Julia   12

'''