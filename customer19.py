import pandas as pd
# Load dataset from CSV
df = pd.read_csv("customer.csv")  # Make sure 'data.csv' is in the working directory
print("Original DataFrame:")
print(df)
# Apply One-Hot Encoding to 'Category' and 'Gender' columns
df_encoded = pd.get_dummies(df, columns=['Category', 'Gender'])
print("\nDataFrame after One-Hot Encoding:")
print(df_encoded)
