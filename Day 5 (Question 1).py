# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe
pre_sale_data=pre_sale_data.drop_duplicates()
pre_sale_data_missing=pre_sale_data.isnull().any(axis=1).sum()

pre_sale_data['pre_order_date']=pd.to_datetime(pre_sale_data['pre_order_date'])
total_rows=len(pre_sale_data)
print((pre_sale_data_missing/total_rows)*100)

pre_sale_data['customer_id'].fillna('NA',inplace=True)
pre_sale_data['region'].fillna('NA',inplace=True)
pre_sale_data['demographic_group'].fillna('Unknown', inplace=True)
pre_sale_data['pre_order_date'].fillna('2024-07-01',inplace=True)
pre_sale_data['pre_order_quantity'].fillna(pre_sale_data['pre_order_quantity'].mean(),inplace=True)
print(pre_sale_data)
