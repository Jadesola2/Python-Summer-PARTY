#Among transactions flagged as 'High' risk in December 2024, which day of the week recorded the highest number of such transactions? This analysis is intended to pinpoint specific days with concentrated high-risk activity and support the development of our preliminary fraud detection score.
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags

# Please print your final result or dataframe

#convert the 'transaction_date' column to a datetime format
fct_transactions['transaction_date']=pd.to_datetime(fct_transactions['transaction_date'])
start_date='2024-12-01'
end_date='2024-12-31'

#filter fct_transactions to include only transactions that occurred in December 2024
filtered_fct_transactions=fct_transactions[(fct_transactions['transaction_date']>=start_date)& (fct_transactions['transaction_date']<=end_date)]

#include a day_of_the_week column to make the problem easier
filtered_fct_transactions['day_of_the_week']=filtered_fct_transactions['transaction_date'].dt.day_name()

#merge dim_risk_flags and filtered_fct_transactions using left join on the 'transaction_id column
merged_df=pd.merge(filtered_fct_transactions,dim_risk_flags,how='left',on='transaction_id')

#create another dataframe to include only transactions with High risk levels
high_risk = merged_df[merged_df['risk_level'] == 'High']

#calculate the size of the list after it has been grouped by 'day_of_the_week'
counts = high_risk.groupby('day_of_the_week').size()

#assign to most_common_day the value of the day of the week with the most High risk transactions
most_common_day = counts.idxmax()


print(most_common_day, counts[most_common_day])
