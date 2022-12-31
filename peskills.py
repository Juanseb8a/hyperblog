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
# df = pd.read_json("skorea.json")
# df = pd.read_json("https://api.github.com/repositories/858127/issues?per_page=5")
# df.head(1)

#  WRANGLING DATA
#  Dealing with missing values (NAs)

df = pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6]])
# print(df)

# #  check if the data frames contains NA
# print(df.isnull())

# #  drop NA values
# #  all rows with cells containing NA will be dropped
# print(df.dropna())

# # drop columns where cells have NAs
# print(df.dropna(axis=1))

# #  thresh parameter lets you specify a minimum of nin-null values for the row/column
# # to be kept
# print(df.dropna(thresh=2))


#  Filling no Values (NA) cells
#  fill NA entries with zero
# print(df.fillna(0))

# # specify a forward-fill to propagate the previous value forward
# print(df.fillna(method="ffill"))

# #  fill forward column wise
# print(df.fillna(method="ffill", axis=1))

# #  back-fill to propagate the bext values backwards
# print(df.fillna(method="bfill"))

# Data handling: Basics of Conditional Data Selection
# data = pd.read_csv('data.csv')

# # print(data.head(n=6))

# # Isolate a column
# print(data['Countries'])

# # Isolate 2 columns
# print(data[['Countries', 'Name in English']])

# # Isolate rows
# print(data[3:10])

# # conditional selection
# print(data[data['Number of speakers']<5000])