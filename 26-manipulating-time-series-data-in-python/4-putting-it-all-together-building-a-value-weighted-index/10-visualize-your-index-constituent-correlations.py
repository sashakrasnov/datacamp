'''
Visualize your index constituent correlations

To better understand the characteristics of your index constituents, you can calculate the return correlations.

Use the daily stock prices or your index companies, and show a heatmap of the daily return correlations!
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

stock_prices = pd.read_csv('../datasets/stock_data/stock_data.csv', index_col='Date', parse_dates=['Date'])

'''
INSTRUCTIONS

We have already imported pandas as pd, matplotlib.pyplot as plt, and seaborn as sns. We have also loaded the historical price series of your index constituents into the variable stock_prices.

*   Inspect stock_prices using .info().
*   Calculate the daily returns for stock_prices and assign the result to returns.
*   Calculate the pairwise correlations for returns, assign them to correlations and print the result.
*   Plot a seaborn annotated heatmap of the daily return correlations with the title 'Daily Return Correlations'.
'''

# Inspect stock_prices here
print(stock_prices.info())

# Calculate the daily returns
returns = stock_prices.pct_change()

# Calculate and print the pairwise correlations
correlations = returns.corr()
print(correlations)

# Plot a heatmap of daily return correlations
sns.heatmap(correlations, annot=True)
plt.title('Daily Return Correlations')
plt.show()