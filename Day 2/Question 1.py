#What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring 'Electronics' in its name during October 2024? This analysis will help determine which electronics-related categories are performing optimally
# The following tables are loaded as pandas DataFrames with the same names: fct_ad_performance, dim_product

import pandas as pd
#merge fct_ad_performance and dim_product on the column product_id
new_df = pd.merge(fct_ad_performance,dim_product, on="product_id")

#filter the dataframe to only include  rows where the product_category contains the string 'Electronics'
new_df = new_df[new_df['product_category'].str.contains("Electronics")]

#convert the recorded_date to datetime format
new_df['recorded_date']=pd.to_datetime(new_df['recorded_date'] )



#filter created_date include only those that were recorded in October 2024
start_date = '2024-10-01'
end_date = '2024-10-31'
new_df = new_df[(new_df['recorded_date'] >= start_date) & (new_df ['recorded_date'] <= end_date)]

#create a new column and assign to it the value of the click-through rate (clicks/impressions * 100)
new_df=new_df.assign(ctr=(new_df["clicks"] / new_df["impressions"])*100)

#group by product_category and calculate the average ctr
new_df = new_df.groupby('product_category')['ctr'].mean()



print(new_df)


