# Introduction to Numpy
# Keep in mind that numpy (NUMerical PYthon) is here to help with computing
# 
# Compared to the list, Numpy has advantage not only in computation but also flexibility


import numpy as np

# For example, we want to add each element for each index
a=[1,2,3]
b=[3,4,5]
c=a+b
c

# In Numpy
np_a=np.array([1,2,3])
np_b=np.array([3,4,5])
np_c=np_a+np_b
np_c

# In order to do that, list should be written like this
a=[1,2,3]
b=[3,4,5]
c=[]
for i,j in zip(a,b):
    d=i+j
    c.append(d)
c

# Another Example
print(np_a/2)

# Create 1D matrix with specified value
array_1D = np.array([1,2,3])
array_1D

# An array also can be calculated with addition or other operations
np.array([1,2,3,-1])+1

# Create 2D matrix with specified value
array_2D = np.array([[1,2],[3,4],[5,6]])
array_2D

# Slicing is an activity to take certain elements from a matrix, use index(from 0)!
print(array_2D[1,1])
print(array_2D[:,1])

# Create a matrix with range value
print(np.arange(10))
print(np.arange(3,10))
print(np.arange(3,10,2))

# how to make a zero matrix with specific size
array_zeros = np.zeros((5,6))
array_zeros

# how to make a matrix of contents with all values = 1
array_ones = np.ones((5,5))
array_ones

# how to make identity matrix
array_identity = np.eye((5), dtype=np.str)
array_identity

# NUMPY - SIMPLE MATH
# Numpy can sum all value inside matrix
np.sum(array_ones)

# Generate a uniform random number 0-1
array_randomuniform = np.random.rand(2,2)
array_randomuniform

# Generate a standard normal random number
array_randomnormalstandard = np.random.randn(4,2)
array_randomnormalstandard

# Generate an interval number
array_lin = np.linspace(0,100,5)
array_lin

# How to multiply matrix -> Remember linear algebra -> column of matrix 1 = row of matrix 2
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
c = np.dot(a,b)
c

print(np.size(c)) # Return the size or number of elements in matrix
print(np.shape(c)) # Return the shape of matrix

print(np.pi)
print(np.sin(90))