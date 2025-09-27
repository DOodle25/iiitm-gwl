import pandas as pd 
import numpy as np

df = pd.read_csv('./ML/archive/Housing.csv')

df.to_excel('./ML/Housing.xlsx', index=False)
df.to_json('./ML/Housing.json', index=False)

print(df.head())
print(df.tail(7))
print(df.describe())
print(df.isnull().sum())
print(df.select_dtypes(include=[np.number]).corr())

