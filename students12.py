# Experiment 10: Data Analysis – Grouped Boxplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
plt.figure(figsize=(6,5))
sns.boxplot(x="Dept", y="Marks", data=df)
plt.title("Marks Distribution Across Departments")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
