# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe
pre_sale_data=pre_sale_data.drop_duplicates()
pre_sale_data_missing=pre_sale_data.isnull().any(axis=1).sum()
pre_sale_data['pre_order_date']=pd.to_datetime(pre_sale_data['pre_order_date'])
pre_sale_data['customer_id'].fillna('NA',inplace=True)
pre_sale_data['region'].fillna('NA',inplace=True)
pre_sale_data['demographic_group'].fillna('Unknown', inplace=True)
pre_sale_data['pre_order_date'].fillna('2024-07-01',inplace=True)
pre_sale_data['pre_order_quantity'].fillna(pre_sale_data['pre_order_quantity'].mean(),inplace=True)
pre_sale_data['month'] = pre_sale_data['pre_order_date'].dt.to_period('M')
pre_sale_data['total_pre_sale_orders']=pre_sale_data.groupby(['region','month','demographic_group'])['pre_order_quantity'].transform(sum)
pre_sale_data=pre_sale_data[['month','demographic_group','region','total_pre_sale_orders']]
pre_sale_data=pre_sale_data.drop_duplicates()
pivot_table = pre_sale_data.pivot_table(index=['region', 'demographic_group'], columns='month', values='total_pre_sale_orders')

print(pivot_table)


