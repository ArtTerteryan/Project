import matplotlib.pyplot as plt

def plot_monthly_humidity_for_year(df, year):
    year_data = df[df['Formatted Date'].dt.year == year]
    monthly_avg = year_data.groupby(year_data['Formatted Date'].dt.month)['Humidity'].mean()
    
    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', color='skyblue')
    
    plt.title(f'Average Monthly Humidity for {year}')
    plt.xlabel('Month')
    plt.ylabel('Humidity')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()