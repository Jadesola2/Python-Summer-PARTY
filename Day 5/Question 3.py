#Predict the total pre-sales quantity for each region for September 2024. Assume that growth rate from August to September, is the same as the growth rate from July to August in each region.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe

#clean the data by dropping duplicates 
pre_sale_data=pre_sale_data.drop_duplicates()

#change the pre_order_date column elements to datetime objects
pre_sale_data['pre_order_date']=pd.to_datetime(pre_sale_data['pre_order_date'])

#fill null data 
pre_sale_data['customer_id'].fillna('NA',inplace=True)
pre_sale_data['region'].fillna('NA',inplace=True)
pre_sale_data['demographic_group'].fillna('Unknown', inplace=True)
pre_sale_data['pre_order_date'].fillna('2024-07-01',inplace=True)
pre_sale_data['pre_order_quantity'].fillna(pre_sale_data['pre_order_quantity'].mean(),inplace=True)

#create a new column for the months states in the pre_order_date column
pre_sale_data['month'] = pre_sale_data['pre_order_date'].dt.to_period('M')

#filter the data only include rows with pre_order_date between August and September 
pre_sale_data = pre_sale_data[pre_sale_data['month'].isin([pd.Period('2024-07'),pd.Period ('2024-08')])]

#calculate the sum of pre_order_quantity for each region and month, then reset the index
pre_sale_data=pre_sale_data.groupby(['region','month'])['pre_order_quantity'].sum().reset_index()

#drop duplicated regions and months
pre_sale_data=pre_sale_data.drop_duplicates(subset=['region','month'])

pre_sale_data=pre_sale_data[['month','region','pre_order_quantity']]

#create a pivot table
pivot_table = pre_sale_data.pivot_table(index=['region'], columns='month', values='pre_order_quantity')

#calculate the growth rate
growth_rate=((pivot_table['2024-08']-pivot_table['2024-07'])/pivot_table['2024-07'])*100

#calculate the total pre-sales quantity for each region for September 2024
pivot_table['2024-09']=pivot_table['2024-08']*(1+growth_rate/100)

print(pivot_table)



