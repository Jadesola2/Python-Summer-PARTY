# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe

#convert the elements of the transaction_date column into datetime objects and filter the dataframe to only include transactions that occurred between April 1st and June 30th, 2025
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2025-04-01'
end_date='2025-06-30'
fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]

#get the average order_value for each payment method
average_order_value=fct_transactions.groupby('payment_method')['order_value'].mean()


print(average_order_value)
