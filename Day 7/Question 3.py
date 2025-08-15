#For Q1 2025 (January 1st through March 31st, 2025), can you rank the unique celebrity collaborations based on their total sales amounts and list the top 3 collaborations in descending order? This will help recommend the most successful partnerships for Nike's future product drop strategies.

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

#convert the sale_date column elements into datetime objects, fill null sale_amounts and filter the dataframe to only include sales that occurred in Q1
fct_sales['sale_date']=pd.to_datetime(fct_sales['sale_date'])
start_date='2025-01-01'
end_date='2025-03-31'
fct_sales['sale_amount']=fct_sales['sale_amount'].fillna(0.00)
fct_sales=fct_sales[(fct_sales['sale_date']>=start_date) &(fct_sales['sale_date']<=end_date)]

#get the total sale_amount for each celebrity_id and product_id collaboration
final=fct_sales.groupby(['celebrity_id','product_id'])['sale_amount'].sum().reset_index()

#sort the dataframe by sale_amount in descending order
final=final.sort_values(by='sale_amount',ascending=False)
print(final)

#get the top 3 collaborations
print(final.head(3).to_string(index=False))
