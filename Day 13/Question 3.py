#For each row in dataset, calculate the difference between that customer's rating and the average rating for the flavor. Don't forget to clean the DataFrame first by dropping duplicate values.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: milkshake_ratings
# Please print your final result or dataframe

#clean the dataframe by dropping duplicates
cleaned_milkshake_ratings=milkshake_ratings.drop_duplicates()

#create a row for the average rating per flavor
cleaned_milkshake_ratings['average_customer_rating']=cleaned_milkshake_ratings.groupby('flavor')['rating'].transform('mean')

#calculate the difference_in_rating
cleaned_milkshake_ratings['difference_in_rating']=cleaned_milkshake_ratings['rating']-cleaned_milkshake_ratings['average_customer_rating']
print(cleaned_milkshake_ratings)



  
