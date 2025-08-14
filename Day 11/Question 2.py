# For transactions occurring in November 2024, what is the average transaction amount, using 0 as a default for any missing values? This calculation will help us detect abnormal transaction amounts that could be related to fraudulent activity.



#Explore The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags
# Please print your final result or dataframe

#convert the'transaction_date' column to a time date format
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])

#filter the dataframe to only include transactions that occured in November 2024
start_date='2024-11-01'
end_date='2024-11-30'
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)& (fct_transactions['transaction_date']<=end_date)]

#fill null data in the transaction_amount column with 0.0
filtered_fct_transactions['transaction_amount']=filtered_fct_transactions['transaction_amount'].fillna(0.0)

#calculate the mean/average
average_transaction_amount=filtered_fct_transactions['transaction_amount'].mean()

print(average_transaction_amount)
