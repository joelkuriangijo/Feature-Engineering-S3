import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
plt.figure(figsize=(10,6))
plt.hist(df['Marks'], bins=8, color='blue', edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
