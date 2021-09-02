'''
Filling missing data (imputation) by group

Many statistical and machine learning packages cannot determine the best action to take when missing data entries are encountered. Dealing with missing data is natural in pandas (both in using the default behavior and in defining a custom behavior). In Chapter 1, you practiced using the .dropna() method to drop missing values. Now, you will practice imputing missing values. You can use .groupby() and .transform() to fill missing data appropriately for each group.

Your job is to fill in missing 'age' values for passengers on the Titanic with the median age from their 'gender' and 'pclass'. To do this, you'll group by the 'sex' and 'pclass' columns and transform each group with a custom function to call .fillna() and impute the median value.

The DataFrame has been pre-loaded as titanic. Explore it in the IPython Shell by printing the output of titanic.tail(10). Notice in particular the NaNs in the 'age' column.

INSTRUCTIONS
*   Group titanic by 'sex' and 'pclass'. Save the result as by_sex_class.
*   Write a function called impute_median() that fills missing values with the median of a series. This has been done for you.
*   Call .transform() with impute_median on the 'age' column of by_sex_class.
*   Print the output of titanic.tail(10). This has been done for you - hit 'Submit Answer' to see how the missing values have now been imputed.
'''

import pandas as pd

titanic = pd.read_csv('../datasets/titanic.csv')

# ---

# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex', 'pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

'''
      pclass  survived                                     name     sex   age  sibsp  parch  ticket     fare cabin embarked boat   body home.dest
1299       3         0                      Yasbeck, Mr. Antoni    male  27.0      1      0    2659  14.4542   NaN        C    C    NaN       NaN
1300       3         1  Yasbeck, Mrs. Antoni (Selini Alexander)  female  15.0      1      0    2659  14.4542   NaN        C  NaN    NaN       NaN
1301       3         0                     Youseff, Mr. Gerious    male  45.5      0      0    2628   7.2250   NaN        C  NaN  312.0       NaN
1302       3         0                        Yousif, Mr. Wazli    male  25.0      0      0    2647   7.2250   NaN        C  NaN    NaN       NaN
1303       3         0                    Yousseff, Mr. Gerious    male  25.0      0      0    2627  14.4583   NaN        C  NaN    NaN       NaN
1304       3         0                     Zabour, Miss. Hileni  female  14.5      1      0    2665  14.4542   NaN        C  NaN  328.0       NaN
1305       3         0                    Zabour, Miss. Thamine  female  22.0      1      0    2665  14.4542   NaN        C  NaN    NaN       NaN
1306       3         0                Zakarian, Mr. Mapriededer    male  26.5      0      0    2656   7.2250   NaN        C  NaN  304.0       NaN
1307       3         0                      Zakarian, Mr. Ortin    male  27.0      0      0    2670   7.2250   NaN        C  NaN    NaN       NaN
1308       3         0                       Zimmerman, Mr. Leo    male  29.0      0      0  315082   7.8750   NaN        S  NaN    NaN       NaN
'''