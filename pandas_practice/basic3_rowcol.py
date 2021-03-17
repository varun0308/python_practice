import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

# loc gets the contents of that row
# This is the only way I've seen so far :)
print(df.loc[2])

# Gets the column with name calories
print(df.calories)


'''
output-->

calories    390
duration     45
Name: 2, dtype: int64
0    420
1    380
2    390
Name: calories, dtype: int64
'''