import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing timeseries
from prepare_timeseries import date_for_timeseries

# Sorting data frame
df_timeseries = date_for_timeseries.sort_values('Date').reset_index(drop=True)

# Forecast next 14 days by using the 7 days moving average
last_7 = list(df_timeseries['TotalAmount'].iloc[-7:])
predictions = []

for i in range(14):
    next_val = np.mean(last_7[-7:])
    predictions.append(next_val)
    last_7.append(next_val)

# Creating future dates
last_date = pd.to_datetime(df_timeseries['Date'].iloc[-1])
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=14)

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted_TotalAmount': predictions
})

print("14-Day Forecast:")
print(forecast_df)

# Plotting Forecast
plt.figure(figsize=(10,6))
plt.plot(df_timeseries['Date'].iloc[-30:], df_timeseries['TotalAmount'].iloc[-30:], label='Last 30 Days Actual')
plt.plot(forecast_df['Date'], forecast_df['Predicted_TotalAmount'], label='14-Day Forecast', linestyle='--', marker='o')
plt.xlabel('Date')
plt.ylabel('Daily Sales (TotalAmount)')
plt.title('14-Day Sales Forecast (7-day Moving Average)')
plt.legend()
plt.tight_layout()
plt.show()
