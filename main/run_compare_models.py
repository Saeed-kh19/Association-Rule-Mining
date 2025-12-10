import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from prepare_timeseries import date_for_timeseries
df_timeseries=date_for_timeseries.sort_values('Date').reset_index(drop=True)

alpha = 0.5
train_size = int(len(df_timeseries) * 0.8)
train = df_timeseries['TotalAmount'][:train_size]
test = df_timeseries['TotalAmount'][train_size:]

# Exponential Smoothing
es_pred = []
prev = train.iloc[0]
for actual in train:
    prev = alpha * actual + (1 - alpha) * prev
es_pred = [prev] * len(test)

# Moving Average
ma_pred = []
for i in range(len(test)):
    window = df_timeseries['TotalAmount'][train_size + i - 7 : train_size + i]
    ma_pred.append(window.mean())

# Evaluation
def rmse(y_true, y_pred): return np.sqrt(((y_true - y_pred) ** 2).mean())
def mape(y_true, y_pred): return (np.abs((y_true - y_pred) / y_true).mean()) * 100

print("MA RMSE:", rmse(test, ma_pred), "MAPE:", mape(test, ma_pred))
print("ES RMSE:", rmse(test, es_pred), "MAPE:", mape(test, es_pred))

plt.plot(test.index, test.values, label='Actual')
plt.plot(test.index, ma_pred, label='Moving Average')
plt.plot(test.index, es_pred, label='Exponential Smoothing')
plt.legend(); plt.show()
