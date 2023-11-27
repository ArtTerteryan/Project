import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from FormattedDate import string_to_object
from Temperature import plot_monthly_temperature_for_year
from Temperature import plot_for_comparing_temperature
from Humidity import plot_monthly_humidity_for_year
from Visibility import plot_monthly_visibility_of_year
from Visibility import plot_visibility_vs_temperature
from outliers import implementation
from PrecipType import one_hot
from CloudCover import remove_uniques
from Summary import histogram_for_summary
from Pressure import pressure_and_other

file_path = '/home/artur/Desktop/Project/weatherHistory.csv'
weather_dataset = pd.read_csv(file_path)

string_to_object(weather_dataset)
remove_uniques(weather_dataset)
implementation(weather_dataset)
one_hot(weather_dataset)

year_input = int(input("Enter the year you want to analyze: "))
plot_monthly_temperature_for_year(weather_dataset, year_input)
plot_monthly_humidity_for_year(weather_dataset, year_input)
plot_monthly_visibility_of_year(weather_dataset, year_input)
plot_for_comparing_temperature(weather_dataset)
plot_visibility_vs_temperature(weather_dataset, 'Temperature (C)', 'Visibility (km)')
histogram_for_summary(weather_dataset)
pressure_and_other(weather_dataset)