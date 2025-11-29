import pandas as pd

dataset_path = "C:\\Users\\Saeed.kh\\Desktop\\Project\\Association-Rule-Mining\\dataset\\dataset.xlsx"
retail_data=pd.read_excel(dataset_path)

print("First 5 rows of the dataset:")
print(retail_data.head())

print("\nDataset dimensions (rows,columns):")
print(retail_data.shape)

print("\nColumn data types:")
print(retail_data.dtypes)

print("\nSummary of missing values per column:")
print(retail_data.isnull().sum())