import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# --- 1. Load and Prepare the Data ---
# Read the dataset (ensure the CSV file is in your working directory)
df = pd.read_csv('iris.csv')


# Display the first few rows
print("Original Data:")
print(df.head())


# Define feature columns and target column
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
target = 'Species'


# Separate features (X) and target (Y)
x = df.loc[:, features].values  # Feature values
y = df.loc[:, [target]].values  # Target values


# --- 2. Standardize the Data ---


# PCA works best when data is standardized (mean = 0, variance = 1)
x = StandardScaler().fit_transform(x)


print("\nStandardized Data (First 5 Rows):")
print(pd.DataFrame(data=x, columns=features).head())


# --- 3. PCA Projection to 2D ---


# Create PCA object with 2 principal components
pca = PCA(n_components=2)


# Fit and transform the standardized data
principalComponents = pca.fit_transform(x)


# Create a DataFrame for the principal components
principalDf = pd.DataFrame(principalComponents,
                          columns=['Principal Component 1', 'Principal Component 2'])


# Combine with the target variable
finalDf = pd.concat([principalDf, df[[target]]], axis=1)
print("\nFinal Data (PCA + Target - First 5 Rows):")
print(finalDf.head())


# --- 4. Visualize 2D PCA Projection ---


plt.figure(figsize=(8, 8))
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_title('2-Component PCA of Iris Dataset')


# Define target classes and colors
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']


# Plot each class in different color
for target_name, color in zip(targets, colors):
   indicesToKeep = finalDf['Species'] == target_name
   ax.scatter(finalDf.loc[indicesToKeep, 'Principal Component 1'],
              finalDf.loc[indicesToKeep, 'Principal Component 2'],
              c=color, s=50, label=target_name)


ax.legend()
ax.grid()
plt.show()


# --- 5. Variance Explained ---


# Show the proportion of variance explained by each component
print("\nVariance Explained Ratio:")
print(pca.explained_variance_ratio_)


# Display total variance explained
print("Total Variance Explained by 2 Components: {:.2f}%".format(sum(pca.explained_variance_ratio_) * 100))

#Above code is reformatted version of below code due to indentation error
'''import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# --- 1. Load the Dataset ---
# Make sure iris.csv is in the same folder or provide full path
df = pd.read_csv('iris.csv')

print("Original Data:")
print(df.head())

# --- 2. Prepare Features and Target ---
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
target = 'Species'

x = df.loc[:, features].values
y = df.loc[:, [target]].values

# --- 3. Standardize the Data ---
x = StandardScaler().fit_transform(x)

print("\nStandardized Data (First 5 Rows):")
print(pd.DataFrame(data=x, columns=features).head())

# --- 4. PCA Projection to 2D ---
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(principalComponents, 
                           columns=['Principal Component 1', 'Principal Component 2'])

finalDf = pd.concat([principalDf, df[[target]]], axis=1)

print("\nFinal Data (PCA + Target - First 5 Rows):")
print(finalDf.head())

# --- 5. Visualize 2D PCA Projection ---
fig, ax = plt.subplots(figsize=(8, 8))  # <-- define ax

ax.set_xlabel('Principal Component 1', fontsize=12)
ax.set_ylabel('Principal Component 2', fontsize=12)
ax.set_title('2-Component PCA of Iris Dataset', fontsize=15)

# Define target classes and colors
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']

for target_name, color in zip(targets, colors):
    indicesToKeep = finalDf['Species'] == target_name
    ax.scatter(finalDf.loc[indicesToKeep, 'Principal Component 1'],
               finalDf.loc[indicesToKeep, 'Principal Component 2'],
               c=color, s=50, label=target_name)

ax.legend()
ax.grid()
plt.show()

# --- 6. Variance Explained ---
print("\nVariance Explained Ratio:")
print(pca.explained_variance_ratio_)

print("Total Variance Explained by 2 Components: {:.2f}%".format(
    sum(pca.explained_variance_ratio_) * 100))'''
