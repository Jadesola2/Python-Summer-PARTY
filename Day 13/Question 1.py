#There was an error in our data collection process, and we unknowingly introduced duplciate rows into our data. Remove any duplicate entries in the customer ratings data to ensure the accuracy of the analysis.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: milkshake_ratings
# Please print your final result or dataframe

#drop duplicates
cleaned_milkshake_ratings=milkshake_ratings.drop_duplicates()

print(cleaned_milkshake_ratings)
