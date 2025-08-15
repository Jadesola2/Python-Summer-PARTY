#Identify and remove any duplicate sales transactions from the dataset to ensure accurate analysis of seasonal patterns.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: ice_cream_sales_data
# Please print your final result or dataframe

#remove rows with duplicate transaction_id
ice_cream_sales_data=ice_cream_sales_data.drop_duplicates(subset=['transaction_id'])

print(ice_cream_sales_data)
