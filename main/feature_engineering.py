import pandas as pd
from invalid_records import filtered_by_price

filtered_by_price['TotalAmount'] = filtered_by_price['Quantity'] * filtered_by_price['UnitPrice']

print("\nFirst 5 rows with TotalAmount:")
print(filtered_by_price[['Quantity','UnitPrice','TotalAmount']].head())

invalid_total_count = (filtered_by_price['TotalAmount'] <= 0 ).sum()
print(f"\nNumber of rows with non-positive TotalAmount: {invalid_total_count}")