'''
Loading & examining our data

Let's begin by loading and examining two datasets: One that contains a set of user demographics and the other a set of data relating to in-app purchases for our meditation app.

INSTRUCTIONS

*   Import pandas as pd.
*   Load the file 'customer_data.csv' as a DataFrame called customer_data.
*   Load the file 'inapp_purchases.csv' as a DataFrame called app_purchases.
*   Print the columns of customer_data and then app_purchases using their .columns attribute.
'''

# Import pandas 
import pandas as pd 

# Load the customer_data
customer_data = pd.read_csv('../datasets/customer_data.csv')

# Load the app_purchases
app_purchases = pd.read_csv('../datasets/inapp_purchases.csv')

# Print the columns of customer data
print(customer_data.columns)

# Print the columns of app purchases
print(app_purchases.columns)