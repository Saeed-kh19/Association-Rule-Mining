import pandas as pd
from missing import retail_data_cleaned  # Import the dataset from loading.py

# Remove rows with non-positive Quantity
filtered_by_quantity = retail_data_cleaned[retail_data_cleaned['Quantity'] > 0]

# Remove rows with non-positive UnitPrice
filtered_by_price = filtered_by_quantity[filtered_by_quantity['UnitPrice'] > 0]

rows_removed_due_to_quantity = len(retail_data_cleaned) - len(filtered_by_quantity)
rows_removed_due_to_price = len(filtered_by_quantity) - len(filtered_by_price)
total_rows_removed = len(retail_data_cleaned) - len(filtered_by_price)

print(f"Rows removed due to non-positive quantity: {rows_removed_due_to_quantity}")
print(f"Rows removed due to non-positive unit price: {rows_removed_due_to_price}")
print(f"Total rows removed: {total_rows_removed}")

print("\nFinal cleaned dataset shape:")
print(filtered_by_price.shape)

print("\nRemainin missing values per column:")
print(filtered_by_price.isnull().sum())
