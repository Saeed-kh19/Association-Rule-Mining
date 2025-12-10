import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prepare_timeseries import daily_sales

#Convert Date column to datetime
daily_sales['Date'] = pd.to_datetime(daily_sales['Date'])

#Time series plot of daily sales
plt.figure(figsize=(14,6))
sns.lineplot(data=daily_sales,x='Date',y='DailyTotal',color='steelblue')
plt.title('Daily Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

#aAdding 7-day moving average
daily_sales['7DayMA'] = daily_sales['DailyTotal'].rolling(window=7).mean()

#Plot with moving average
plt.figure(figsize=(14,6))
sns.lineplot(data=daily_sales, x='Date', y='DailyTotal', label='Dailyl Sales', color='lightgray')
sns.lineplot(data=daily_sales,x='Date',y='7DayMA', label='7-Day Moving Average',color='darkblue')
plt.title('Sales Trend with 7-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.tight_layout()
plt.show()