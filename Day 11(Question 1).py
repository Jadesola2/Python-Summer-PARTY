# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags
# Please print your final result or dataframe

fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2024-10-01'
end_date='2024-10-31'
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)& (fct_transactions['transaction_date']<=end_date)]
emerging_risk=filtered_fct_transactions['customer_email'].str.endswith(('gmail.com','yahoo.com','hotmail.com'))
uncommon_transactions=filtered_fct_transactions[~emerging_risk]
print(uncommon_transactions.shape[0])


