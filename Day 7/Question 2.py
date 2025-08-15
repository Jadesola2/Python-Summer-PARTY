#For Q1 2025 (January 1st through March 31st, 2025), can you list the unique combinations of celebrity_id and product_id from the sales table? This will ensure that each collaboration is accurately accounted for in the analysis of Nike's marketing performance.


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

#convert the sale_date column elements to datetime objects. Then filter the dataframe to only include sales than occurred in Q1
fct_sales['sale_date']=pd.to_datetime(fct_sales['sale_date'])
start_date='2025-01-01'
end_date='2025-03-31'
fct_sales=fct_sales[(fct_sales['sale_date']>=start_date) &(fct_sales['sale_date']<=end_date)]

#crop the dataframe to only include celebrity_id and product_id and drop duplicates
fct_sales=fct_sales[['celebrity_id','product_id']].drop_duplicates()
print(fct_sales.to_string(index=False))
