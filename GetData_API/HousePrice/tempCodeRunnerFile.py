
print(df[(df['Price'] < 100000) & (df['Price'] > 80000) & (df['Neighborhood'] == 'North')].sort_values('Price'))