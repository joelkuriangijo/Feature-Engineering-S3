import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. GENERATE HIGHLY RIGHT-SKEWED RANDOM DATASET
# Use exponential distribution and scale to 50–500
np.random.seed(42) # for reproducible results
data = np.random.exponential(scale=50, size=1000)
df = pd.DataFrame({'Distance': data})
# Display original data
print("Original DataFrame:")
print(df)


# 2. APPLY LOGARITHMIC TRANSFORMATION
df['Log_Distance'] = np.log(df['Distance'])


# Display transformed data
print("\nDataFrame after Logarithmic Transformation:")
print(df)


# 3. VISUALIZE ORIGINAL AND LOG-TRANSFORMED DISTRIBUTION SIDE BY SIDE
plt.figure(figsize=(12,5))


# Original Distance Histogram
plt.subplot(1,2,1)
plt.hist(df['Distance'], bins=10, color='skyblue', edgecolor='black')
plt.title('Figure 1: Original Distance Distribution (Highly Right-Skewed)')
plt.xlabel('Distance (meters)')
plt.ylabel('Frequency')


# Log-Transformed Distance Histogram
plt.subplot(1,2,2)
plt.hist(df['Log_Distance'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Figure 2: Log-Transformed Distance Distribution (Reduced Skewness)')
plt.xlabel('Log(Distance)')
plt.ylabel('Frequency')


plt.tight_layout()
plt.show()
