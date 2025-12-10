import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prepare_baskets import basket_df

#Basket size distribution
basket_sizes = basket_df['Basket'].apply(len)

plt.figure(figsize=(10,6))
sns.histplot(basket_sizes,bins=30,kde=False,color='steelblue')
plt.title('Basket Size Distribution')
plt.xlabel('Number of Items per Basket')
plt.ylabel('Number of Transactions')
plt.tight_layout()
plt.show()

# Item Frequency across all baskets
all_items = [item for basket in basket_df['Basket'] for item in basket]
item_counts = pd.Series(all_items).value_counts().head(20)

plt.figure(figsize=(10,6))
sns.barplot(x=item_counts.values, y=item_counts.index,palette='cubehelix')
plt.title('Top 20 Most Frequent Items in Baskets')
plt.xlabel('Frequency')
plt.ylabel('Item Description')
plt.tight_layout()
plt.show()
