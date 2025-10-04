# Experiment 10: Data Analysis – Boxplots using Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("students.csv")


plt.figure(figsize=(4,5))
sns.boxplot(y='Marks', data=df, color='red')
plt.title("Marks Outlier Detection")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
