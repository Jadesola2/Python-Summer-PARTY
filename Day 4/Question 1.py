#Identify and remove any duplicate entries in the dataset to ensure data quality. How many duplicates were found and removed?

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: user_engagement_data
# Please print your final result or dataframe



#calculate the number of duplicates found in the dataframe
no_of_duplicates=user_engagement_data.duplicated().sum()

print(no_of_duplicates)

#clean the dataframe by dropping duplicates
cleaned_df=user_engagement_data.drop_duplicates()

print(cleaned_df)
