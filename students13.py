import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("students.csv")


# Pivot table (Dept vs Name with Marks)
pivot_marks = df.pivot_table(index='Dept', columns='Name', values='Marks')


# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(pivot_marks, annot=True, fmt='g', cmap='YlOrRd', linewidths=0.5)
plt.title('Heatmap of Marks by Department and Student')
plt.xlabel('Student Name')
plt.ylabel('Department')
plt.show()