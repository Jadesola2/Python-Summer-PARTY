#Take a look at the data in the story_date column. Correct any data type inconsistencies in that column.


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data
# Please print your final result or dataframe

#convert the elements
stories_data['story_date']=pd.to_datetime(stories_data['story_date'],errors='coerce')
print(stories_data)
