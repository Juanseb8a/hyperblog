import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import csv
from collections import Counter


plt.style.use("fivethirtyeight")

# Matplotlib Tutorial 4

# minutes = [1,2,3,4,5,6,7,8,9]

# player1 = [1,2,3,3,4,4,4,4,5]
# player2 = [1,1,1,1,2,2,2,3,4]
# player3 = [1,1,1,2,2,2,3,3,3]

# labels = ['player_1','player_2','player_3']
# colors = ['#6d904f', '#fc4f30', '#008fd5']
# # plt.pie([1,1,1], labels= ["Player 1", "Player 2", "Player 3"])
# plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# plt.legend(loc='lower left')

# plt.title("Mt Awesome Stack Plot")
# plt.tight_layout()
# plt.show()

#  Matplotlib Tutorial 3
#  Excercise 2

# plt.style.use("fivethirtyeight")

# slices = [59219,55466,47544,36443,35917]
# # slices = [59219,55466,47544,36443,35917,31991,27097,23030,20524,18523,18017,7920,7331,7201,5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# # labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++',
# # 'TypeScript', 'C', 'Others(s)', 'Ruby', 'Go', 'Assembly']
# explode=[0.1,0,0,0.3,0]
# plt.pie(slices, labels=labels, explode=explode, shadow = True, startangle = 90, 
#  autopct = '%1.1f%%',wedgeprops={'edgecolor':'black'})

# plt.title("MyAwesome Pie Chart")
# plt.tight_layout()
# plt.show()

#  Excercise 1
# plt.style.use("fivethirtyeight")

# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['blue', 'red', 'yellow', 'green']

# plt.pie(slices, labels = labels, wedgeprops={'edgecolor': 'black'})

# plt.title("My Awesome Chart")
# plt.tight_layout()
# plt.show()

# Matplotlib Tutorial (Part 2)
# data = pd.read_csv('data.txt')
# ids = data['Responder_id']
# lang_responses = data['LanguagesWorkedWith']

# language_counter = Counter()

# # with open('data.txt') as csv_file:
# #     csv_reader = csv.DictReader(csv_file)
# #     language_counter = Counter()

# for response in lang_responses:
#     language_counter.update(response.split(';'))
    
# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# languages.reverse()
# popularity.reverse()

# plt.barh(languages, popularity)

# plt.title("Most popular Languages")
# plt.ylabel("Number of People Who Use")

# plt.tight_layout()
# plt.show()
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
# sample_data = pd.read_csv('sample_data.csv')

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