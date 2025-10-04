import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Load the CSV file
df = pd.read_csv("medals.csv")
print("Original DataFrame:")
print(df)


# Initialize the LabelEncoder
le = LabelEncoder()


# Fit and transform the 'Medal' column
df['Medal_Encoded'] = le.fit_transform(df['Medal'])
print("\nDataFrame after Label Encoding:")
print(df)