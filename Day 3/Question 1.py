#What is the average spending per guest per visit for each park experience type during July 2024? Ensure that park experience types with no recorded transactions are shown with an average spending of 0.0. This analysis helps establish baseline spending differences essential for later segmentation.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending
# Please print your final result or dataframe

#convert the visit_date column into datetime objects
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date'])

#filter the dataframe to only include rows with visit dates in July 2024
start_date = '2024-07-01'
end_date = '2024-07-31'
new_df = fct_guest_spending[(fct_guest_spending['visit_date']>=start_date) &  (fct_guest_spending['visit_date']<=end_date)]

#group the dataframe by park_experience_type and guest_id and calculate the average amount_spent 
new_df=new_df.groupby(['park_experience_type','guest_id'])['amount_spent'].mean()

#reset the index
new_df=new_df.reset_index()

#group the dataframe once again by park_experience_type and calculate the average 'amount_spent'
new_df=new_df.groupby('park_experience_type')['amount_spent'].mean()

#drop the guest_id column
new_df=new_df.drop(columns='guest_id')

#create a series with the unique park_experience_type elements
unique=fct_guest_spending['park_experience_type'].unique()

#convert it into a dataframe
unique_df=pd.DataFrame(unique, columns=['park_experience_type'])


#reset the index
new_df=new_df.reset_index()


#merge unique_df and new_df using left join on the column 'park_experience_type
new_df=pd.merge(unique_df,new_df ,on='park_experience_type', how='left')

#fill null values in the 'amount_spent' column with 0.0
new_df['amount_spent']=new_df['amount_spent'].fillna(0.0)

#include only the two relevant columns and sort the park_experience_type alphabetically and reset index
new_df=new_df[['park_experience_type','amount_spent']].sort_values('park_experience_type').reset_index(drop=True)

#change the amount_spent column to avg_spending_per_guest
new_df =new_df.rename(columns={'amount_spent':'avg_spending_per_guest'})

#reset the index 
new_df.reset_index(drop=True, inplace=True)
new_df = new_df.to_string(index=False)
print(new_df)




