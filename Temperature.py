import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_temperature_for_year(df, year):
    year_data = df[df['Formatted Date'].dt.year == year]
    monthly_avg = year_data.groupby(year_data['Formatted Date'].dt.month)['Temperature (C)'].mean()
    
    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', color='skyblue')
    
    plt.title(f'Average Monthly Temperatures for {year}')
    plt.xlabel('Month')
    plt.ylabel('Average Temperature (C)')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()

def plot_for_comparing_temperature(df):
    yearly_avg = df.groupby(df['Formatted Date'].dt.year)['Temperature (C)'].mean()

    yearly_avg = yearly_avg[yearly_avg.index != 2005]
    plt.figure(figsize=(10, 5))
    yearly_avg.plot(kind='bar', color='lightblue')
    plt.title('Yearly Average Temperatures')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()