# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

  # Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales
# Please print your final result or dataframe

fct_sales['sale_date']=pd.to_datetime(fct_sales['sale_date'])
start_date='2025-01-01'
end_date='2025-03-31'
fct_sales['sale_amount']=fct_sales['sale_amount'].fillna(0.00)
fct_sales=fct_sales[(fct_sales['sale_date']>=start_date) &(fct_sales['sale_date']<=end_date)]
# fct_sales_unique=fct_sales[['celebrity_id','product_id','sale_amount']].drop_duplicates()
final=fct_sales.groupby(['celebrity_id','product_id'])['sale_amount'].sum().reset_index()
final=final.sort_values(by='sale_amount',ascending=False)
print(final)
print(final.head(3).to_string(index=False))
# should the other columns be included

# it still says my answer isn't quite correct
