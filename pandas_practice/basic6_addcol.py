import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')

x = [2]*32

# Telling add the column named 'clusters', 
# which has values of x
df['clusters'] = x

print(df)
