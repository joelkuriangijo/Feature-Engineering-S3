# Experiment: Histogram of Class Marks for Different Subjects
import pandas as pd
import matplotlib.pyplot as plt


# Sample data for one class
data = {
   'Physics': [78, 82, 88, 90, 72, 85, 80, 79, 86, 91],
   'Chemistry': [70, 68, 80, 75, 65, 85, 78, 72, 74, 82]
}
# Create DataFrame
df = pd.DataFrame(data)

# Plot histograms
plt.figure(figsize=(10,5))
plt.hist(df['Physics'], bins=8, alpha=0.6, color='green', edgecolor='black', label='Physics')
plt.hist(df['Chemistry'], bins=8, alpha=0.6, color='orange', edgecolor='black', label='Chemistry')
# Add title and labels
plt.title("Distribution of Marks in Different Subjects")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y')
plt.show()
