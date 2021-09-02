'''
Many-to-many data merge

The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.

Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.

Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.

Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.

INSTRUCTIONS

*   Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous two exercises. Save the result as m2o.
*   Merge the m2o and survey DataFrames on the 'ident' column of m2o and 'taken' column of survey.
*   Hit 'Submit Answer' to print the first 20 lines of the merged DataFrame!
'''

# Merge site and visited: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2o and survey: m2m
m2m = pd.merge(left=m2o, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))

'''
> site
    name    lat    long
0   DR-1 -49.85 -128.57
1   DR-3 -47.15 -126.72
2  MSK-4 -48.87 -123.40

> visited
   ident   site       dated
0    619   DR-1  1927-02-08
1    622   DR-1  1927-02-10
2    734   DR-3  1939-01-07
3    735   DR-3  1930-01-12
4    751   DR-3  1930-02-26
5    752   DR-3         NaN
6    837  MSK-4  1932-01-14
7    844   DR-1  1932-03-22

> survey
    taken person quant  reading
0     619   dyer   rad     9.82
1     619   dyer   sal     0.13
2     622   dyer   rad     7.80
3     622   dyer   sal     0.09
4     734     pb   rad     8.41
5     734   lake   sal     0.05
6     734     pb  temp   -21.50
7     735     pb   rad     7.22
8     735    NaN   sal     0.06
9     735    NaN  temp   -26.00
10    751     pb   rad     4.35
11    751     pb  temp   -18.50
12    751   lake   sal     0.10
13    752   lake   rad     2.19
14    752   lake   sal     0.09
15    752   lake  temp   -16.00
16    752    roe   sal    41.60
17    837   lake   rad     1.46
18    837   lake   sal     0.21
19    837    roe   sal    22.50
20    844    roe   rad    11.25

> m2o
    name     lat     long  ident   site       dated
0   DR-1  -49.85  -128.57    619   DR-1  1927-02-08
1   DR-1  -49.85  -128.57    622   DR-1  1927-02-10
2   DR-1  -49.85  -128.57    844   DR-1  1932-03-22
3   DR-3  -47.15  -126.72    734   DR-3  1939-01-07
4   DR-3  -47.15  -126.72    735   DR-3  1930-01-12
5   DR-3  -47.15  -126.72    751   DR-3  1930-02-26
6   DR-3  -47.15  -126.72    752   DR-3         NaN
7  MSK-4  -48.87  -123.40    837  MSK-4  1932-01-14

> m2m
     name     lat     long  ident   site       dated  taken person  quant  reading  
0    DR-1  -49.85  -128.57    619   DR-1  1927-02-08    619   dyer    rad     9.82  
1    DR-1  -49.85  -128.57    619   DR-1  1927-02-08    619   dyer    sal     0.13  
2    DR-1  -49.85  -128.57    622   DR-1  1927-02-10    622   dyer    rad     7.80  
3    DR-1  -49.85  -128.57    622   DR-1  1927-02-10    622   dyer    sal     0.09  
4    DR-1  -49.85  -128.57    844   DR-1  1932-03-22    844    roe    rad    11.25  
5    DR-3  -47.15  -126.72    734   DR-3  1939-01-07    734     pb    rad     8.41  
6    DR-3  -47.15  -126.72    734   DR-3  1939-01-07    734   lake    sal     0.05  
7    DR-3  -47.15  -126.72    734   DR-3  1939-01-07    734     pb   temp   -21.50  
8    DR-3  -47.15  -126.72    735   DR-3  1930-01-12    735     pb    rad     7.22  
9    DR-3  -47.15  -126.72    735   DR-3  1930-01-12    735    NaN    sal     0.06  
10   DR-3  -47.15  -126.72    735   DR-3  1930-01-12    735    NaN   temp   -26.00  
11   DR-3  -47.15  -126.72    751   DR-3  1930-02-26    751     pb    rad     4.35  
12   DR-3  -47.15  -126.72    751   DR-3  1930-02-26    751     pb   temp   -18.50  
13   DR-3  -47.15  -126.72    751   DR-3  1930-02-26    751   lake    sal     0.10  
14   DR-3  -47.15  -126.72    752   DR-3         NaN    752   lake    rad     2.19  
15   DR-3  -47.15  -126.72    752   DR-3         NaN    752   lake    sal     0.09  
16   DR-3  -47.15  -126.72    752   DR-3         NaN    752   lake   temp   -16.00  
17   DR-3  -47.15  -126.72    752   DR-3         NaN    752    roe    sal    41.60  
18  MSK-4  -48.87  -123.40    837  MSK-4  1932-01-14    837   lake    rad     1.46  
19  MSK-4  -48.87  -123.40    837  MSK-4  1932-01-14    837   lake    sal     0.21  
20  MSK-4  -48.87  -123.40    837  MSK-4  1932-01-14    837    roe    sal    22.50
'''
