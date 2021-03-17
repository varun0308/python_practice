import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')

# Gives the first 10 rows
print(df.head(10))

# Gives first 5 rows (default) 
print(df.head())

# Gives last 5 rows (default) 
print(df.tail()) 

# Gives basic info about that dataframe
print(df.info())