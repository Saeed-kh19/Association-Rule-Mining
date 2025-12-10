import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from prepare_baskets import basket_df

# encoding the basket data
te  = TransactionEncoder()
te_array = te.fit(basket_df['Basket']).transform(basket_df['Basket'])
df_encoded = pd.DataFrame(te_array, columns=te.columns_)

# Applying Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.02, use_colnames=True)

# Generating association rules from frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)

# Filter rules with lift > 1 for positive association
rules_filtered = rules[rules['lift'] > 1].sort_values(by='lift', ascending=False)

# Select top 10 most interesting rules
top_rules = rules_filtered.head(10)

print(f"Number of rules after filtering: {len(top_rules)}")

print("\nTop 10 Association Rules (lift > 1):")
for idx, row in top_rules.iterrows():
    antecedent = ', '.join(row['antecedents'])
    consequent = ', '.join(row['consequents'])
    print(f"Rule: If a customer buys [{antecedent}], they are likely to buy [{consequent}]")
    print(f" - Support: {row['support']:.4f}")
    print(f" - Confidence {row['confidence']:.4f}")
    print(f" - Lift: {row['lift']:.4f}\n")
    
    
print("\nThreshold Explanation:")
print("used min_support = 0.02 to focus on itemsets appearing in at least 5% of the transactions. ")
print("used min_confidence = 0.3 to ensure rules are reliable and not spurious. \n")

top_rules = rules_filtered.head(10).copy()
top_rules['Antecedent'] = top_rules['antecedents'].apply(lambda x:', '.join(x))
top_rules['Consequent'] = top_rules['consequents'].apply(lambda x:', '.join(x))

print("Top 10 Association Rules: ")
print(top_rules[['Antecedent','Consequent','support','confidence','lift']].to_string(index=False))

plt.figure(figsize=(10,6))
scatter = sns.scatterplot(
    data=rules_filtered,
    x='support',
    y='confidence',
    hue='lift',
    palette='viridis',
    edgecolor='black'
)

plt.title('Association Rules: Support vs. Confidence')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.colorbar(scatter.collections[0], label='Lift')
plt.tight_layout()
plt.show()
