# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

fct_sales['sale_date']=pd.to_datetime(fct_sales['sale_date'])
start_date='2025-01-01'
end_date='2025-03-31'
fct_sales=fct_sales[(fct_sales['sale_date']>=start_date) &(fct_sales['sale_date']<=end_date)]
missing_data=fct_sales['sale_amount'].isnull()
missing_sales=fct_sales[missing_data]
print(missing_sales)
