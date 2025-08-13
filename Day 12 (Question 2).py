# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: customer_returns
# Please print your final result or datafram

customer_returns['order_date']=pd.to_datetime(customer_returns['order_date'], errors='coerce')


customer_returns.set_index(['customer_id', 'order_date'], inplace=True)
monthly_returns = customer_returns[customer_returns['return_flag'] == True].groupby(
    [pd.Grouper(level='customer_id'), pd.Grouper(level='order_date', freq='M')]
).size()




result = monthly_returns.reset_index(name='total_returns')
print(result)
