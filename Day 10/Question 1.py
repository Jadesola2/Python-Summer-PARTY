#There are some data inconsistencies in the 'rating' column, specifically: leading or trailing white space, decimals represented by commas instead of decimal points (eg. 4,2 instead of 4.2), and non-numeric values. Clean up these data issues and convert the column to a numeric data type.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe


app_ratings=pd.read_csv('Day 10/app_ratings.csv')


#cleaning the rating column by removing whitespaces and replacing the commas with a point
app_ratings['rating']=app_ratings['rating'].str.replace(',','.').str.strip()

#change the data type to numeric and use "errors='coerce'" to handles errors in the type conversion
app_ratings['rating']=pd.to_numeric(app_ratings['rating'],errors='coerce')
print(app_ratings)
