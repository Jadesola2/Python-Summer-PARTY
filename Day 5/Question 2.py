#Using the cleaned data, calculate the total pre-sale orders per month for each region and demographic group.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe


#drop duplicated rows
pre_sale_data=pre_sale_data.drop_duplicates()

#convert the pre_order_date column into datetime objects
pre_sale_data['pre_order_date']=pd.to_datetime(pre_sale_data['pre_order_date'])

#fill missing data
pre_sale_data['customer_id'].fillna('NA',inplace=True)
pre_sale_data['region'].fillna('NA',inplace=True)
pre_sale_data['demographic_group'].fillna('Unknown', inplace=True)
pre_sale_data['pre_order_date'].fillna('2024-07-01',inplace=True)
pre_sale_data['pre_order_quantity'].fillna(pre_sale_data['pre_order_quantity'].mean(),inplace=True)

#create a column to indicate the month each pre_order was made
pre_sale_data['month'] = pre_sale_data['pre_order_date'].dt.to_period('M')

#calculate the total pre-order quantity after grouping by region, month and demographic_group
pre_sale_data['total_pre_sale_orders']=pre_sale_data.groupby(['region','month','demographic_group'])['pre_order_quantity'].transform(sum)

#crop the dataframe
pre_sale_data=pre_sale_data[['month','demographic_group','region','total_pre_sale_orders']]

#drop duplicates
pre_sale_data=pre_sale_data.drop_duplicates()

#create a pivot table
pivot_table = pre_sale_data.pivot_table(index=['region', 'demographic_group'], columns='month', values='total_pre_sale_orders')

print(pivot_table)


