'''
NOTE to self : All the basic5 programs are done for the same file.
               They are broken into several pieces for convenience
               Put them together for proper final answer
'''

# Dropping empty cells' rows
import pandas as pd

df = pd.read_csv("D:\Varun\python_practice\pandas_practice\dirtydata.csv")

# dropna() drops all rows with NaN values (no value)
# Sensible to do with very larg dataframe (not until >50 or 100)
new = df.dropna()
print(new.to_string())

# inplace = True overwrites on the original dataframe
df.dropna(inplace = True)
print(df.to_string())

# We can drop specific column empty cells
# Refer basic5.3_clean.py 