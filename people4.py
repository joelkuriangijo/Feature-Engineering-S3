import pandas as pd


# Load and display the dataset
df = pd.read_csv("people.csv")
print("Original Dataset:")
print(df)


# Remove all duplicate rows (keep first by default)
df_no_duplicates = df.drop_duplicates()
print("\nDataset after removing all duplicate rows (keep='first'):")
print(df_no_duplicates)


# Remove duplicates but keep the last occurrence
df_keep_last = df.drop_duplicates(keep='last')
print("\nDataset after removing duplicates (keep='last'):")
print(df_keep_last)


# Remove duplicates based on a specific column, e.g., "Gender"
df_gender_unique = df.drop_duplicates(subset=['Gender'])
print("\nDataset after removing duplicates based on 'Gender':")
print(df_gender_unique)