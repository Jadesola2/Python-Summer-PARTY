#Determine the percentage difference in average transaction value between loyalty program members and non-members for July 2024.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers
# Please print your final result or dataframe

#convert the 'transaction_date' column elements into datetime objects and filter it to include transactions that occurred in July 2024
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2024-07-01'
end_date='2024-07-31'
dim_customers['is_loyalty_member']=dim_customers['is_loyalty_member'].astype(int)
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)&(fct_transactions['transaction_date']<=end_date)]

#merge both dataframes
merged_df=pd.merge(filtered_fct_transactions,dim_customers, how='left',on='customer_id')

#group by is_loyalty_member and average transaction_value
merged_df=merged_df.groupby('is_loyalty_member')['transaction_value'].mean()

#calculate the percemtage difference
percentage_difference=((merged_df[1]-merged_df[0])/merged_df[0])*100
print(percentage_difference)

