import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

plt.show()
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize = (10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(df['Year'].min(), 2051)
    y_values = intercept + slope*x_values
    plt.plot(x_values, y_values, 'r', label=f'Fit (Full Data): y = {slope:.2f}x + {intercept:.2f}')


    # Create second line of best fit
    min_year_recent = 2000
    max_year_recent = 2050  
    slope_recent, intercept_recent, R, P, STDerr = linregress(df['Year'][(df['Year'] >= min_year_recent) & (df['Year'] <= max_year_recent)], df['CSIRO Adjusted Sea Level'][(df['Year'] >= min_year_recent) & (df['Year'] <= max_year_recent)])
    x_values_recent = range(min_year_recent, max_year_recent + 1)
    y_values_recent = slope_recent * x_values_recent + intercept_recent

    plt.plot(x_values_recent, y_values_recent, 'g', label=f'Fit (Since 2000): y = {slope_recent:.2f}x + {intercept_recent:.2f}')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()