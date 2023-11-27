import matplotlib.pyplot as plt

def plot_monthly_visibility_of_year(df, year):
    year_data = df[df['Formatted Date'].dt.year == year]
    monthly_avg = year_data.groupby(year_data['Formatted Date'].dt.month)['Visibility (km)'].mean()
    
    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', color='skyblue')
    
    plt.title(f'Average Monthly Visibility for {year}')
    plt.xlabel('Month')
    plt.ylabel('Visibility (km)')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()

def plot_visibility_vs_temperature(weather_dataset, temperature_column, visibility_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(weather_dataset[temperature_column], weather_dataset[visibility_column], alpha=0.5)
    
    plt.title('Visibility vs Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Visibility')
    plt.show()