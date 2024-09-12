import pandas as pd
import numpy as np

# Load your CSV data (replace 'your_data.csv' with the actual file path)
df = pd.read_csv('AppUsage.csv')

# Extract month and year from the date column
df['statdate'] = pd.to_datetime(df['date'])
df['statmonth'] = df['statdate'].dt.month
df['statyear'] = df['statdate'].dt.year

# Group by month and calculate statistics
monthly_stats = df.groupby(['statyear', 'statmonth'])['application_usage'].agg(
    Mean=np.mean,
    Median=np.median,
    Std=np.std,
    Min=np.min,
    Max=np.max
)

# Check if data already exists in the text file
existing_months = set()
try:
    with open('descriptive_stats.txt', 'r') as file:
        for line in file:
            year, month = map(int, line.strip().split('-'))
            existing_months.add((year, month))
except FileNotFoundError:
    pass

# Save to text file (append if not already present)
with open('descriptive_stats.txt', 'a') as file:
    for idx, stats in monthly_stats.items():
        year, month = idx
        if (year, month) not in existing_months:
            file.write(f"{year}-{month:02d}: {stats}\n")
            # You can customize the format of the saved data as needed

