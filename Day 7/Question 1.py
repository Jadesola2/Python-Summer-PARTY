#For Q1 2025 (January 1st through March 31st, 2025), can you identify all records of celebrity collaborations from the sales data where the sale_amount is missing? This will help us flag incomplete records that could impact the analysis of Nike's product performance.


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

#convert the sale_date elements into datetime object and filter the dataframe to include only celebrity collaborations that occurred in Q1
fct_sales['sale_date']=pd.to_datetime(fct_sales['sale_date'])
start_date='2025-01-01'
end_date='2025-03-31'
fct_sales=fct_sales[(fct_sales['sale_date']>=start_date) &(fct_sales['sale_date']<=end_date)]

#get the rows where sale_amount is missing
missing_data=fct_sales['sale_amount'].isnull()
missing_sales=fct_sales[missing_data]
print(missing_sales)
