import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# Load dataset
df = pd.read_csv("class.csv")
print("Original Dataset:\n")
print(df)


# Columns to normalize
numeric_cols = ['Height', 'Weight']

scaler = MinMaxScaler()
df_minmax = df.copy()
df_minmax[numeric_cols] = scaler.fit_transform(df[numeric_cols])


print("\nMin-Max Normalized Dataset:\n")
print(df_minmax)