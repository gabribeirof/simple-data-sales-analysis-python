import pandas as pd

# 1. Load the data
df = pd.read_csv('sales_data.csv')

# 2. Basic Data Cleaning & Exploration
print("--- First 5 rows of the dataset ---")
print(df.head())

# 3. Data Processing: Calculate total revenue per category
category_revenue = df.groupby('category')['revenue'].sum().reset_index()

print("\n--- Total Revenue by Category ---")
print(category_revenue)

# 4. Find the most expensive product sold
expensive_product = df.loc[df['price'].idxmax()]
print(f"\nMost expensive product sold: {expensive_product['product']} at ${expensive_product['price']}")

# 5. Exporting the result to a new CSV (Small ETL process)
category_revenue.to_csv('category_report.csv', index=False)
print("\nReport generated successfully as 'category_report.csv'")