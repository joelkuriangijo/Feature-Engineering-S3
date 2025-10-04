import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
df = pd.read_csv("measurements.csv")
print("Original Dataset:\n")
print(df)
numeric_cols = ['Height', 'Weight']
X = df[numeric_cols]
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
feature_names = poly.get_feature_names_out(numeric_cols)
df_poly = pd.DataFrame(X_poly, columns=feature_names)
print("\nDataset with Polynomial and Interaction Features:\n")
print(df_poly)
