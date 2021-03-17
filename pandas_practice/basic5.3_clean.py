# Changing date format
import pandas as pd

df = pd.read_csv('D:\Varun\python_practice\pandas_practice\dirtydata.csv')

# .to_datetime() method converts into date format yyyy/mm/dd
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# Remove the NaT (Not a Time) row
# subset = [] specifies the column, no other column will be checked.
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

# Changes 8th (7th index) in duration column
# loc gets contents of that row
df.loc[7, 'Duration'] = 45