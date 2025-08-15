#What percentage of records have missing values in at least one column? Handle the missing values, so that we have a cleaned dataset to work with.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data
# Please print your final result or dataframe

#drop the duplicated rows
pre_sale_data=pre_sale_data.drop_duplicates()

#get the sum of rows with missing or null data
pre_sale_data_missing=pre_sale_data.isnull().any(axis=1).sum()

#convert the pre_oder_date column into datetime objects
pre_sale_data['pre_order_date']=pd.to_datetime(pre_sale_data['pre_order_date'])

#get the lenght of the data (number of rows)
total_rows=len(pre_sale_data)

# print percentage of records have missing values in at least one column
print((pre_sale_data_missing/total_rows)*100)

#fill the missing data
pre_sale_data['customer_id'].fillna('NA',inplace=True)
pre_sale_data['region'].fillna('NA',inplace=True)
pre_sale_data['demographic_group'].fillna('Unknown', inplace=True)
pre_sale_data['pre_order_date'].fillna('2024-07-01',inplace=True)
pre_sale_data['pre_order_quantity'].fillna(pre_sale_data['pre_order_quantity'].mean(),inplace=True)

print(pre_sale_data)
