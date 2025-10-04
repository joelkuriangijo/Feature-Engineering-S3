import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("students.csv")
print("Dataset:\n", df)


# Select numeric columns
numeric_cols = ['Marks', 'Height', 'Weight']
df_numeric = df[numeric_cols]


# Compute correlation matrix
corr_matrix = df_numeric.corr()
print("\nCorrelation Matrix:\n", corr_matrix)


# Visualize correlation matrix
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
