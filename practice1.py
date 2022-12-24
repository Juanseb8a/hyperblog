import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Basics of plotting
# x = [1, 2, 3]
# y = [1, 4, 9]
# z = [10, 5, 0]

# plt.plot(x,z)
# plt.plot(x,y)

# plt.title("test plot")
# plt.xlabel("x")
# plt.ylabel("y and z")

# plt.legend(["this is z", "this is y"])
# plt.show()

#  Basics of getting data
sample_data = pd.read_csv('sample_data.csv')

#  Getting a column 
# print(sample_data.column_c)

#  Getting a specific value 
# print(sample_data.column_c.iloc[0])

# Plotting columns of a data set
# plt.plot(sample_data.column_a, sample_data.column_b, 'o')
# plt.plot(sample_data.column_a, sample_data.column_c)

# print(sample_data.column_c)
# print(sample_data.column_b)

# plt.legend(["this is a vs b","this is a vs c"])
# plt.show()

#  Compare the population grwoth in the US and China
# Getting all data in a variable
data = pd.read_csv('countries.csv')
print(data)

afghanistan = data[data.country == 'Afghanistan']
china = data[data.country == "China"]

print(afghanistan.population)

plt.plot(afghanistan.year, afghanistan.population/afghanistan.population.iloc[0]*100)
plt.plot(china.year, china.population/china.population.iloc[0]*100)
plt.legend(["This is Afghanistan", "This is China"])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()