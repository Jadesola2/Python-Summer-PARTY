start_date='2024-08-01'
end_date='2024-08-31'
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date'])
new_df=fct_guest_spending[(fct_guest_spending['visit_date']>=start_date)&(fct_guest_spending['visit_date']<=end_date)]
new_df=new_df.sort_values(by=['guest_id','visit_date'], ascending=[True,True])
guest_id_counts=new_df['guest_id'].value_counts()
duplicated_guest_id= guest_id_counts[guest_id_counts>1].index
new_df=new_df[new_df['guest_id'].isin(duplicated_guest_id)]
new_df=new_df.groupby('guest_id')['amount_spent'].agg(['first','last'])
new_df['difference_in_amount_spent']=new_df['last']-new_df['first']
print(new_df)
