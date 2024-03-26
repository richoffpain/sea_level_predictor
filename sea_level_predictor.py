import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress





def draw_plot():
    # Read data from file
    df = pd.read_csv('epa_sea_level.csv')
    #print(df.index)
    
    

    # Create scatter plot
    x = df.Year
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, color='blue')

    # Create first line of best fit
    """
        for  y = mx + b
            _ y dependent variable
            _ m is the slope
            _ x independent variable
            _ b the intercept

            Best fit will represent the overall minimum distance between two points from the line
    """
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    #plt.plot(x, intercept + (slope * x), color='orange')
    #plt.show()
    years_after = np.arange(1880, 2051)
    plt.plot(years_after, intercept + (slope * years_after), color='red')
    #plt.show()

    


    # Create second line of best fit
    sub_data = df[df['Year'] >= 2000]
    x_subdata_year = sub_data['Year']
    sub_years_aft = np.arange(2000, 2051)
    y_subdata_csiro = sub_data['CSIRO Adjusted Sea Level']
    plt.scatter(x_subdata_year, y_subdata_csiro, color='orange')
    slope_sub, intercept_sub, r_value_sub, p_value_sub, std_err_sub = linregress(x_subdata_year, y_subdata_csiro)
    plt.plot(sub_years_aft, slope_sub*sub_years_aft + intercept_sub, color='green')
    #print(x_subdata)
    #years_dsp = np.arange(x, 2051)
    #print(years_dsp)


  

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    #plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

#draw_plot()