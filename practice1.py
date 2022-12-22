import numpy as np
import pandas as pd

# print(np.__version__)

# --- Ejercicio 1
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])
c = a + b*a
print(c)


# --- Ejercicio 2
# a = np.array([[1,2,3],
#               [4,5,6]])

# b = 2*a
# print(b)


# --- Ejercicio 3 (Create an identity Matrix)
# i = np.eye(4)
# print(i)


# --- Ejercicio 4
# a = np.array([x for x in range(27)])
# o = a.reshape((3,3,3))
# print(o)


# --- Ejercicio 5
# a = np.array([[2.5, 3.8, 1.5],
#               [4.7, 2.9, 1.56]])

# o = a.astype('int')
# print(o)


# --- Ejercicio 6
# Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array

# a = np.array([[1,0,1]
#             ,[1,1,1]
#             ,[0,0,0]])

# o = a.astype('bool')
# print(o)


# --- Ejercicio 7
# Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in 2D arrays)
# a1 = np.array([[1,2,3]
#               ,[4,5,6]])

# a2 = np.array([[7,8,9]
#               ,[10,11,12]])
# o = np.hstack((a1, a2))
# print(o)

# --- Ejercicio 8
# Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)

# a1 = np.array([[1,2]
#               ,[3,4]
#               ,[5,6]])
# a2 = np.array([[7,8]
#               ,[9,10]
#               ,[10,11]])

# o = np.vstack((a1,a2))
# print(o)

# --- Ejercicio 9
# Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
# list_of_numbers = [x for x in range(0,101,2)]

# # o = np.array(list_of_numbers)
# o = np.arange(0,101,2)
# print(o)

# --- Ejercicio 10
# From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
# a = np.array([1,2,3,4,5])
# b = np.array([1,3,2,4,5])

# print(np.where(a == b))


# Ejercicio 11
# Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)
# o = np.linspace(0,100,5)
# print(o)


# Ejercicio 12
# Output a matrix (numpy array) of dimension 2-by-3 with each and every value equal to 5
# o =  np.full((2,3),5)
# print(o)  

# a = np.ones((2,3))
# o = 5 * a
# o = o.astype('int')
# print(o)


# Ejercicio 13
# Output an array by repeating a smaller array of 2 dimensions, 10 times

# a = np.array([[1,2,3] 
#              ,[4,5,6]])
# o = np.tile(a, 10)
# print(o)


# Ejercicio 14
# Output a 5-by-5 array of random integers between 0 (inclusive) and 10 (exclusive)

# np.random.seed(123) #setting the seed
# o = np.random.randint(0, 10, size = (5,5))
# print(o)


#  Ejercicio 15
# Output a 3-by-3 array of random numbers following normal distribution
# np.random.seed(123)
# o = np.random.normal(size = (3,3))
# print(o)


#  Ejercicio 16
# Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices (as a numpy array)

# a = np.array([[1,2,3]
#              ,[4,5,6]
#              ,[7,8,9]])
# b = np.array([[2,3,4]
#              ,[5,6,7]
#              ,[8,9,10]])

# o = a@b
# o = np.matmul(a,b)
# print(o)


#  Ejercicio 17
# Output the transpose of a matrix (as numpy array)
# a = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])

# a_transpose = a.T
# print(a_transpose)

# Ejercicio 18
# Calculate the sine of an array of angles (in radians) using NumPy

# angles = np.array([3.14, 3.14/2, 6.28])
# sine_of_angles  = np.sin(angles)
# print('Sine of the given array of angles = ', sine_of_angles)

# Ejercicio 19
# Calculate the cosine similarity of 2 vectors (as numpy arrays)

# angles = np.array([3.14, 3.14/2, 6.28])
# cosine_of_angles = np.cos(angles)
# print('Cosine of the given array of angles = ', cosine_of_angles)

# Ejercicio 20
# Output the array element indexes such that the array elements appear in the ascending order
# array = np.array([10,1,5,2])
# indexes = np.argsort(array)
# print(indexes)

# Ejercicio 21
# Crear un vector con valores dentro del rango 10 a 49

# array = np.arange(10, 50)
# print(array)

# #  Invertir el vector
# flipped = np.flip(array)
# print(flipped)


# Crear una matriz 3x3 con valores de 0 a 8
array = np.array() 