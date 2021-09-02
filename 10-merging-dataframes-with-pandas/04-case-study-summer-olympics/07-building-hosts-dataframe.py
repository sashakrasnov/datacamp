'''
Building hosts DataFrame

Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.

Once created, you will subset the Edition and NOC columns and set Edition as the Index.

There are some missing NOC values; you will set those explicitly.

Finally, you'll reset the Index & print the final DataFrame.

INSTRUCTIONS

*   Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
*   Clean up hosts by subsetting and setting the Index.
*   Extract the columns 'Edition' and 'NOC'.
*   Set 'Edition' column as the Index.
*   Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
*   Reset the index of hosts using .reset_index(), and then hit 'Submit Answer' to see what hosts looks like!
'''

import pandas as pd

editions = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv', sep='\t')[['Edition', 'Grand Total', 'City', 'Country']]

ioc_codes = pd.read_csv('../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv')[['Country', 'NOC']]

# ---

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition','NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)

'''
> hosts.loc[hosts.NOC.isnull()]

         NOC
Edition
1972     NaN
1980     NaN
1988     NaN

> hosts
    Edition  NOC
0      1896  GRE
1      1900  FRA
2      1904  USA
3      1908  GBR
4      1912  SWE
5      1920  BEL
6      1924  FRA
7      1928  NED
8      1932  USA
9      1936  GER
10     1948  GBR
11     1952  FIN
12     1956  AUS
13     1960  ITA
14     1964  JPN
15     1968  MEX
16     1972  FRG
17     1976  CAN
18     1980  URS
19     1984  USA
20     1988  KOR
21     1992  ESP
22     1996  USA
23     2000  AUS
24     2004  GRE
25     2008  CHN
'''