import pandas as pd
import matplotlib.pyplot as plt
from PrecipType import one_hot

def histogram_for_summary(df):
    one_hot(df)
    
    threshold = 5000
    summary_counts = df['Summary'].value_counts()
    below_threshold = summary_counts[summary_counts < threshold].index.tolist()
    df['Summary_Grouped'] = df['Summary'].apply(lambda x: 'Other' if x in below_threshold else x)

    rain_frequency = df.groupby('Summary_Grouped')['Rain'].sum()
    snow_frequency = df.groupby('Summary_Grouped')['Snow'].sum()

    fig, axes = plt.subplots(1, 2, figsize=(15, 8))

    axes[0].bar(rain_frequency.index, rain_frequency.values, color='blue')
    axes[0].set_title('Rain Frequency for Grouped Weather Summaries')
    axes[0].set_xlabel('Weather Summary')
    axes[0].set_ylabel('Frequency of Rain')
    axes[0].tick_params(axis='x', rotation=45)

    axes[1].bar(snow_frequency.index, snow_frequency.values, color='gray')
    axes[1].set_title('Snow Frequency for Grouped Weather Summaries')
    axes[1].set_xlabel('Weather Summary')
    axes[1].set_ylabel('Frequency of Snow')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()