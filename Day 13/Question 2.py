#For each milkshake flavor, calculate the average customer rating and append this as a new column to the milkshake_ratings DataFrame. Don't forget to clean the DataFrame first by dropping duplicate values.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: milkshake_ratings
# Please print your final result or dataframe

#drop duplicates
cleaned_milkshake_ratings=milkshake_ratings.drop_duplicates()

#create a row for the average rating for each flavor
cleaned_milkshake_ratings['average_customer_rating']=cleaned_milkshake_ratings.groupby('flavor')['rating'].transform('mean')

print(cleaned_milkshake_ratings)
