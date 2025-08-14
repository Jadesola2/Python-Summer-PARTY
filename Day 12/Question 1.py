#Convert the 'order_date' column to a datetime format and create a MultiIndex with 'customer_id' and 'order_date'. Then, calculate the total number of returns per customer for each month. This will provide insights into monthly return patterns for each customer.
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: customer_returns
# Please print your final result or datafram

#convert the format for the 'order_date' column to datetime 
customer_returns['order_date']=pd.to_datetime(customer_returns['order_date'], errors='coerce')

#set the index to 'customer_id' and 'order_date' and make use of 'inplace=True' to reflect the change to the orginal dataframe
customer_returns.set_index(['customer_id', 'order_date'], inplace=True)

#for rows where 'return_flag'==True, group by customer_id and the month in the order_date and return the size
monthly_returns = customer_returns[customer_returns['return_flag'] == True].groupby(
    [pd.Grouper(level='customer_id'), pd.Grouper(level='order_date', freq='M')]
).size()


#reset the index to total_returns
result = monthly_returns.reset_index(name='total_returns')
print(result)

