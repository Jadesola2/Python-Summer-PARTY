# Create a pivot table to summarize the total sales volume of ice cream products by month and temperature range.
# Use the following temperature bins where each bin excludes the upper bound but includes the lower bound:
# - Less than 60 degrees
# - 60 to less than 70 degrees
# - 70 to less than 80 degrees
# - 80 to less than 90 degrees
# - 90 to less than 100 degrees
# - 100 degrees or more


#convert the sale_date column elements into datetime objects and create a new column for the months
ice_cream_sales_data['sale_date']=pd.to_datetime(ice_cream_sales_data['sale_date'])
ice_cream_sales_data['month']=ice_cream_sales_data['sale_date'].dt.to_period('M')



# Define bin edges
bins = [float('-inf'), 60, 70, 80, 90, 100, float('inf')]

# Define labels
labels = [
    'Less than 60°F',
    '60–69°F',
    '70–79°F',
    '80–89°F',
    '90–99°F',
    '100°F or more'
]

# Apply pd.cut
ice_cream_sales_data['temperature_range'] = pd.cut(
    ice_cream_sales_data['temperature'],
    bins=bins,
    labels=labels,
    right=False  # makes intervals left-inclusive: [60, 70)
)
#creat a pivot table
pivot_table=ice_cream_sales_data.pivot_table(index='month',columns='temperature_range',values='sales_volume',aggfunc='sum')

print(pivot_table)


