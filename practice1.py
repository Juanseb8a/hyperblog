import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style



# Matplotlib Tutorial (Part )



# Matplotlib Tutorial (Part 1)
#  -------------------------------------------
# plt.style.use('ggplot')
# # plt.xkcd()

# dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexes = np.arange(len(dev_x))
# width = 0.25

# dev_y = [38496, 42000, 46752, 49320, 53200, 
# 56000, 62316, 64928, 67317, 68748, 73752]

# py_dev_y = [45375, 48876, 53850, 57287, 
# 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# js_dev_y = [37810, 43515,46823,49293,53437,
# 56373, 62375, 66674, 68745, 68746, 74583]

# # plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
# # plt.plot(dev_x, py_dev_y, color='#5a7d9a', linewidth=3, marker='o', label='Python')
# # plt.plot(dev_x, js_dev_y, color='#123456', linestyle='--', label="Javascript")

# plt.bar(x_indexes-width, dev_y, width=width, color="#444444", label="All Devs")
# plt.bar(x_indexes, py_dev_y, width=width, color="#008fd5", label="Python")
# plt.bar(x_indexes+width, js_dev_y, width=width, color="#e5ae38", label="JavaScript")

# plt.legend()

# plt.xticks(ticks=x_indexes, labels=dev_x)

# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')

# # plt.grid(True)
# plt.tight_layout()
# plt.show()

#  -------------------------------------------------------------------------


# Basics of plotting
# x = [1,  2,  3]
# y = [1,  4,  9]
# z = [10,  5,  0]

# plt.plot(x,  z)
# plt.plot(x,  y)

# plt.title("test plot")
# plt.xlabel("x")
# plt.ylabel("y and z")

# plt.legend(["this is z",  "this is y"])
# plt.show()

#  Basics of getting data
sample_data = pd.read_csv('sample_data.csv')

#  Getting a column 
# print(sample_data.column_c)

#  Getting a specific value 
# print(sample_data.column_c.iloc[0])

# Plotting columns of a data set
# plt.plot(sample_data.column_a,  sample_data.column_b,  'o')
# plt.plot(sample_data.column_a,  sample_data.column_c)

# print(sample_data.column_c)
# print(sample_data.column_b)

# plt.legend(["this is a vs b",  "this is a vs c"])
# plt.show()

#  Compare the population grwoth in the US and China
# Getting all data in a variable
# data = pd.read_csv('countries.csv')
# print(data)

# afghanistan = data[data.country == 'Afghanistan']
# china = data[data.country == "China"]

# print(afghanistan.population)

# plt.plot(afghanistan.year,  afghanistan.population/afghanistan.population.iloc[0]*100)
# plt.plot(china.year,  china.population/china.population.iloc[0]*100)
# plt.legend(["This is Afghanistan",  "This is China"])
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.show()


# Practice before Project 1
# plt.style.use('seaborn')
# x = [5,  7,  8,  5,  6,  7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7,  4,  3,  9,  1,  3,  2,  5,  2,  4,  8,  7,  1,  6,  4,  9,  7,  7,  5,  1]

# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

#  1st project: Plot a Scatter plot
# data = pd.read_csv('iris.data')

# print(data)