import pandas as pd

df = pd.read_pickle("0825all_data.pkl")

print(df.head())
print(len(df))