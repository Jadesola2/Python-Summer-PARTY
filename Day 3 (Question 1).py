# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending
# Please print your final result or dataframe
import pandas as pd
fct_guest_spending.to_csv("file.csv")
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date'])
start_date = '2024-07-01'
end_date = '2024-07-31'
unique=fct_guest_spending['park_experience_type'].unique()
unique_df=pd.DataFrame(unique, columns=['park_experience_type'])
new_df = fct_guest_spending[(fct_guest_spending['visit_date']>=start_date) &  (fct_guest_spending['visit_date']<=end_date)]
new_df=new_df.groupby(['park_experience_type','guest_id'])['amount_spent'].mean()


new_df=new_df.reset_index()
new_df=new_df.groupby('park_experience_type')['amount_spent'].mean()
new_df=new_df.drop(columns='guest_id')
new_df=pd.merge(unique_df,new_df ,on='park_experience_type', how='left')
new_df['amount_spent']=new_df['amount_spent'].fillna(0.0)
new_df=new_df[['park_experience_type','amount_spent']].sort_values('park_experience_type').reset_index(drop=True)
# new_df.drop( axis=1, inplace=True)
new_df =new_df.rename(columns={'amount_spent':'avg_spending_per_guest'})
new_df.reset_index(drop=True, inplace=True)
new_df = new_df.to_string(index=False)
print(new_df)
