import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # 3. Line of best fit using ALL data (1880 to 2050)
    slope1, intercept1, r1, p1, se1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(df['Year'].min(), 2051)
    sea_level_pred1 = [slope1 * year + intercept1 for year in years_extended]
    ax.plot(years_extended, sea_level_pred1, color='red', label='Best Fit Line (All Data)')

    # 4. Line of best fit using data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    sea_level_pred2 = [slope2 * year + intercept2 for year in years_recent]
    ax.plot(years_recent, sea_level_pred2, color='green', label='Best Fit Line (2000 onwards)')

    # 5. Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig
