import pandas as pd


# Load and display the dataset
df = pd.read_csv("People.csv")
print("Initial Dataset:")
print(df)


# Convert Gender column from 0/1 to M/F using for loop
for x in df.index:
   if df.loc[x, "Gender"] == "1":
       df.loc[x, "Gender"] = "M"
   elif df.loc[x, "Gender"] == "0":
       df.loc[x, "Gender"] = "F"


# Standardize City column by converting all values to lowercase
df["City"] = df["City"].str.lower()


print("\nAfter Standardization:")
print(df)
