#Between April 1st and June 30th, 2025, what is the count of transactions for each payment method? This analysis will establish the baseline distribution of how customers currently pay.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe

#convert the elements of the transaction_date column into datetime objects and filter the dataframe to only include transactions that occurred between April 1st and June 30th, 2025
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2025-04-01'
end_date='2025-06-30'
fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]

#get the number of transactions for each payment method
transaction_count=fct_transactions.groupby('payment_method')['transaction_id'].count()

print(transaction_count)

