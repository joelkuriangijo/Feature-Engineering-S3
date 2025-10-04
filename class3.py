import pandas as pd

# Load dataset
df = pd.read_csv("class.csv")
print("Original Dataset:\n", df)

# Fill missing values with 0
df_fill0 = df.fillna(0)
print("\nDataset after filling missing values with 0:\n", df_fill0)

# Replace Age NaN with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nAfter filling missing Age with mean:\n", df)

# Replace Height NaN with median
df["Height"] = df["Height"].fillna(df["Height"].median())
print("\nAfter filling missing Height with median:\n", df)

# Replace Grade NaN with mode
df["Grade"] = df["Grade"].fillna(df["Grade"].mode()[0])
print("\nAfter filling missing Grade with mode:\n", df)

# Forward Fill
df_ffill = df.ffill()
print("\nDataset after Forward Fill:\n", df_ffill)

# Backward Fill
df_bfill = df.bfill()
print("\nDataset after Backward Fill:\n", df_bfill)
