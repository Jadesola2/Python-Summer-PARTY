 # Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_ad_performance, dim_product
# Please print your final result or dataframe

import Pandas as pd
new_df = pd.merge(fct_ad_performance,dim_product, on="product_id")
# new_df = new_df[new_df['product_category'].str.contains("Electronics")]
new_df['recorded_date']=pd.to_datetime(new_df['recorded_date'] )



# #filter created_date
start_date = '2024-10-01'
end_date = '2024-10-31'
new_df = new_df[(new_df['recorded_date'] >= start_date) & (new_df ['recorded_date'] <= end_date)]
# print(new_df)

new_df=new_df.assign(ctr=(new_df["clicks"] / new_df["impressions"])*100)
# print(new_df)
mean=new_df['ctr'].mean()
new_df2 = new_df.groupby('product_category')['ctr'].mean()

high_performing_categories=new_df2[new_df2>mean]

print(high_performing_categories)

