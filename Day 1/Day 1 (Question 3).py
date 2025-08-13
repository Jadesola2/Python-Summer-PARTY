#For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? This insight will help assess engagement in larger groups and support recommendations for group messaging features.
#A dataframe with the columns: created_date, participant_count,group_id and total_messages was given and I was asked to write a code to give the average number of messages sent to groups with over 50 participants created in October 2024  

import pandas as pd
#convert the data type on the 'created_date' column
dim_groups['created_date']=pd.to_datetime(dim_groups['created_date'] )

#filter created_date
start_date = '2024-10-01'
end_date = '2024-10-31'
filtered_df = dim_groups[(dim_groups['created_date'] >= start_date) & (dim_groups['created_date'] <= end_date)]

#print the  average number of messages sent to groups with over 50 participants created in October 2024  
print(filtered_df[(filtered_df["participant_count"]>50)]["total_messages"].mean())
