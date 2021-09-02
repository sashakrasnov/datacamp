'''
Reading your data with CSV Reader and Establishing your Data Containers

Let's get started! The exercises in this chapter are intentionally more challenging, to give you a chance to really solidify your knowledge. Don't lose heart if you find yourself stuck; think back to the concepts you've learned in previous chapters and how you can apply them to this crime dataset. Good luck!

Your data file, crime_sampler.csv contains the date (1st column), block where it occurred (2nd column), primary type of the crime (3rd), description of the crime (4th), description of the location (5th), if an arrest was made (6th), was it a domestic case (7th), and city district (8th).

Here, however, you'll focus only 4 columns: The date, type of crime, location, and whether or not the crime resulted in an arrest.

Your job in this exercise is to use a CSV Reader to load up a list to hold the data you're going to analyze.

INSTRUCTIONS

*   Import the Python csv module.
*   Create a Python file object in read mode for crime_sampler.csv called csvfile.
*   Create an empty list called crime_data.
*   Loop over a csv reader on the file object :
    *   Inside the loop, append the date (first element), type of crime (third element), location description (fifth element), and arrest (sixth element) to the crime_data list.
*   Remove the first element (headers) from the crime_data list.
*   Print the first 10 records of the crime_data list. This has been done for you, so hit 'Submit Answer' to see the result!
'''

# Import the csv module
import csv

# Create the file object: csvfile
csvfile = open('../datasets/crime_sampler.csv', 'r')

# Create an empty list: crime_data
crime_data = []

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):

    # Append the date, type of crime, location description, and arrest
    crime_data.append((row[0], row[2], row[4], row[5]))
    
# Remove the first element from crime_data
crime_data.pop(0)

# Print the first 10 records
print(crime_data[:10])