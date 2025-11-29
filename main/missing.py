import pandas as pd
from loading import retail_data

missing_values_summary = retail_data.isnull().sum()
print("Missing values per column:")
print(missing_values_summary)

retail_data_cleaned = retail_data.dropna(subset=['Description'])

print("\nAfter cleaning 'Description':")
print(retail_data_cleaned.isnull().sum())

rows_removed = len(retail_data) - len(retail_data_cleaned)
print(f"\nTotal rows removed due to missing 'Description': {rows_removed}")