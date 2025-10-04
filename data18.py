import pandas as pd
# Load dataset from CSV
df = pd.read_csv("data.csv")  # Make sure 'data.csv' is in the working directory
print("Original DataFrame:")
print(df)


# Apply One-Hot Encoding to 'Favorite_Subject' column
df_encoded = pd.get_dummies(df, columns=['Favorite_Subject'])
print("\nDataFrame after One-Hot Encoding:")
print(df_encoded)