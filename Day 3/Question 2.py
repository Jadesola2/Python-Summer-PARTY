#For guests who visited our parks more than once in August 2024, what is the difference in spending between their first and their last visit? This investigation, using sequential analysis, will reveal any shifts in guest spending behavior over multiple visits.

#filter the dataframe to include visit that occured in August 2024
start_date='2024-08-01'
end_date='2024-08-31'
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date'])
new_df=fct_guest_spending[(fct_guest_spending['visit_date']>=start_date)&(fct_guest_spending['visit_date']<=end_date)]

#sort the values by both guest_id and 'visit_date' in ascending order
new_df=new_df.sort_values(by=['guest_id','visit_date'], ascending=[True,True])

#use value_counts function to get the number of times each guest visited
guest_id_counts=new_df['guest_id'].value_counts()

#find out the guest that visited more than once
duplicated_guest_id= guest_id_counts[guest_id_counts>1].index

#make new_df include only guest_ids that visited more than once
new_df=new_df[new_df['guest_id'].isin(duplicated_guest_id)]

#group by guest_id and create a new column for the amount_spent during the guest's first and last visit
ng new_df=new_df.groupby('guest_id')['amount_spent'].agg(['first','last'])

#calculate the difference in amount_spent during the guest's first and last visit
new_df['difference_in_amount_spent']=new_df['last']-new_df['first']
print(new_df)
