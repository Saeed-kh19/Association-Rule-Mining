import pandas as pd
from invalid_records import filtered_by_price

filtered_by_price['InvoiceDate'] = pd.to_datetime(filtered_by_price['InvoiceDate'], errors='coerce')

print("\nData types after conversion:")
print(filtered_by_price.dtypes)


invalid_dates_count = filtered_by_price['InvoiceDate'].isna().sum()
print(f"\nNumber of rows with invalid InvoiceDate after conversion: {invalid_dates_count}")

