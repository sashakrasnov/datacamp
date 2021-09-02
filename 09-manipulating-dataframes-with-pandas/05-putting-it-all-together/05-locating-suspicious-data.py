'''
Locating suspicious data

You will now inspect the suspect record by locating the offending row.

You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.

INSTRUCTIONS

*   Create a Boolean Series with a condition that captures the only row that has medals.Event_gender == 'W' and medals.Gender == 'Men'. Be sure to use the & operator.
*   Use the Boolean Series to create a DataFrame called suspect with the suspicious row.
*   Print suspect. This has been done for you, so hit 'Submit Answer' to see the result.
'''

import pandas as pd

medals = pd.read_csv('../datasets/all_medalists.csv')

# ---

# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)

'''
         City  Edition      Sport Discipline            Athlete  NOC Gender     Event Event_gender   Medal
23675  Sydney     2000  Athletics  Athletics  CHEPCHUMBA, Joyce  KEN    Men  marathon            W  Bronze
'''