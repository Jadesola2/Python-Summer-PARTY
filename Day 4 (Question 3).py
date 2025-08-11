user_engagement_data=user_engagement_data.drop_duplicates()
cleaned_df=user_engagement_data.fillna(0.0)
cleaned_df['average_interaction_time']=cleaned_df.groupby('search_results_displayed')['interaction_time'].transform('mean')
# cleaned_df=cleaned_df.assign(average_user_interaction_time=(cleaned_df['interaction_time']/cleaned_df['search_results_displayed']))
# cleaned_df=[['search_results_displayed','average_interaction_time']]
cleaned_df=cleaned_df[['search_results_displayed','average_interaction_time']].drop_duplicates().sort_values(by='average_interaction_time',ascending=False)
highest_average_interaction_time=cleaned_df.iloc[0]
print(highest_average_interaction_time)
