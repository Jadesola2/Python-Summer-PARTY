user_engagement_data=user_engagement_data.drop_duplicates()
cleaned_df=user_engagement_data.fillna(0.0)
cleaned_df['average_interaction_time']=cleaned_df.groupby('search_results_displayed')['interaction_time'].transform('mean')

cleaned_df=cleaned_df[['search_results_displayed','average_interaction_time']].drop_duplicates().to_string(index=False)
print(cleaned_df)
