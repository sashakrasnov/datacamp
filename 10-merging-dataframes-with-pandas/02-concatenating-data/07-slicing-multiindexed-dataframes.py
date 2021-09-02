'''
Slicing MultiIndexed DataFrames

This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).

You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.

pandas has been imported for you as pd and the DataFrame medals is already in your namespace.

INSTRUCTIONS

*   Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
*   Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
*   Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
*   Slice all the data on medals won by the United Kingdom. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.
'''

import pandas as pd

medals = []
medal_types = ['bronze', 'silver', 'gold']

# ---

for medal in medal_types:

    file_name = "../datasets/summer-olympic-medals/%s_top5.csv" % medal

    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# ---

# Sort the entries of medals
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])

'''
> medals
                        Total
       Country               
bronze United States   1052.0
       Soviet Union     584.0
       United Kingdom   505.0
       France           475.0
       Germany          454.0
silver United States   1195.0
       Soviet Union     627.0
       United Kingdom   591.0
       France           461.0
       Italy            394.0
gold   United States   2088.0
       Soviet Union     838.0
       United Kingdom   498.0
       Italy            460.0
       Germany          407.0

> medals_sorted
                        Total
       Country               
bronze France           475.0
       Germany          454.0
       Soviet Union     584.0
       United Kingdom   505.0
       United States   1052.0
gold   Germany          407.0
       Italy            460.0
       Soviet Union     838.0
       United Kingdom   498.0
       United States   2088.0
silver France           461.0
       Italy            394.0
       Soviet Union     627.0
       United Kingdom   591.0
       United States   1195.0

> medals_sorted.loc[('bronze','Germany')]
Total    454.0
Name: (bronze, Germany), dtype: float64

> medals_sorted.loc['silver']
                 Total
Country               
France           461.0
Italy            394.0
Soviet Union     627.0
United Kingdom   591.0
United States   1195.0

> medals_sorted.loc[idx[:,'United Kingdom'], :]
                       Total
       Country
bronze United Kingdom  505.0
gold   United Kingdom  498.0
silver United Kingdom  591.0
'''