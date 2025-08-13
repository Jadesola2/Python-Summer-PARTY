#Calculate the basic summary statistics (mean, median, standard deviation) of app ratings for each category to identify variations and performance patterns.



# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe

app_ratings=pd.read_csv('Day 10/app_ratings.csv')
#cleaning the rating column by removing whitespaces and replacing the commas with a point
app_ratings['rating']=app_ratings['rating'].str.replace(',','.').str.strip()

#change the data type to numeric and use "errors='coerce'" to handles errors in the type conversion
app_ratings['rating']=pd.to_numeric(app_ratings['rating'],errors='coerce')

#use the aggregate function to 
stats_summary=app_ratings.groupby('category')['rating'].agg(['mean','median','std'])


print(stats_summary)
