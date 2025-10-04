import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
# Sample dataset
data = {
   'Height': [168, 172, 180, 160, 175, 165, 182],
   'Weight': [62, 70, 78, 55, 68, 60, 85]
}


df = pd.DataFrame(data)
print("Original Dataset:\n", df)


poly = PolynomialFeatures(degree=2, include_bias=True)


poly_features = poly.fit_transform(df)


feature_names = poly.get_feature_names_out(df.columns)


df_poly = pd.DataFrame(poly_features, columns=feature_names)
print("\nPolynomial and Interaction Features:\n", df_poly)


