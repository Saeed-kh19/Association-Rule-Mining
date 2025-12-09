import pandas as pd
from feature_engineering import filtered_by_price

date_for_timeseries = filtered_by_price.copy()

date_for_timeseries['InvoiceDate'] = pd.to_datetime(date_for_timeseries['InvoiceDate'])

date_for_timeseries['Date'] = date_for_timeseries['InvoiceDate'].dt.date

daily_sales = (
    date_for_timeseries.groupby('Date')['TotalAmount'].sum()
    .reset_index(name='DailyTotal')
)

daily_sales = daily_sales.sort_values('Date').reset_index(drop=True)

print("\nFirst 5 days of daily sales: ")
print(daily_sales.head())

print(f"\nTotal number of days in dataset: {len(daily_sales)}")