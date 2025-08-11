# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: user_engagement_data
# Please print your final result or dataframe
count=user_engagement_data['user_id'].value_counts()
new_df2=user_engagement_data.duplicated().sum()

print(new_df2)
cleaned_df=user_engagement_data.drop_duplicates()

print(cleaned_df)
