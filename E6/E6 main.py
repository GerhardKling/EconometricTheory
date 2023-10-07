"""
Econometric Theory
The data matrix in Python
@author: Gerhard Kling
"""

import numpy as np

#Operations with numerics
a = 7
b = 2

#Square root
print(np.sqrt(a))

#Creating Numpy array
#The all one vector
ones = np.ones(5)

#Change entries in vector
ones[0] = 3
ones[-1] = 8

#Or assign array as follows
vector_a = np.array([1, 2, 34, 7])

#Create a matrix 
matrix = np.zeros((3, 4)) 

#Change entry in matrix using indexing
matrix[0, 1] = 22

#Shape and size attributes
print(matrix.shape)
print(matrix.size)

#Pre-multiply the 3 by 4 matrix with a suitable all one row vector
ones = np.ones((1, matrix.shape[0]))

#Matrix multiplication
matrix_new = np.matmul(ones, matrix)

#Identity matrix
matrix_identity = np.eye(5)

#Horizontal and vertical stacks
#Three explanatory variables
matrix_a = np.array([[1, 2, 3], [3, 6, 8]])

#Additional observations
matrix_b = np.array([[0, -2, 3], [4, -5, 1], [2, -1, 0]])

#Add to data matrix X
print("Vertical")
X = np.vstack([matrix_a, matrix_b])

#Create a matching all one vector
ones = np.ones((X.shape[0],1))

#Add to data matrix X
print("Horizontal")
X = np.hstack([ones, X])
