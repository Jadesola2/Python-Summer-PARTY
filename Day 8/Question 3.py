
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions
# Please print your final result or dataframe
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2025-04-01'
end_date='2025-06-30'
fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]
average_order_value=fct_transactions.groupby('payment_method')['order_value'].mean()
total_sales=fct_transactions.groupby('payment_method')['order_value'].sum()
payment=fct_transactions['payment_method']
count=payment.value_counts()
no_of_switched_customers=count['credit_card']*0.2
increase_in_order_value=average_order_value['credit_card']*0.15
total=total_sales['credit_card']
print((no_of_switched_customers*increase_in_order_value))

# print(increase_in_order_value)
