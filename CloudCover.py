def remove_uniques(weather_dataset):
    if 'Loud Cover' in weather_dataset.columns and len(weather_dataset['Loud Cover'].unique()) == 1:
        weather_dataset.drop(columns='Loud Cover', inplace=True)
    return weather_dataset 
