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
pivot_table=ice_cream_sales_data.pivot_table(index='month',columns='temperature_range',values='sales_volume',aggfunc='sum')

print(pivot_table)


