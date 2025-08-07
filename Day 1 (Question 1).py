# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: dim_groups
# Please print your final result or dataframe

#convert the data type on the 'created_date' column
dim_groups['created_date']=pd.to_datetime(dim_groups['created_date'] )

#filter created_date
start_date = '2024-10-01'
end_date = '2024-10-31'
filtered_df = dim_groups[(dim_groups['created_date'] >= start_date) & (dim_groups['created_date'] <= end_date)]

#print the maximum participant_count
print(filtered_df["participant_count"].max())
# def dateconversion(x):
#   dim_groups[x]=pd.to_datetime(dim_groups[x] )
#   start
#   largestgroup=pd.dim_groups[x].max()
#   print(largestgroup)

# dim_groups["created_date"].apply(dateconversion)
