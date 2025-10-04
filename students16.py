import pandas as pd
import matplotlib.pyplot as plt


# Sample dataset
data = {
   'Name': ['Amal', 'Bijo', 'Charlie', 'Devika', 'Edvin', 'Farah', 'George'],
   'Marks': [95, 88, 95, 78, 82, 91, 67]
}


df = pd.DataFrame(data)
print("Original Dataset:\n", df)


#Apply Equal-Frequency (Quantile) Binning (3 bins)
df['Marks_Quantile_Bin'] = pd.qcut(df['Marks'], q=3, labels=['Low', 'Medium', 'High'])


print("\nDataset with Equal-Frequency Bins:\n", df)


#Optional histogram to visualize bins
plt.figure(figsize=(6,4))
plt.hist(df['Marks'], bins=7, color='lightgreen', edgecolor='black')
plt.title('Histogram of Marks (for Equal-Frequency Binning)')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
