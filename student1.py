import pandas as pd


# Load dataset
df = pd.read_csv("student.csv")
print("Original Dataset:\n", df)


# Remove rows by index
df_drop_index = df.drop([0,2])
print("\nAfter removing rows at index 0 and 2:\n", df_drop_index)


# Remove rows with Marks > 90
df_filtered = df[df['Mark'] <= 90]
print("\nAfter removing rows with Marks > 90:\n", df_filtered)


# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\nAfter removing duplicates:\n", df_no_duplicates)


# Remove a range of rows
df_range_removed = df.drop(df.index[1:3])
print("\nAfter removing rows index 1 to 2:\n", df_range_removed)


# Remove rows with NaN
df_no_nan = df.dropna()
print("\nAfter removing rows with NaN:\n", df_no_nan)
