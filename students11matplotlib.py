#Matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("students.csv")


# Boxplot for Marks
plt.figure(figsize=(4,5))
plt.boxplot(df['Marks'], labels=['Marks'])
plt.title("Marks Outlier Detection")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


