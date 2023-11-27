import seaborn as sns
import matplotlib.pyplot as plt
def pressure_and_other(df):
    # Grouping 'Summary' categories with occurrences less than 5000 into an 'Other' category
    summary_counts = df['Summary'].value_counts()
    low_count_summary_types = summary_counts[summary_counts < 5000].index
    df['Grouped Summary'] = df['Summary'].replace(low_count_summary_types, 'Other')

    # Box plot for Grouped Weather Summary vs Pressure
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Grouped Summary', y='Pressure (millibars)', data=df)
    plt.title('Air Pressure Distribution by Grouped Weather Summary')
    plt.xlabel('Grouped Weather Summary')
    plt.ylabel('Pressure (millibars)')
    plt.xticks(rotation=45)
    plt.show()

    # Creating subplots for multiple analyses
    fig, axes = plt.subplots(2, 2, figsize=(15, 8))

    # Scatter plot for Visibility vs Pressure
    sns.scatterplot(ax=axes[0, 0], data=df, x='Visibility (km)', y='Pressure (millibars)')
    axes[0, 0].set_title('Visibility (km) vs. Pressure (millibars)')
    axes[0, 0].set_xlabel('Visibility (km)')
    axes[0, 0].set_ylabel('Pressure (millibars)')

    # Scatter plot for Wind Speed vs Pressure
    sns.scatterplot(ax=axes[0, 1], data=df, x='Wind Speed (km/h)', y='Pressure (millibars)')
    axes[0, 1].set_title('Wind Speed (km/h) vs. Pressure (millibars)')
    axes[0, 1].set_xlabel('Wind Speed (km/h)')
    axes[0, 1].set_ylabel('Pressure (millibars)')

    # Box plot for Precip Type vs Pressure
    sns.boxplot(ax=axes[1, 1], x='Precip Type', y='Pressure (millibars)', data=df)
    axes[1, 1].set_title('Air Pressure Distribution by Precip Type')
    axes[1, 1].set_xlabel('Precip Type')
    axes[1, 1].set_ylabel('Pressure (millibars)')

    # Scatter plot for Temperature vs Pressure
    sns.scatterplot(ax=axes[1, 0], data=df, x='Temperature (C)', y='Pressure (millibars)')
    axes[1, 0].set_title('Temperature (C) vs. Pressure (millibars)')
    axes[1, 0].set_xlabel('Temperature (C)')
    axes[1, 0].set_ylabel('Pressure (millibars)')

    plt.tight_layout()
    plt.show()
