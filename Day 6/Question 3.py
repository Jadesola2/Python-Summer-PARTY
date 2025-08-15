# Can you detect any outliers in the monthly sales volume using the Inter Quartile Range (IQR) method? A month is considered an outlier if falls below Q1 minus 1.5 times the IQR or above Q3 plus 1.5 times the IQR.


#convert the sale_date column elements into datetime object and create a new column for the months
ice_cream_sales_data['sale_date']=pd.to_datetime(ice_cream_sales_data['sale_date'])
ice_cream_sales_data['month']=ice_cream_sales_data['sale_date'].dt.to_period('M')

#for each month, calculate the total sale volume. Then, reset the index
ice_cream_sales_data=ice_cream_sales_data.groupby('month')['sales_volume'].sum().reset_index()

#calculate Q1 and Q3
Q1=ice_cream_sales_data['sales_volume'].quantile(0.25)
Q3=ice_cream_sales_data['sales_volume'].quantile(0.75)

#calculate the Inter Quartile Range (IQR)
IQR=Q3-Q1

#calculate the loer and upper bound
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#create a dataframe that consists of the outliers
outliers=ice_cream_sales_data[(ice_cream_sales_data['sales_volume']<lower_bound)|(ice_cream_sales_data['sales_volume']>upper_bound)]
print(outliers.to_string(index=False))
