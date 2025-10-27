import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the dataset
df = pd.read_csv('cabin_class.csv')
print("Original Dataset:\n", df, "\n")

# -------- Label Encoding --------
label_encoder = LabelEncoder()
df['Cabin_Label'] = label_encoder.fit_transform(df['Cabin_Class'])
print("After Label Encoding:\n", df[['Passenger_ID', 'Cabin_Class', 'Cabin_Label']], "\n")

# -------- One-Hot Encoding --------
onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(df[['Cabin_Class']])
encoded_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['Cabin_Class']))

# Combine original and encoded data
final_df = pd.concat([df, encoded_df], axis=1)
print("After One-Hot Encoding:\n", final_df[['Passenger_ID', 'Cabin_Class'] + list(encoded_df.columns)], "\n")

# -------- Comparison --------
print("👉 Label Encoding gives each category a number (C1=0, C2=1, ...)")
print("👉 One-Hot Encoding creates separate columns for each category (1 if present, else 0)")
