import seaborn as sns
import matplotlib.pyplot as plt

def one_hot(weather_dataset):
    weather_dataset['Precip Type'] = weather_dataset['Precip Type'].fillna('None')
    weather_dataset['Rain'] = (weather_dataset['Precip Type'] == 'rain').astype(int)
    weather_dataset['Snow'] = (weather_dataset['Precip Type'] == 'snow').astype(int)
    print(weather_dataset[['Precip Type', 'Rain', 'Snow']])