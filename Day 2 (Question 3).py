  # Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_ad_performance, dim_product
# Please print your final result or dataframe

new_df = pd.merge(fct_ad_performance,dim_product, on="product_id", how='left')

new_df['recorded_date']=pd.to_datetime(new_df['recorded_date'] )



# #filter created_date
start_date = '2024-10-01'
end_date = '2024-10-31'
new_df = new_df[(new_df['recorded_date'] >= start_date) & (new_df ['recorded_date'] <= end_date)]
# print(new_df)

new_df=new_df.assign(ctr=(new_df["clicks"] / new_df["impressions"])*100)

mean=new_df['ctr'].mean()
new_df2 = new_df.groupby('product_category')['ctr'].mean()



high_performing_categories=new_df2[new_df2 > mean]
high_performing_categories=high_performing_categories.to_frame(name='average_ctr')
high_performing_categories=high_performing_categories.assign(average_ctr=((high_performing_categories['average_ctr']-mean)/mean)*100)
print(high_performing_categories)


# print(high_performing_categories)





