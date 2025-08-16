#Calculate the 25th, 50th, and 75th percentiles of the number of stories created per user per day.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe

#convert the 'story_date' column elements into datetime objects and handle errors
stories_data['story_date']=pd.to_datetime(stories_data['story_date'],errors='coerce')

#group by story_date and user_id and get the sum
grouped_stories_data=stories_data.groupby(['story_date','user_id'])['story_count'].sum()

#sort the values in ascending order
grouped_stories_data=grouped_stories_data.sort_values(ascending=True)

#calculate the 25th, 50th, and 75th percentiles 
q1=np.percentile(grouped_stories_data.values,25)
q2=np.percentile(grouped_stories_data.values,50)
q3=np.percentile(grouped_stories_data.values,75)
print(q1)
print(q2)
print(q3)
