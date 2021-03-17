import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')
print(df.head())

# We can drop any unwanted column as
df1 = df.drop(['Calories'], axis = 1) # Or axis = 1
print(df.head())

# We can concatinate 2 dataframe, column-wise or row-wise
df2 = pd.concat([df1,df['Calories']], axis = 1) # Or axis = 0 for row concatination
print(df2.head())