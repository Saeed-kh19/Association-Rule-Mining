import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Preparing the time series
from prepare_timeseries import date_for_timeseries
df_timeseries = date_for_timeseries.sort_values('Date').reset_index(drop=True)

# Setting the Date as index
df_timeseries['Date'] = pd.to_datetime(df_timeseries['Date'])
df_timeseries.set_index('Date', inplace=True)

# Seasonal Decomposition
result = seasonal_decompose(df_timeseries['TotalAmount'], model='additive', period=7)

# Drawing Plots
plt.figure(figsize=(12,8))
plt.subplot(411)
plt.plot(result.observed, label='Observed')
plt.legend(loc='best')

plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc='best')

plt.subplot(413)
plt.plot(result.seasonal, label='Seasonal')
plt.legend(loc='best')

plt.subplot(414)
plt.plot(result.resid, label='Residual')
plt.legend(loc='best')

plt.tight_layout()
plt.show()
