# Filling NaN values

import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')

df1 = df["Calories"].fillna(130)
# or df.Calories = df["Calories"].fillna(130)
print(df1.to_string())

# Can fill in values of mean, median or mode of that column into the empty cell.
x = df["Calories"].mean()
y = df["Calories"].median()
print(x,y)

df2 = df["Calories"].fillna(x)
print(df2.to_string())

df3 = df["Calories"].fillna(y)
print(df3.to_string())

# If you want entire dataframe, use inplace = True and print that