#What percentage of users have had at least one day, where they posted more than 10 stories on that day?



# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe

#convert the 'story_date' column elements into datetime objects
stories_data['story_date']=pd.to_datetime(stories_data['story_date'],errors='coerce') 

#get the unique users by cleaning the user_id column, dropping duplicates and then getting the count
number_of_unique_users=stories_data['user_id'].str.lower().str.strip().drop_duplicates().count()

#cleaning the user_id column
stories_data['user_id']=stories_data['user_id'].str.lower().str.strip()

#group by both story_date and user_id and get the sum of story_count 
grouped_stories_data=stories_data.groupby(['story_date','user_id'])['story_count'].sum()

#sort the values in ascending order
grouped_stories_data=grouped_stories_data.sort_values(ascending=True)

#create a dataframe for rows where the sum of story_count is greater than 10
greater_than_10=grouped_stories_data[grouped_stories_data>10]

#get the number of unique user_id where the sum of story_count is greater than 10 
unique_users_greater_than_10=greater_than_10.index.get_level_values('user_id').nunique()

print(unique_users_greater_than_10/number_of_unique_users*100)


