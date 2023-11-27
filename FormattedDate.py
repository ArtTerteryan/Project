import pandas as pd
import matplotlib.pyplot as plt

def string_to_object(weather_dataset):
    weather_dataset['Formatted Date'] = pd.to_datetime(weather_dataset['Formatted Date'], utc=True)
    weather_dataset['Formatted Date'] = weather_dataset['Formatted Date'].dt.tz_convert(None)