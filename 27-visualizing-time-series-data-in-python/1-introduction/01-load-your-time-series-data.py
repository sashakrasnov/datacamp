'''
Load your time series data

The most common way to import time series data in Python is by using the pandas library. You can use the read_csv() from pandas to read the contents of a file into a DataFrame. This can be achieved using the following command:

|   df = pd.read_csv("name_of_your_file.csv")

Once your data is loaded into Python, you can display the first rows of your DataFrame by calling the .head(n=5) method, where n=5 indicates that you want to print the first five rows of your DataFrame.

In this exercise, you will read in a time series dataset that contains the number of "great" inventions and scientific discoveries from 1860 to 1959, and display its first five rows.
'''

url_discoveries = '../datasets/ch1_discoveries.csv'

'''
INSTRUCTIONS

*   Import the pandas library using the pd alias.
*   Read in the time series data from the csv file located at url_discoveries into a DataFrame called discoveries.
*   Print the first 5 lines of the DataFrame using the .head() method.
'''

# Import pandas
import pandas as pd

# Read in the file content in a DataFrame called discoveries
discoveries = pd.read_csv(url_discoveries)

# Display the first five lines of the DataFrame
print(discoveries.head())