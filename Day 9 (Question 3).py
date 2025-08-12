# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe


stories_data['story_date']=pd.to_datetime(stories_data['story_date'],errors='coerce')
number_of_unique_users=stories_data['user_id'].str.lower().str.strip().drop_duplicates().count()
stories_data['user_id']=stories_data['user_id'].str.lower().str.strip()
grouped_stories_data=stories_data.groupby(['story_date','user_id'])['story_count'].sum()
grouped_stories_data=grouped_stories_data.sort_values(ascending=True)
greater_than_10=grouped_stories_data[grouped_stories_data>10]
unique_users_greater_than_10=greater_than_10.index.get_level_values('user_id').nunique()

print(unique_users_greater_than_10/number_of_unique_users*100)
