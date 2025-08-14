#In September 2024, how can guests be categorized into distinct spending segments such as Low, Medium, and High based on their total spending? Use the following thresholds for categorization:
#-Low: Includes values from $0 up to, but not including, $50.
#-Medium: Includes values from $50 up to, but not including, $100.
#-High: Includes values from $100 and above.
#Exclude guests who did not make any purchases in the period.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending
# Please print your final result or dataframe

#convert the 'visit_date' to datetime objects anf filter the dataframe to include only rows where the visit occurs in September 2024
fct_guest_spending['visit_date']=pd.to_datetime(fct_guest_spending['visit_date']) 
start_date='2024-09-01'
end_date='2024-09-30'
new_df=fct_guest_spending[(fct_guest_spending['visit_date']>=start_date) & (fct_guest_spending['visit_date']<=end_date)]

#create a new column called 'total_amount_spent' to include the total amount spent by each guest
new_df['total_amount_spent']=new_df.groupby('guest_id')['amount_spent'].transform(sum)

#crop the dataframe to include only the two relevant columns
new_df=new_df[['guest_id','total_amount_spent']]

#include on guests with total_amount_spent>0
new_df=new_df[new_df['total_amount_spent']>0]

#create a list of conditions and choices
conditions=[(new_df['total_amount_spent']>0.00) & (new_df['total_amount_spent']<50.00),
            (new_df['total_amount_spent']>=50.00) &( new_df['total_amount_spent']<100.00),
           (new_df['total_amount_spent']>=100.00)]
choice=['Low','Medium','High']

#use the numpy select function to select choices based on the conditions
new_df['spending_segment']=np.select(conditions,choice, default='Other')
new_df=new_df.drop_duplicates().to_string(index=False)







print(new_df)
