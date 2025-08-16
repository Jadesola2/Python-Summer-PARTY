#Identify the combination of rider count and total distance that results in the highest average driver earnings per UberPool ride between July 1st and September 30th, 2024. This analysis directly recommends optimal trip combination strategies to maximize driver earnings.


#convert the 'trip_date column elements into datetime objects and the rider_count into numeric objects
fct_trips['trip_date']=pd.to_datetime(fct_trips['trip_date'])
fct_trips['rider_count']=pd.to_numeric(fct_trips['rider_count'])


#filter the dataframe to only include rides that occurred between July 1st and September 30th, 2024
start_date='2024-07-01'
end_date='2024-09-30'
filtered_fct_trips=fct_trips[(fct_trips['trip_date']>=start_date) & (fct_trips['trip_date']<=end_date)]


#filter the dataframe to only include rides with ride_type=='UberPool'
filtered_fct_trips=filtered_fct_trips[filtered_fct_trips['ride_type']=='UberPool']

#calculate the average total_earnings per combination of rider_count and total_distance
filtered_fct_trips=filtered_fct_trips.groupby(['rider_count','total_distance'])['total_earnings'].mean()

#sort the values in descending order
filtered_fct_trips=filtered_fct_trips.sort_values(ascending=False)

#reset the index and rename the column appropriately
filtered_fct_trips=filtered_fct_trips.reset_index()
filtered_fct_trips=filtered_fct_trips.rename(columns={'total_earnings' : 'average_driver_earnings_per_ride'})

print(filtered_fct_trips.head(1).to_string(index=False))
