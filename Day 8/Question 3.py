#Between April 1st and June 30th, 2025, what would be the predicted sales lift if a 'pay over time' option were introduced? Assume that 20% of credit card transactions during this period would switch to using the 'pay over time' option. And that for these switched transactions, the order value is expected to increase by 15% based on the average order value of all credit card transactions in that same time period.


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe

#convert the transaction_date column elements into datetime objects and filter it to include transaction that occurred between April 1st and June 30th, 2025
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2025-04-01'
end_date='2025-06-30'
fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]

#get the average order_value for each payment_method
average_order_value=fct_transactions.groupby('payment_method')['order_value'].mean()

#get the total order_value for each payment_method
total_sales=fct_transactions.groupby('payment_method')['order_value'].sum()

#crop the payment_method column
payment=fct_transactions['payment_method']

#get the count for each payment method
count=payment.value_counts()

#calculate the number of switched customers
no_of_switched_customers=count['credit_card']*0.2

#calculate the increase in order_value
increase_in_order_value=average_order_value['credit_card']*0.15

print((no_of_switched_customers*increase_in_order_value))

