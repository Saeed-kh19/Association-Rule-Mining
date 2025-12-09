import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engineering import filtered_by_price

print("\nSummary statistics for numerical columns:")
print(filtered_by_price[['Quantity','UnitPrice','TotalAmount']].describe())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(filtered_by_price['Quantity'],bins=50,kde=True,color='skyblue')
plt.title('Distribution of Quantity')

plt.subplot(1,2,2)
sns.histplot(filtered_by_price['UnitPrice'],bins=50,kde=True,color='salmon')
plt.title('Distribution of UnitPrice')

plt.tight_layout()
plt.show()

top_products = (
    filtered_by_price['Description'].value_counts().head(15)
)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values,y=top_products.index,palette='viridis')
plt.title('Top 15 Most Frequently Purchased Products')
plt.xlabel('Purchase Count')
plt.ylabel('Product Description')
plt.tight_layout()
plt.show()

country_sales = (
    filtered_by_price.groupby('Country')['TotalAmount']
    .sum().sort_values(ascending=False).head(15)
)

plt.figure(figsize=(10,6))
sns.barplot(x=country_sales.values,y=country_sales.index,palette='magma')
plt.title('Top 15 Countries by Total Sales')
plt.xlabel('Total Sales Amount')
plt.ylabel('Country')
plt.tight_layout()
plt.show()