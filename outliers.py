import seaborn as sns
import matplotlib.pyplot as plt

def calculate_z_score(df, column):
    mean = df[column].mean()
    std = df[column].std()
    return (df[column] - mean) / std

def remove_outliers_z_score(df, column):
    mean = df[column].mean()
    std = df[column].std()
    z_scores = (df[column] - mean) / std
    return df[(z_scores >= -3) & (z_scores <= 3)]

def implementation(weather_dataset):
    outliers = {}
    numeric_columns = weather_dataset.select_dtypes(include=['float64', 'int64']).columns
    for column in numeric_columns:
        z_scores = calculate_z_score(weather_dataset, column)
        outliers[column] = weather_dataset[(z_scores < -3) | (z_scores > 3)]
    outlier_counts = {column: len(outliers_df) for column, outliers_df in outliers.items()}
    print(f"Number of outliers in each column before removal: {outlier_counts}\n")

    plt.figure(figsize=(15, 10))
    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(len(numeric_columns), 2, 2*i-1)
        sns.boxplot(y=weather_dataset[column])
        plt.title(f'Before: {column}')

    for column in numeric_columns:
        weather_dataset = remove_outliers_z_score(weather_dataset, column)

    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(len(numeric_columns), 2, 2*i)
        sns.boxplot(y=weather_dataset[column])
        plt.title(f'After: {column}')

    plt.tight_layout()
    plt.show()