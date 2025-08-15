#After dropping duplicates, aggregate the data to find the average user interaction time for each number of search results displayed per page. What are the average interaction times?


#clean the dataframe by dropping duplicates and filling null data with 0.0
user_engagement_data=user_engagement_data.drop_duplicates()
cleaned_df=user_engagement_data.fillna(0.0)

#create a column for the average interaction time per search result displayed
cleaned_df['average_interaction_time']=cleaned_df.groupby('search_results_displayed')['interaction_time'].transform('mean')

#drop duplicated rows
cleaned_df=cleaned_df[['search_results_displayed','average_interaction_time']].drop_duplicates().to_string(index=False)
print(cleaned_df)
