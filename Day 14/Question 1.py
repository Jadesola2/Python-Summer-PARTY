#For the month of July 2024, how many transactions did loyalty program members and non-members make? Compare the transaction counts between these two groups.
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers
# Please print your final result or dataframe

#convert the 'transaction_date' column element into datetime objects and filter it to only include transactions that occurred in July 2024
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2024-07-01'
end_date='2024-07-31'
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]

#get the number of transactions for each customer_id
filtered_fct_transactions=filtered_fct_transactions.groupby('customer_id')['transaction_value'].count().reset_index()
#merge the two dataframes
merged_df=pd.merge(filtered_fct_transactions,dim_customers, how='left',on='customer_id')

#rename the column
merged_df=merged_df.rename(columns={'transaction_value':'transaction_count'})

#get the sum of transaction_count for 'is_loyalty_member'==True
merged_df=merged_df.groupby('is_loyalty_member')['transaction_count'].sum()
print(merged_df)
