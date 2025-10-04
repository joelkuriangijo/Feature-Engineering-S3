import pandas as pd
import matplotlib.pyplot as plt
data = {
   'Name': ['Amal', 'Bijo', 'Charlie', 'Devika', 'Edvin', 'Farah', 'George'],
   'Marks': [95, 88, 95, 78, 82, 91, 67]
}
df = pd.DataFrame(data)
print("Original Dataset:\n", df)
# Equal Width Binning (3 bins)
df['Marks_Bin'] = pd.cut(df['Marks'], bins=3, labels=['Low', 'Medium', 'High'])
print("\nDataset with Equal-Width Bins:\n", df)

# histogram to visualize bins
plt.figure(figsize=(6,4))
plt.hist(df['Marks'], bins=3, color='skyblue', edgecolor='black')
plt.title('Histogram of Marks (Equal-Width Bins)')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
