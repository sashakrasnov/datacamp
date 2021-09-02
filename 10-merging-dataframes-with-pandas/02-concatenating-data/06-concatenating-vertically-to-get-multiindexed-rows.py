'''
Concatenating vertically to get MultiIndexed rows

When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keys as the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.

Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset. Once again, pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

INSTRUCTIONS

*   Within the for loop:
    *   Read file_name into a DataFrame called medal_df. Specify the index to be 'Country'.
    *   Append medal_df to medals.
*   Concatenate the list of DataFrames medals into a single DataFrame called medals. Be sure to use the keyword argument keys=['bronze', 'silver', 'gold'] to create a vertically stacked DataFrame with a MultiIndex.
*   Print the new DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!
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

# Print medals
print(medals)
'''
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
'''