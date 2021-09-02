'''
Explore the Jobs dataset

In this exercise, you will explore the new jobs DataFrame, which contains the unemployment rate of different industries in the USA during the years of 2000-2010. As you will see, the dataset contains time series for 16 industries and across 122 timepoints (one per month for 10 years). In general, the typical workflow of a Data Science project will involve data cleaning and exploration, so we will begin by reading in the data and checking for missing values.
'''

import pandas as pd

url_jobs = '../datasets/ch5_employment.csv'

'''
INSTRUCTIONS

We've imported pandas as pd.

*   Read in the the csv file located at url_jobs into a DataFrame called jobs and review the data type of each column.
*   Convert the datestamp column in jobs to the datetime type.
*   Set the datestamp column as the index of jobs.
*   Print the number of missing values in each column of jobs.
'''

# Read in jobs file
jobs = pd.read_csv(url_jobs)

# Review the first five lines of your DataFrame
print(jobs.head(5))

# Review the type of each column in your DataFrame
print(jobs.dtypes)

# Convert datestamp column to a datetime object
jobs['datestamp'] = pd.to_datetime(jobs['datestamp'])

# Set the datestamp columns as the index of your DataFrame
jobs = jobs.set_index('datestamp')

# Check the number of missing values in each column
print(jobs.isnull().sum())