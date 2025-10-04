import pandas as pd
from sklearn.preprocessing import LabelEncoder


data = {
   'Athlete': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
   'Medal': ['Gold', 'Silver', 'Bronze', 'Silver', 'Gold']
}


df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


le = LabelEncoder()


df['Medal_Encoded'] = le.fit_transform(df['Medal'])
print("\nDataFrame after Label Encoding:")
print(df)
