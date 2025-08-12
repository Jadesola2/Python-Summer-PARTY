 # Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe

stories_data['story_date']=pd.to_datetime(stories_data['story_date'],errors='coerce')
grouped_stories_data=stories_data.groupby(['story_date','user_id'])['story_count'].sum()
grouped_stories_data=grouped_stories_data.sort_values(ascending=True)
q1=np.percentile(grouped_stories_data.values,25)
q2=np.percentile(grouped_stories_data.values,50)
q3=np.percentile(grouped_stories_data.values,75)
print(q1)
print(q2)
print(q3)
