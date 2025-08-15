#Sort the aggregated results from Q2 to determine which number of search results per page has the highest average user interaction time. What is the optimal number of search results per page?

#clean the dataframe by dropping duplicates and filling null data with 0.0
user_engagement_data=user_engagement_data.drop_duplicates()
cleaned_df=user_engagement_data.fillna(0.0)

#create a column for the average interaction time per search result displayed
cleaned_df['average_interaction_time']=cleaned_df.groupby('search_results_displayed')['interaction_time'].transform('mean')

#drop the duplicates and sort the values in ascending order of search_results_displayed and average_interaction_time
cleaned_df=cleaned_df[['search_results_displayed','average_interaction_time']].drop_duplicates().sort_values(by='average_interaction_time',ascending=False)

#create a variable for the first column. cleaned_df.head(1) will work here too
highest_average_interaction_time=cleaned_df.iloc[0]

print(highest_average_interaction_time)

