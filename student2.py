import pandas as pd


# Load dataset
df = pd.read_csv("student.csv")
print("Original Dataset:\n", df)


# Remove columns by label
df_drop_label = df.drop(columns=['Dept','Grade'])
print("\nAfter dropping Dept and Grade:\n", df_drop_label)


# Remove columns by index
df_drop_index = df.drop(df.columns[[1,4]], axis=1)
print("\nAfter dropping columns at index 1 and 4:\n", df_drop_index)


# Remove range of columns
df_drop_range = df.drop(df.columns[0:2], axis=1)
print("\nAfter removing columns index 0 to 1:\n", df_drop_range)


# Remove column using del
del df['Mark']
print("\nAfter deleting 'Mark' column:\n", df)


# Remove column using pop()
dept_col = df.pop('Dept')
print("\nRemoved 'Dept' column using pop():\n", dept_col)
print("\nRemaining DataFrame:\n", df)