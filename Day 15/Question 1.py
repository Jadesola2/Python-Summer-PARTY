#What is the average driver earnings per completed UberPool ride with more than two riders between July 1st and September 30th, 2024? This analysis will help isolate trips that meet specific rider thresholds to understand their impact on driver earnings.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips
# Please print your final result or dataframe


#convert the 'trip_date column elements into datetime objects and the rider_count into numeric objects
fct_trips['trip_date']=pd.to_datetime(fct_trips['trip_date'])
fct_trips['rider_count']=pd.to_numeric(fct_trips['rider_count'])


#filter the dataframe to only include rides that occurred between July 1st and September 30th, 2024
start_date='2024-07-01'
end_date='2024-09-30'
filtered_fct_trips=fct_trips[(fct_trips['trip_date']>=start_date) & (fct_trips['trip_date']<=end_date)]

#filter the dataframe to only include rides where ride_type==UberPool and rider_count >2
filtered_fct_trips=filtered_fct_trips[filtered_fct_trips['ride_type']=='UberPool']
filtered_fct_trips=filtered_fct_trips[filtered_fct_trips['rider_count']>2]

#get the average total_earnings
filtered_fct_trips=filtered_fct_trips['total_earnings'].mean()
print(filtered_fct_trips)




















filtered_fct_trips=filtered_fct_trips['total_earnings'].mean()
print(filtered_fct_trips)
