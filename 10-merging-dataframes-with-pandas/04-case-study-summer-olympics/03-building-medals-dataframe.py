'''
Building medals DataFrame

Here, you'll start with the DataFrame editions from the previous exercise.

You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).

You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.

The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).

Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().

INSTRUCTIONS

*   Within the for loop:
    *   Create the file path. This has been done for you.
    *   Read file_path into a DataFrame. Assign the result to the year key of medals_dict.
    *   Select only the columns 'Athlete', 'NOC', and 'Medal' from medals_dict[year].
    *   Create a new column called 'Edition' in the DataFrame medals_dict[year] whose entries are all year.
*   Concatenate the dictionary of DataFrames medals_dict into a DataFame called medals. Specify the keyword argument ignore_index=True to prevent repeated integer indices.
*   Print the first and last 5 rows of medals. This has been done for you, so hit 'Submit Answer' to see the result!
'''

import pandas as pd

file_path = '../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

editions = pd.read_csv(file_path, sep='\t')[['Edition', 'Grand Total', 'City', 'Country']]

summers = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t', skiprows=4)

# ---

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:
    # Create the file path: file_path
    #file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    #medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    #medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]

    # Will use single file instead of separated files
    summer_year = summers['Edition'] == year
    medals_dict[year] = summers[summer_year][['Athlete', 'NOC', 'Medal']]

    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year 
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict, ignore_index=True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())

'''
> medals.head()
              Athlete  NOC   Medal  Edition       
0       HAJOS, Alfred  HUN    Gold     1896       
1    HERSCHMANN, Otto  AUT  Silver     1896       
2   DRIVAS, Dimitrios  GRE  Bronze     1896       
3  MALOKINIS, Ioannis  GRE    Gold     1896       
4  CHASAPIS, Spiridon  GRE  Silver     1896       

> medals.tail()
                    Athlete  NOC   Medal  Edition 
29211        ENGLICH, Mirko  GER  Silver     2008 
29212  MIZGAITIS, Mindaugas  LTU  Bronze     2008 
29213       PATRIKEEV, Yuri  ARM  Bronze     2008 
29214         LOPEZ, Mijain  CUB    Gold     2008 
29215        BAROEV, Khasan  RUS  Silver     2008 
'''