import pandas as pd


df = pd.read_csv("People.csv")
print("Initial Dataset:")
print(df)


outliers = df[df['Height'] > 250]
print("\nOutliers where Height > 250:")
print(outliers)


df.loc[3, 'Height'] = 156
print("\nAfter correcting the specific outlier at index 3:")
print(df)


df.loc[df['Height'] > 250, 'Height'] = 156
print("\nAfter replacing all outliers (>250) with 156:")
print(df)


if 5 in df.index:
   df.drop(5, inplace=True)
   print("\nAfter dropping the outlier at index 5:")
   print(df)


df.drop(df[df['Height'] > 250].index, inplace=True)
print("\nFinal dataset after removing all outliers (>250):")
print(df)
