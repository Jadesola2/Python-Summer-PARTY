# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags
# Please print your final result or dataframe

fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2024-11-01'
end_date='2024-11-30'
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)& (fct_transactions['transaction_date']<=end_date)]
filtered_fct_transactions['transaction_amount']=filtered_fct_transactions['transaction_amount'].fillna(0.0)
average_transaction_amount=filtered_fct_transactions['transaction_amount'].mean()

print(average_transaction_amount)
