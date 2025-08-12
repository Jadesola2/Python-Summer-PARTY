# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe

app_ratings['rating']=app_ratings['rating'].str.replace(',','.').str.strip()
app_ratings['rating']=pd.to_numeric(app_ratings['rating'],errors='coerce')
print(app_ratings)
