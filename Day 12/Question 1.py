#Identify and list all unique customer IDs who have made returns between July 1st 2024 and June 30th 2025. This will help us understand the base set of customers involved in returns during the specified period.


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: customer_returns
# Please print your final result or datafram

#convert the format of the order_date column to datetime format
customer_returns['order_date']=pd.to_datetime(customer_returns['order_date'], errors='coerce')

#filter the dataframe to include transactions that occurred between July 1st 2024 and June 30th 2025
start_date='2024-07-01'
end_date='2025-06-30'
filtered_returns=customer_returns[(customer_returns['order_date']>=start_date)&(customer_returns['order_date']<=end_date)]

#filter the dataframe to include only transactions where the retun_flag==True
customers_with_returns=filtered_returns[filtered_returns['return_flag']==True]

#use drop_duplicates() so that it only includes unique customer IDs
unique_customers=customers_with_returns['customer_id'].drop_duplicates()

print(unique_customers.to_string(index=False))
