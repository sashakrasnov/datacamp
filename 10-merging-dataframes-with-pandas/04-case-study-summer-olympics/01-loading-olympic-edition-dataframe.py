'''
Loading Olympic edition DataFrame

In this chapter, you'll be using The Guardian's Olympic medal dataset.

Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.

Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.

For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.

INSTRUCTIONS

*   Read file_path into a DataFrame called editions. The identifier file_path has been pre-defined with the filename 'Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'. You'll have to use the option sep='\t' because the file uses tabs to delimit fields (pd.read_csv() expects commas by default).
*   Select only the columns 'Edition', 'Grand Total', 'City', and 'Country' from editions.
*   Print the final DataFrame editions in entirety (there are only 26 rows). This has been done for you, so hit 'Submit Answer' to see the result!
'''

#Import pandas
import pandas as pd

# Create file path: file_path
file_path = '../datasets/summer-olympic-medals/Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)

'''
    Edition  Grand Total         City                     Country
0      1896          151       Athens                      Greece
1      1900          512        Paris                      France
2      1904          470    St. Louis               United States
3      1908          804       London              United Kingdom
4      1912          885    Stockholm                      Sweden
5      1920         1298      Antwerp                     Belgium
6      1924          884        Paris                      France
7      1928          710    Amsterdam                 Netherlands
8      1932          615  Los Angeles               United States
9      1936          875       Berlin                     Germany
10     1948          814       London              United Kingdom
11     1952          889     Helsinki                     Finland
12     1956          885    Melbourne                   Australia
13     1960          882         Rome                       Italy
14     1964         1010        Tokyo                       Japan
15     1968         1031  Mexico City                      Mexico
16     1972         1185       Munich  West Germany (now Germany)
17     1976         1305     Montreal                      Canada
18     1980         1387       Moscow       U.S.S.R. (now Russia)
19     1984         1459  Los Angeles               United States
20     1988         1546        Seoul                 South Korea
21     1992         1705    Barcelona                       Spain
22     1996         1859      Atlanta               United States
23     2000         2015       Sydney                   Australia
24     2004         1998       Athens                      Greece
25     2008         2042      Beijing                       China
'''