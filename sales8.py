import pandas as pd




# Read dataset
df = pd.read_csv("sales.csv")
print("Initial Dataset:")
print(df)




# Count the number of sales orders in each region
order_count = df.groupby(['region'])['order_id'].count()
print("\nNumber of sales orders in each region:")
print(order_count)




# Total sales amount for each region
total_sales = df.groupby(['region'])['sales'].sum()
print("\nTotal sales amount for each region:")
print(total_sales)




# Average sales amount per region
average_sales = df.groupby(['region'])['sales'].mean()
print("\nAverage sales amount per region:")
print(average_sales)




# Highest sales amount in each region
max_sales = df.groupby(['region'])['sales'].max()
print("\nHighest sales amount in each region:")
print(max_sales)




# Lowest sales amount in each region
min_sales = df.groupby(['region'])['sales'].min()
print("\nLowest sales amount in each region:")
print(min_sales)
