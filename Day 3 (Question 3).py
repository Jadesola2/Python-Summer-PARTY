import pandas as pd
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date']) 
start_date='2024-09-01'
end_date='2024-09-30'
new_df=fct_guest_spending[(fct_guest_spending['visit_date']>=start_date) & (fct_guest_spending['visit_date']<=end_date)]
new_df['total_amount_spent']=new_df.groupby('guest_id')['amount_spent'].transform(sum)
new_df=new_df[['guest_id','total_amount_spent']]
new_df=new_df[new_df['total_amount_spent']>0]
conditions=[(new_df['total_amount_spent']>0.00) & (new_df['total_amount_spent']<50.00),
            (new_df['total_amount_spent']>=50.00) &( new_df['total_amount_spent']<100.00),
           (new_df['total_amount_spent']>=100.00)]
choice=['Low','Medium','High']
new_df['spending_segment']=np.select(conditions,choice, default='Other')
new_df=new_df.drop_duplicates().to_string(index=False)






print(new_df)
