import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Preparing time series data
from prepare_timeseries import date_for_timeseries

df_timeseries = date_for_timeseries.sort_values('Date')

# Splitting the data for 80% train and 20% test
split_index = int(len(df_timeseries) * 0.8)
train = df_timeseries.iloc[:split_index]
test = df_timeseries.iloc[split_index:].copy()

# Applying 7 Day Moving Average forecasting
predictions = []
for i in range(len(test)):
    window = df_timeseries.iloc[split_index + i - 7 : split_index + i]['TotalAmount']
    predictions.append(window.mean())
    
test['Predicted'] = predictions

# Evaluate performance (for RMSE  and MAPE)
rmse = np.sqrt(((test['TotalAmount'] - test['Predicted'])**2).mean())
mape = (np.abs((test['TotalAmount'] - test['Predicted']) / test['TotalAmount']).mean())

print("First 5 rows of actual vs predicted:")
print(test[['Date','TotalAmount','Predicted']].head())
print(f"\nRMSE: {rmse:.2f}")
print(f"MAPE: {mape:.2f}%")


#Acutal vs Predicted
plt.figure(figsize=(10,6))
plt.plot(test['Date'], test['TotalAmount'], label='Actual')
plt.plot(test['Date'], test['Predicted'], label='Predicted', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Daily Sales')
plt.title('Actual vs Predicted Sales (by 7-day Moving Average)')
plt.legend()
plt.tight_layout()
plt.show()