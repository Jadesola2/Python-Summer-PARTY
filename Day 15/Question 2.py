#For completed UberPool rides between July 1st and September 30th, 2024, derive a new column calculating earnings per mile (total_earnings divided by total_distance) and then compute the average earnings per mile for rides with more than two riders. This calculation will reveal efficiency metrics for driver compensation.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips
# Please print your final result or dataframe

fct_trips['trip_date']=pd.to_datetime(fct_trips['trip_date'])
fct_trips['rider_count']=pd.to_numeric(fct_trips['rider_count'])

start_date='2024-07-01'
end_date='2024-09-30'
filtered_fct_trips=fct_trips[(fct_trips['trip_date']>=start_date) & (fct_trips['trip_date']<=end_date)]
filtered_fct_trips=filtered_fct_trips[filtered_fct_trips['ride_type']=='UberPool']
filtered_fct_trips=filtered_fct_trips.assign(earnings_per_mile=(filtered_fct_trips['total_earnings']/filtered_fct_trips['total_distance']))

more_than_two_riders=filtered_fct_trips[filtered_fct_trips['rider_count']>2]

more_than_two_riders=more_than_two_riders['earnings_per_mile'].mean()
print(filtered_fct_trips)
print(more_than_two_riders)
