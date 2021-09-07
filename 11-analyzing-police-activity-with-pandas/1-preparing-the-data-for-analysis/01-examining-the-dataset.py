'''
Examining the dataset

Throughout this course, you'll be analyzing a dataset of traffic stops in Rhode Island that was collected by the Stanford Open Policing Project (https://openpolicing.stanford.edu/).

Before beginning your analysis, it's important that you familiarize yourself with the dataset. In this exercise, you'll read the dataset into pandas, examine the first few rows, and then count the number of missing values.

INSTRUCTIONS

*   Import pandas using the alias pd.
*   Read the file police.csv into a DataFrame named ri.
*   Examine the first 5 rows of the DataFrame (known as the "head").
*   Count the number of missing values in each column: Use .isnull() to check which DataFrame elements are missing, and then take the .sum() to count the number of True values in each column.
'''

# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('../datasets/RI_cleaned.csv', nrows=100000, low_memory=False)

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

