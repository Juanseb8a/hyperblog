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

#  Drop column row
# data = pd.read_csv('data.csv')
# # print(data.head(n=5))

# # print(type(data))

# #  removing the first row
# # data.drop(data.index[0], inplace=True)

# #  removing the first two rows
# data.drop(data.index[:2], inplace=True)
# print(data)

# # drop column named latitude
# data.drop(['Latitude'], axis = 1, inplace = True)

#  Subsetting and Indexing
data = pd.read_csv('data.csv')
# print(data)

# selecting all entries from index 2 onwards
# print(data[6:])

# #  select entries at even index locations
# print(data[::2])

# #  specify the ranges of rows and columns TO SELECT 
# print(data.iloc[0:8,0:7])

# #  select all columns for rows of index values 0 and 10
# print(data.iloc[[0,10], : ])

#  isolate rows and columns
# print(data[['Countries', 'Name in English']][4:8])

# isolate by row names
# print(data[data.Countries == "Italy"])

#  isolate by row labels
# x = data.loc[data['Countries'].isin(['Italy','Germany'])]
# print(x.head(15))

#  replace "Number of speakers" with "Number"
df = data[:]
df = pd.DataFrame(data=df)
# df.rename(columns={'Number of Speakers' : 'Number'}, inplace = True)
# print(df.head(5))
# print(data[(data.Countries=="India") & (data.Degree of endangerment == "Vulnerable")])

# df.drop(['Name in English'], axis = 1)
# df = df.drop(['Description of the location','Name in French', 'Name in English', 'Name in Spanish', 'Latitude', 'Longitude'], axis = 1)
# df = df[df.Countries == "India"]
# df.rename(columns={df.columns[7] : "Number"}, inplace = True)
# df = df[(df.Countries == "India") & (df.Number < 1751489.0)]

# print(df.columns)
# print(df)

# #  sort in descending order
# large = data.sort_values(by='Number of speakers', ascending=False)
# print(large.head(n=10))

# # sort in descending order
# small = data.sort_values(by='Number of speakers', ascending = True)
# print(small.head(n=10))

# # grouping by
# group_by = data.groupby(['Degree of endangerment']).count()
# print(group_by)

# group on basis of two qualitative columns
# bygroup_CnS = data.groupby(['Countries', 'Degree of endangerment'])
# print(data.head(10))
# print(bygroup_CnS.count())

# group number of speañers by group labels (row names) from countries
# x = data['Number of speakers'].groupby(data['Countries'])
# print(x.head(n=10))

# Lambda functions
# Identify which of the languages have fewer than 5k speakers

# data['vfew'] = data['Number of speakers'].apply(lambda x: x <= 5000)
# # print(data.head(n=6))

# print(data['Degree of endangerment'].value_counts())

# #  tabulate our data on basis of two columns
# x = pd.crosstab(data["Country codes alpha 3"], data["Degree of endangerment"], margins=True)
# print(x.head(4))
# # print(data.columns)

# def perConvert(var):
#     return var/float(var[-1])

# x = pd.crosstab(data["Country codes alpha 3"], data["Degree of endangerment"], margins = True).apply(perConvert, axis = 1)
# print(x.head(3))

# dstack = data.stack()
# print(dstack)

# patient = pd.DataFrame({'FirstName' : ['Bill', 'Jane'], 'LastName' : ['Shakespeare', 'Austen'], 'BloodType' : ['o+', 'B+'],
#                         'wt' : [85, 62]})
# print(patient)

#  melting
#  use melt()
# you have a data that has one or more columns that are identifier variables
# while all other columns are considered measured variables

# print(pd.melt(patient, id_vars = ['FirstName','LastName'], var_name = 'measurements'))

# x = data[0:15]
# print(x.head(3))

#  drop id
# x = x.drop('ID', axis=1)
# print(x.head(4))

#  drop multiple columns
# x1 = data[0:15]
# # x1 = data.drop(columns=['Latitude', 'Longitude'])
# print(x1.head(4))

# melted = pd.melt(x1, id_vars = ['Latitude', 'Longitude'], value_name = "No")
# print(melted)

# Pivoting
data1 = pd.read_csv('ranking_table.csv')
# print(data1.head(5))

# print(data1.pivot_table(index='power_index', columns='progress', values='rank', aggfunc='sum'))
# print(data1.columns)

#  Rank and sorting
s = pd.Series(range(4), index=['d','a','b','c'])
# print(s)

#  sort from index a to d
# print(s.sort_index())

# columns will be arranged alphabetically
# sorted = data.sort_index(axis=1)
# print(sorted)

#  columns will be arranged Z-A
# print(data.sort_index(axis=1, ascending=False))

#  Sort the values of a column in a table
# print(data.sort_values(by='ID'))

#  sort the values of two columns in a table
# print(data.sort_values(by=['ID','Latitude']))

# x = data.iloc[0:8,0:8]
# # print(x.head(5))

# x['ITCANBEANYTHING'] = x['ID'].rank(ascending=1)
# print(x.head(6))

# Video: Concatenate
# df1 = pd.DataFrame([['a', 1],['b', 2]], columns=['letter', 'number'])
# print(df1)

# df2 = pd.DataFrame([['c', 3],['d', 4]],columns=['letter', 'number'])
# print(df2)

# df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']], columns=['letter', 'number', 'animal'])
# print(df3)

# print(pd.concat([df1, df2]))

# # only columns common for both data frames are joined together
# pd.concat([df1, df2], join="inner")

