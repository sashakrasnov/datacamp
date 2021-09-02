'''
Grouping by multiple columns

In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.

The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.

Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.

The DataFrame has been pre-loaded as titanic.

INSTRUCTIONS

*   Group by the 'pclass' column and save the result as by_class.
*   Aggregate the 'survived' column of by_class using .count(). Save the result as count_by_class.
*   Print count_by_class. This has been done for you.
*   Group titanic by the 'embarked' and 'pclass' columns. Save the result as by_mult.
*   Aggregate the 'survived' column of by_mult using .count(). Save the result as count_mult.
*   Print count_mult. This has been done for you, so hit 'Submit Answer' to view the result.
'''

import pandas as pd

titanic = pd.read_csv('../datasets/titanic.csv')

# ---

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked', 'pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)

'''
> titanic.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1309 entries, 0 to 1308
Data columns (total 14 columns):
pclass       1309 non-null int64
survived     1309 non-null int64
name         1309 non-null object
sex          1309 non-null object
age          1046 non-null float64
sibsp        1309 non-null int64
parch        1309 non-null int64
ticket       1309 non-null object
fare         1308 non-null float64
cabin        295 non-null object
embarked     1307 non-null object
boat         486 non-null object
body         121 non-null float64
home.dest    745 non-null object
dtypes: float64(3), int64(4), object(7)
memory usage: 143.2+ KB

> count_by_class
pclass
1    323
2    277
3    709
Name: survived, dtype: int64

> count_mult
embarked  pclass
C         1         141
          2          28
          3         101
Q         1           3
          2           7
          3         113
S         1         177
          2         242
          3         495
Name: survived, dtype: int64
'''