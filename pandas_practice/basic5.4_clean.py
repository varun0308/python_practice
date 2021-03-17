import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')

# Boolean result only
print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df)


# Combine all basic5 to get completely cleaned/preprocessed data