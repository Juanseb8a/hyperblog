import pandas as pd
import numpy as np
import html5lib
import json

dict = {'a' : 3, 'b' : 'cat', 'c' : 2.5}
# print(pd.Series(dict))

# oneD = pd.Series([100,'cat',310,'gog',500],['Amy','Bobby','Cat','Don','Emma'])
oneD = pd.Series([100,'cat',310,'gog',500],index=['Amy','Bobby','Cat','Don','Emma'])

# print(oneD)

# print(oneD.loc[['Cat','Emma']])

# print(oneD[[0,3,4]])

# print(oneD.iloc[1])

# print('Cat' in oneD)

#  DataFrames - 2D data structure, Stores data in tabular form (rows and columns)
#  cclass 'pandas.core.frame.DataFrame'

d = {'A' : pd.Series([100., 200.,  300.], index=['apple','pear','orange']),
     'B' : pd.Series([111., 222., 333., 4444.],index=['apple','pear','orange','melon'])}

df = pd.DataFrame(d)
# print(df)

# print(type(df))

# print(df.index)

# print(df.columns)

# print(pd.DataFrame(df, index=['orange', 'melon', 'apple'], columns=['A']))

#  Reading CSV files

# df1 = pd.read_csv('countries.csv')
# # print(df1.head(6))

# df2 = pd.read_csv('data.txt', sep = ';')
# print(df2.head(5))

# Reading HTML files

# uss = pd.read_html('https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_the_Philippines')
# print(type(uss))

# # grab dataframe from index 1, table 2 of the tentative WFS series
# u = uss[1]
# print(u)

#  Reading json files