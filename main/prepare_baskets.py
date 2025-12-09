import pandas as pd
from feature_engineering import filtered_by_price

basket_df = (
    filtered_by_price.groupby('InvoiceNo')['Description'].apply(lambda items: sorted(set(items)))
    .reset_index(name='Basket')
)

item_frequency = filtered_by_price['Description'].value_counts()

frequent_items = item_frequency[item_frequency >= 10].index.tolist()

basket_df['Basket'] = basket_df['Basket'].apply(
    lambda basket: [item for item in basket if item in frequent_items]
)

basket_df = basket_df[basket_df['Basket'].map(len)>0]

print(f"\nTotal baskets after filtering: {len(basket_df)}")
print("\nFirst 5 filtered baskets:")
print(basket_df.head())